import click

@click.group()
def cli():
    pass


@cli.group(name='clone')
def clone_group():
    pass


@cli.group(name='fetch')
def fetch_group():
    pass


@cli.group(name='pull')
def pull_group():
    pass

@cli.group(name='init')
def init_group():
    pass