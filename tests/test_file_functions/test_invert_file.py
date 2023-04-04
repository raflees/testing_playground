from click.testing import CliRunner
import filecmp
import pytest

import testing

# autouse makes it to be called every test
@pytest.fixture(autouse=True)
def patch_functions(monkeypatch, tmp_path):
	monkeypatch.setattr(
		testing.file_functions.functions,
		'get_inverted_filename',
		lambda filepath: f'{tmp_path}/to_invert_inv.txt')

def test_invert_file(monkeypatch, tmp_path):
	testing.file_functions.invert_file_content('tests/test_file_functions/mock_files/to_invert.txt')

	assert filecmp.cmp(
		'tests/test_file_functions/mock_files/expected_output.txt',
		f'{tmp_path}/to_invert_inv.txt',
		shallow=False)


def test_cli_invert_file(monkeypatch, tmp_path):
	runner = CliRunner()

	result = runner.invoke(
		testing.cli,
		['invert-file-content', 'tests/test_file_functions/mock_files/to_invert.txt']
	)

	# I can check output directly now
	assert result.output == ''
	assert not result.exception
	assert result.exit_code == 0

	assert filecmp.cmp(
		'tests/test_file_functions/mock_files/expected_output.txt',
		f'{tmp_path}/to_invert_inv.txt',
		shallow=False)

