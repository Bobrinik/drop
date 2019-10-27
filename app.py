import click
import json
from os import listdir
from os.path import isfile, join

def validate_config(config):
    names = set()
    inputs = set()
    for device in config['devices']:
        name = device['name']
        input_ = device['input']

        if name in names:
            raise ValueError('Duplicate names are not allowed!')

        if input_ in inputs:
            raise ValueError('Duplicate input paths are not allowed!')
        
        names.add(name)
        inputs.add(input_)


def load_configs():
    '''
    This comman looks for 
    .dropconfig file in the directory if it does not find it
    it will throw an error else it will silently load it and other
    programs can use it in the background.
    '''
    files = [file for file in listdir('.') if isfile(file) and file == '.dropconfig']

    if len(files) == 0:
        raise ValueError(".dropconfig is not found in the current directory")
    elif len(files) > 1:
        raise ValueError("you have more than one .dropconfig file")

    with open(files[0]) as f:
        config = json.load(f)
        validate_config(config)
        return config


if __name__ == "__main__":
    configs=load_configs()
