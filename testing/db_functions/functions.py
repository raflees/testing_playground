import json
import pandas as pd
import psycopg2
import statistics as st

def fetch_result(query):
    # Get connection cursor
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()

    # Execute and return query results
    cursor.execute(query)
    cols = [col.name for col in cursor.description]
    for row in cursor:
        yield {cols[i]: val for i, val in enumerate(row)}

def summarize_table(query):
    # Fetches data
    data = pd.DataFrame(data=list(fetch_result(query)))

    # Transposes so we can access all values at once
    t_data = data.transpose()

    # Create a df with the field types so we can filter
    df_types = data.dtypes

    output = {}
    for field in df_types.loc[df_types == 'int64'].index:
        summarize_field(field, t_data.loc[field])
        try:
            output[field] = summarize_field(field, t_data.loc[field])
        except:
            pass

    return output

def summarize_field(field, field_data):
    return {
        "min": round(min(field_data), 4),
        "max": round(max(field_data), 4),
        "avg": round(st.mean(field_data), 4),
        "std": round(st.stdev(field_data), 4)
    }

