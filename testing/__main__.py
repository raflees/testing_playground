import click

import number_functions as nf

@click.group()
def cli():
    pass

@cli.command()
@click.argument('number', type=int)
def is_even(number):
    if nf.is_even(number):
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")
    return

if __name__ == '__main__':
    cli()