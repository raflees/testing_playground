import click
import os.path

import testing.number_functions as nf
import testing.file_functions as ff

@click.group()
def cli():
    pass


@cli.command()
@click.argument('filepath', type=str)
def invert_file_content(filepath):
    # This makes this function more easily testable outside of the click command
    return ff.invert_file_content(filepath)


@cli.command()
@click.argument('number', type=int)
def is_even(number):
    if nf.is_even(number):
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")
    return