import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

from testing.db_functions import count_rows

class PatchedConnection:
    def __init__(self, conn_string):
        self.db_engine = create_engine("sqlite://")
        self.populate_data()

    def populate_data(self):
        pd.read_csv('./tests/test_db_functions/mock_db.csv').to_sql('my_table', con=self.db_engine)

    def cursor(self):
        return PatchedCursor(self.db_engine)

class PatchedCursor:
    data = []

    def __init__(self, db_engine):
        self.db_engine = db_engine
        self._index = 0

    def execute(self, query):
        with self.db_engine.connect() as conn:
            self.data = conn.execute(text(query)).all()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self.data):
            return_value = self.data[self._index]
            self._index += 1
            return return_value
        raise StopIteration

def test_count_rows(monkeypatch):
    # Patching psycopg2.connect() to return the mocked object
    monkeypatch.setattr(
        psycopg2,
        "connect",
        lambda conn_string: PatchedConnection(conn_string)
    )

    assert count_rows("SELECT * FROM my_table") == 3

    