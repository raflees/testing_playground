import pandas as pd

import testing.db_functions

def test_summarize_table(monkeypatch):
	db_return_table = pd.read_csv('./tests/test_db_functions/mock_table.csv').to_dict('records')

	monkeypatch.setattr(
		testing.db_functions.functions,
		'fetch_result',
		lambda query: (row for row in db_return_table) # generator
		)

	assert testing.db_functions.summarize_table("SELECT * FROM dummy") == {
		"IdNumeric": {"min":1, "max":2, "avg":1.3333, "std":0.5774},
		"Value": {"min":-1, "max":10, "avg":4.6667, "std":5.5076}
	}