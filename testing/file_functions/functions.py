import os

from .io import read_file, write_file

def get_inverted_filename(filepath):
	name, ext = os.path.splitext(filepath)
	return name + "_inv" + ext


def invert_text(lines):
	for line in lines:
		inv_line = ''.join([line[i] for i in range(len(line)-1, -1, -1)])
		yield inv_line

def invert_file_content(filepath):
	# Read file
    content = read_file(filepath)

    # Invert every line
    inv_content = '\n'.join(invert_text(content)) + '\n'
    
    # Saves to a new file
    new_filename = get_inverted_filename(filepath)
    write_file(new_filename, inv_content)
