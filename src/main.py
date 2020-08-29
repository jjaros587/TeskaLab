import click
from src import commands


@click.group()
def main():
    pass


@main.command()
@click.argument('filename')
def save(filename):
    commands.save(filename)


@main.command()
def get():
    commands.get()


@main.command()
def delete():
    commands.delete()


if __name__ == '__main__':
    main()
