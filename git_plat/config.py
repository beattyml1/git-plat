import os
import subprocess
from functools import reduce

import yaml

from git_plat import git
from git_plat.format_repo import format_repo


def pwd():
    return os.getcwd()


def load_config_file(path):
    file = open(path, 'r')
    config = yaml.load(file)
    return config


class Config:
    def __init__(self):
        self.config = {}

    def load(self, path='.git-plat.yaml'):
        self.config = load_config_file(path)

    @property
    def org(self):
        return self.config.get('org')

    @property
    def host(self):
        return self.config.get('host')

    @property
    def user(self):
        return self.config.get('user')

    @property
    def repos(self):
        items = self.config.get('repos')
        return map(lambda item: Repo(item[0], item[1], self), items)

    @property
    def repo_groups(self):
        items = self.config.get('repos-groups').items()
        return map(lambda item: RepoGroup(item[0], item[1], self), items)


class RepoConfig:
    def __init__(self, path, raw, parent: Config):
        self.parent = parent
        self.path = path
        if type(raw) == str:
            self.remote_config = {'origin': raw}
        elif type(raw) == dict:
            self.remote_config = raw

    @property
    def origin(self):
        return format_repo(self.remote_config['origin'])

    @property
    def remotes(self):
        return map(lambda item: {'name': item[0], 'uri': format_repo(item[1])}, self.remote_config.items())


class Repo(RepoConfig):
    def clone(self, passphrase):
        git.clone(self.origin, self.path, passphrase)

    def pull(self, remote, branch, passphrase):
        wd = pwd()
        subprocess.run(['cd', self.path])
        git.pull(self.origin, self.path, remote, branch, passphrase)
        subprocess.run(['cd', wd])

    def fetch(self, remote, passphrase):
        wd = pwd()
        subprocess.run(['cd', self.path])
        git.fetch(remote, passphrase)
        subprocess.run(['cd', wd])

    def init(self, passphrase):
        subprocess.run(['mkdir', self.path])
        wd = pwd()
        subprocess.run(['cd', self.path])
        git.init(passphrase)
        subprocess.run(['cd', wd])


class RepoGroup(RepoConfig, Config):
    def __init__(self, path, raw, parent):
        Repo.__init__(self, path, raw, parent)
        Config.__init__(self)

    @property
    def repo_folder(self):
        return self.config.get('root-repo-folder', 'root')

    @property
    def repo_path(self):
        return self.path + '/' + self.repo_folder


    def clone(self, passphrase):
        git.clone(self.origin, self.repo_path, passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        subprocess.run(['ls', '-s', '.git-plat.yaml', f'{self.repo_folder}/git-plat.yaml'])
        self.load()
        subprocess.run(['cd', wd])

    def pull(self, remote, branch, passphrase):
        wd = pwd()
        subprocess.run(['cd', self.path])
        self.load()
        git.pull(remote, branch, passphrase)
        subprocess.run(['cd', wd])

    def fetch(self, remote, passphrase):
        wd = pwd()
        subprocess.run(['cd', self.path])
        self.load()
        git.fetch(remote, passphrase)
        subprocess.run(['cd', wd])

    def init(self, passphrase):
        subprocess.run(['mkdir', self.path])
        subprocess.run(['mkdir', self.repo_path])
        wd = pwd()
        subprocess.run(['cd', self.repo_path])
        git.init(passphrase)
        # todo: write default config
        subprocess.run(['cd', wd])
        subprocess.run(['cd', self.path])
        subprocess.run(['ls', '-s', '.git-plat.yaml', f'root/git-plat.yaml'])
        subprocess.run(['cd', wd])

    def clone_children(self, passphrase):
        self.clone(passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        for repo in self.repos:
            repo.clone(passphrase)
        for repo in self.repo_groups:
            repo.clone(passphrase)
        subprocess.run(['cd', wd])

    def clone_descendants(self, passphrase):
        self.clone(passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        for repo in self.repos:
            repo.clone(passphrase)
        for repo in self.repo_groups:
            repo.clone_descendants(passphrase)
        subprocess.run(['cd', wd])

    def fetch_children(self, remote, passphrase):
        self.fetch(remote, passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        for repo in self.repos:
            repo.fetch(remote, passphrase)
        for repo in self.repo_groups:
            repo.fetch(remote, passphrase)
        subprocess.run(['cd', wd])

    def fetch_descendants(self, remote, passphrase):
        self.fetch(remote, passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        for repo in self.repos:
            repo.fetch(remote, passphrase)
        for repo in self.repo_groups:
            repo.fetch_descendants(remote, passphrase)
        subprocess.run(['cd', wd])

    def pull_children(self, remote, branch, passphrase):
        self.pull(remote, branch, passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        for repo in self.repos:
            repo.pull(remote, branch, passphrase)
        for repo in self.repo_groups:
            repo.pull(remote, branch, passphrase)
        subprocess.run(['cd', wd])

    def pull_descendants(self, remote, branch, passphrase):
        self.pull(remote, passphrase)
        wd = pwd()
        subprocess.run(['cd', self.path])
        for repo in self.repos:
            repo.pull(remote, branch, passphrase)
        for repo in self.repo_groups:
            repo.pull_descendants(remote, branch, passphrase)
        subprocess.run(['cd', wd])