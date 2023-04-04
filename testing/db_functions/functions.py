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

def summarize_field(field, field_data):
    # values = [row[field] for row in data if row.get(field, None) is not None]
    # return {
    #     "min": round(min(values), 4),
    #     "max": round(max(values), 4),
    #     "avg": round(st.mean(values), 4),
    #     "std": round(st.stdev(vaues), 4)
    # }

    return {
        "min": round(min(field_data), 4),
        "max": round(max(field_data), 4),
        "avg": round(st.mean(field_data), 4),
        "std": round(st.stdev(field_data), 4)
    }

def summarize_table(query):
    data = pd.DataFrame(data=list(fetch_result(query)))

    if len(data) == 0:
        return {}

    t_data = data.transpose()
    print(t_data)
    print(t_data.loc('IdText'))
    output = {}
    for field in data.columns:
        try:
            output[field] = summarize_field(t_data.loc(field))
        except:
            pass

    return output
