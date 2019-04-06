import git_plat.git
import click

@click.group()
def cli():
    pass


@cli.command(name='fetch')
@click.option('-w', '--with', default='children', type=click.Choice(['children', 'descendents', 'self']), help='which repos to fetch')
@click.argument('remote', nargs=1)
def fetch(with_, remote):
    print('command: clone')
    print(f'commands: {with_}')
    print(f'remote: {remote}')



@cli.command(name='pull')
@click.option('-w', '--with', default='children', type=click.Choice(['children', 'descendents', 'self']), help='which repos to pull')
@click.argument('remote', nargs=1)
@click.argument('branch', nargs=1)
def pull(with_, remote, branch):
    print('command: clone')
    print(f'commands: {with_}')
    print(f'remote: {remote}')
    print(f'branch: {branch}')


@cli.command(name='init')
def init():
    print('command: init')
    print(f'commands: {with_}')
    print(f'repo: {repo}')


@cli.command('clone')
@click.option('-w', '--with', default='', type=click.Choice(['children', 'descendents', 'self']), help='which repos to clone')
@click.argument('repo', nargs=1)
def clone(with_, repo):
    print('command: clone')
    print(f'commands: {with_}')
    print(f'repo: {repo}')

