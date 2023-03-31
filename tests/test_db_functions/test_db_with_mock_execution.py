import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

import testing.db_functions

class PatchedConnection:
    def __init__(self, conn_string):
        pass

    def cursor(self):
        return PatchedCursor()

class PatchedCursor:
    data = []
    def __init__(self):
        self._index = 0

    def execute(self, query):
        if query == TEST_QUERY:
            self.data = [("Id1", 1), ("Id2", 1), ("Id3", 2)]
        else:
            raise ValueError(f"Unexpected query:\n{query}")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self.data):
            return_value = self.data[self._index]
            self._index += 1
            return return_value
        raise StopIteration

TEST_QUERY = "SELECT * FROM my_table"

def test_count_rows(monkeypatch):
    monkeypatch.setattr(
        psycopg2,
        "connect",
        lambda conn_string: PatchedConnection(conn_string)
    )

    assert testing.db_functions.count_rows(TEST_QUERY) == 3