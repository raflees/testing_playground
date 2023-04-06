import dataclasses
import pandas as pd
import psycopg2

import testing.db_functions

TEST_QUERY = "SELECT * FROM my_table"

Column = dataclasses.make_dataclass('Column', [('name', str)])

class PatchedConnection:
    def __init__(self, conn_string):
        pass

    def cursor(self):
        return PatchedCursor()

class PatchedCursor:
    data = pd.read_csv(
        './tests/test_db_functions/mock_table.csv'
        ).to_dict('records')

    def __init__(self):
        self._index = 0

    @property
    def description(self):
        return [Column(key) for key in self.data[0].keys()]

    def execute(self, query):
        if query == TEST_QUERY:
            return [list(row.values()) for row in self.data]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self.data):
            return_value = self.data[self._index].values()
            self._index += 1
            return return_value
        raise StopIteration

def test_summarize_table_with_mock_conn(monkeypatch):
    monkeypatch.setattr(
        psycopg2,
        "connect",
        lambda conn_string: PatchedConnection(conn_string)
    )

    assert testing.db_functions.summarize_table("SELECT * FROM dummy") == {
        "IdNumeric": {"min":1, "max":2, "avg":1.3333, "std":0.5774},
        "Value": {"min":-1, "max":10, "avg":4.6667, "std":5.5076}
    }