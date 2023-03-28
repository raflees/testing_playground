import click
import os.path

import testing.number_functions as nf
import testing.file_functions as ff

@click.group()
def cli():
    pass

def _invert_file_content(filepath):
    content = ff.read_file(filepath)
    inv_content = ''.join(ff.invert_text(content))
    
    new_filename = ff.get_inverted_filename(filepath)

    ff.write_file(new_filename, inv_content)

@cli.command()
@click.argument('filepath', type=str)
def invert_file_content(filepath):
    return _invert_file_content(filepath)


@cli.command()
@click.argument('number', type=int)
def is_even(number):
    if nf.is_even(number):
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")
    return