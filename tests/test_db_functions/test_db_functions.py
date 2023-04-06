import pandas as pd
from unittest.mock import ANY, call, Mock, patch

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

@patch('testing.db_functions.functions.summarize_field')
@patch('testing.db_functions.functions.fetch_result')
def test_summarize_table_with_mock(mock_fetch_result, mock_summarize_field):
	db_return_table = pd.read_csv('./tests/test_db_functions/mock_table.csv').to_dict('records')

	mock_fetch_result.return_value = (row for row in db_return_table)

	mock_type_check = Mock(side_effect=lambda field: None)
	mock_summarize_field.side_effect = lambda field, data: mock_type_check(field)

	testing.db_functions.summarize_table("SELECT * FROM dummy")

	assert call('IdNumeric') in mock_type_check.mock_calls
	assert call('Value') in mock_type_check.mock_calls
	assert not call('Date') in mock_type_check.mock_calls
	assert not call('IdText') in mock_type_check.mock_calls


def test_summarize_table_with_zero_rows(monkeypatch):
	monkeypatch.setattr(
		testing.db_functions.functions,
		'fetch_result',
		lambda query: (row for row in []) # generator
		)

	assert testing.db_functions.summarize_table("SELECT * FROM dummy") == {}
