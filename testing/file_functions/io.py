import os.path

def read_file(filepath):
	with open(filepath) as f:
		content = f.readlines()
	content = [line.strip() for line in content]
	return content

def write_file(filepath, content):
	if not os.path.exists(filepath):
		with open(filepath, 'w') as f:
			f.write(content)