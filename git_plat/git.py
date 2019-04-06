import subprocess
from time import sleep


def pull(remote: str, branch: str, passphrase: str = None):
    remote_command(['git', 'pull', remote, branch], passphrase)


def clone(remote: str, path: str='', passphrase: str = None):
    remote_command(['git', 'clone', remote, path], passphrase)


def fetch(remote: str, passphrase: str = None):
    remote_command(['git', 'clone', remote], passphrase)


def init(remote: str):
    remote_command(['git', 'clone', remote])


def remote_command(command, passphrase):
    proc = subprocess.Popen(command)
    while proc.poll():
        sleep(.25)
        new_lines = proc.stdout.readlines()
        if len(filter(is_key_prompt, new_lines)) != 0:
            proc.communicate(passphrase)


def is_key_prompt(line :str):
    line.startswith('Enter passphrase for key')
