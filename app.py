import click
import json
from mimetypes import guess_type
import subprocess
from os import listdir, remove
from os.path import isfile, join, isdir, exists
from typing import List
import re

configs = None


def validate_config(config):
    names = set()
    inputs = set()
    repo = configs['repo']
    if not exists(repo):
        raise ValueError(f'{repo} does not exist')

    for device in config['devices']:
        name = device['name']
        input_ = device['input']
        output = device['output']

        if name in names:
            raise ValueError('Duplicate names are not allowed!')

        if input_ in inputs:
            raise ValueError('Duplicate input paths are not allowed!')

        if not exists(input_):
            raise ValueError(f'{input_} does not exist!')

        if not exists(output):
            raise ValueError(f'{output} does not exist!')

        names.add(name)
        inputs.add(input_)


def load_configs():
    '''
    This command looks for .dropconfig file
    in the directory if it does not find it
    it will throw an error else it will silently load it and other
    programs can use it in the background.
    '''
    files = [file for file in listdir('.') if isfile(
        file) and file == '.dropconfig']

    if len(files) == 0:
        raise ValueError(".dropconfig is not found in the current directory")
    elif len(files) > 1:
        raise ValueError("you have more than one .dropconfig file")

    with open(files[0]) as f:
        config = json.load(f)
        validate_config(config)
        return config


def get_configuration(config, name):
    for device in config['devices']:
        if device['name'] == name:
            return device
    raise ValueError('Device does not exist in .dropconfig')


def run_command(command: List[str]):
    result = subprocess.run(command, capture_output=True)
    print(result)
    if result.returncode:
        raise ValueError(f'Command {command[0]} failed to run!')


@click.command()
@click.option('--name', help='Enter name of the device.')
@click.option('--mount', help='Enter path to mount device on.')
def mount(name, mount):
    config = get_configuration(configs, name)
    in_path, mount_point = config['input'], config['mount_point']
    # We are going to store assebled images in the repository
    repo = configs['repository']
    # need to check that the repository exists b4 going further
    # need to check that the input exists b4 going further
    # sort the files by name and then concatenate them together
    files = sorted([join(in_path, file) for file in listdir(in_path)])

    if any(map(isdir, files)):
        raise TypeError(f'{in_path} should not contain directories!')

    repo_path = join(repo, name)

    if exists(repo_path):
        print(f'Removing a file!')
        remove(repo_path)

    with open(repo_path, 'ab') as f:
        for file in files:
            with open(file, 'rb') as fp:
                f.write(fp.read())

    # Here name is going to be a name use in /dev/mapper/name
    run_command(['cryptsetup', 'luksOpen', repo_path, str(name)])
    run_command(['mount', str(mount_point), str(name)])


@click.command()
@click.option('--name', help='Enter name of the device.')
@click.option('--umount', help='Enter path to mount device on.')
def umount(name, mount):
    # TODO: Figure out how to use two functions for different flags
    # we are going to unmount
    # we are going to close luks device
    # we are going to clean the destination
    # we are going to partition file
    # we are going to archive old version
    # we are going to save it
    pass


if __name__ == "__main__":
    configs = load_configs()
    mount()
