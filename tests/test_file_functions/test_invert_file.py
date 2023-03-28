from click.testing import CliRunner

import testing

def assert_file_content_equals(file1, file2):
	with open(file1) as f:
		content1 = f.read()
	with open(file2) as f:
		content2 = f.read()

	assert content1 == content2


def test_invert_file(monkeypatch, tmp_path):
	monkeypatch.setattr(
		testing.file_functions,
		'get_inverted_filename',
		lambda filepath: f'{tmp_path}/to_invert_inv.txt')

	testing.cli_tool._invert_file_content('tests/test_file_functions/mock_files/to_invert.txt')

	assert_file_content_equals(
		'tests/test_file_functions/mock_files/expected_output.txt',
		f'{tmp_path}/to_invert_inv.txt'
		)


def test_cli_invert_file(monkeypatch, tmp_path):
	monkeypatch.setattr(
		testing.file_functions,
		'get_inverted_filename',
		lambda filepath: f'{tmp_path}/to_invert_inv.txt')

	runner = CliRunner()

	result = runner.invoke(
		testing.cli,
		['invert-file-content', 'tests/test_file_functions/mock_files/to_invert.txt']
	)

	# All good
	assert not result.exception
	assert result.exit_code == 0

	assert_file_content_equals(
		'tests/test_file_functions/mock_files/expected_output.txt',
		f'{tmp_path}/to_invert_inv.txt'
		)