import json
import psycopg2

def get_cursor():
    connection = psycopg2.connect("dbname=test user=postgres")
    return connection.cursor()

def fetch_result(query):
    # Get connection cursor
    cursor = get_cursor()

    # Execute and return query results
    cursor.execute(query)
    for row in cursor:
        yield row

def count_rows(query):
    return len(list(fetch_result(query)))
