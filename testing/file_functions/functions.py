def get_inverted_filename(filename):
	name, ext = os.path.splitext(filepath)
	return name + "_inv" + ext


def invert_text(lines):
	for line in lines:
		inv_line = ''.join([line[i] for i in range(len(line)-1, -1, -1)])
		yield inv_line