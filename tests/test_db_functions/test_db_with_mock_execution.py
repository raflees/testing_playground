import pandas as pd
import psycopg2

import testing.db_functions

TEST_QUERY = "SELECT * FROM my_table"

def test_count_rows(monkeypatch):
    monkeypatch.setattr(
        psycopg2,
        "connect",
        lambda conn_string: PatchedConnection(conn_string)
    )

    assert testing.db_functions.count_rows(TEST_QUERY) == 3