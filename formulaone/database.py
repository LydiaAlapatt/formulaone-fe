import boto3

"""
database.py

This module contains functions to interact with the database.
"""


def initialize_database():
    """
    Initialize the database connection.

    :return: Dynamo Resource
    """
    session = boto3.Session()
    dynamo_resource = session.resource(
        'dynamodb',
        region_name='eu-west-1'
    )
    return dynamo_resource


def get_table(table_name):
    """
    Retrieve a table by name.

    :param table_name: Name of the table to retrieve
    :return: Table object
    """
    return initialize_database().Table(table_name)
