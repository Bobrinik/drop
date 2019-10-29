from os import listdir
from app import load_configs, validate_config
import sys
from pytest import raises
sys.path.append('../')


def test_config_file():
    configs = load_configs()
    assert configs == {
        'devices': [
            {
                'name': 'storage_name',
                'input': '/path/to/folder/with/binary/files',
                'outptut': '/path/to/concatenated/file'
            }
        ]
    }


def test_duplicate_names():
    configs_1 = {
        'devices': [
            {
                'name': 'storage_name',
                'input': '/path/to/folder/with/binary/files'
            },
            {
                'name': 'storage_name',
                'input': '/path/to/folder/with/binary/files',
            }
        ]
    }

    configs_2 = {
        'devices': [
            {
                'name': 'storage_name_1',
                'input': '/path/to/folder/with/binary/files'
            },
            {
                'name': 'storage_name_2',
                'input': '/path/to/folder/with/binary/files',
            }
        ]
    }

    with raises(ValueError):
        validate_config(configs_1)

    with raises(ValueError):
        validate_config(configs_2)
