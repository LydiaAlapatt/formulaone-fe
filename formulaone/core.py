# -*- coding: utf-8 -*-

from formulaone.database import get_table
from boto3.dynamodb.conditions import Key
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def get_movies_of_year(year):
    movies = get_table('doc-example-table-movies')
    result = movies.query(KeyConditionExpression=Key('year').eq(year))
    return result['Items']


def convert_data_from_table_to_dataframe(result):
    data = []
    for row in result:
        year = int(row['year'])
        info = row['info']
        data.append({
            'year': year,
            'actors': ', '.join(info.get('actors', [])),
            'release_date': info['release_date'],
            'plot': info['plot'] if 'plot' in info else None,
            'genres': info.get('genres', []),
            'image_url': info['image_url'],
            'directors': ', '.join(info.get('directors', [])),
            'rating': float(info['rating']) if 'rating' in info else None,
            'rank': int(info['rank']),
            'running_time_secs': int(info['running_time_secs']) if 'running_time_secs' in info else None,
            'title': row['title']
        })
    df =  pd.DataFrame(data,
                        columns=['year', 'actors', 'release_date', 'plot', 'genres', 'image_url', 'directors', 'rating',
                                 'rank', 'running_time_secs', 'title'])

    # Perform One-Hot-Encoding on genres using MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    genres_encoded = mlb.fit_transform(df['genres'])
    genres_df = pd.DataFrame(genres_encoded, columns=mlb.classes_)
    df = pd.concat([df.drop(columns=['genres']), genres_df], axis=1)
    return df

