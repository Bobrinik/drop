import sys
sys.path.append('../')  # noqa E402

from pytest import raises
from drop import load_configs, validate_config


def test_config_file():
    configs = load_configs()
    assert configs == {
        'repository': './test_data/repository',
        'devices': [
            {
                'name': 'storage_name',
                'input': './test_data/data',
                'mount_point': './test_data/mount'
            }
        ]
    }


def test_duplicate_names():
    configs_1 = {
        'repository': './test_data/repository',
        'devices': [
            {
                'name': 'storage_name',
                'input': '/path/to/folder/with/binary/files',
                'mount_point': '/path/to/concatenated/file'
            },
            {
                'name': 'storage_name',
                'input': '/path/to/folder/with/binary/files',
                'mount_point': '/path/to/concatenated/file'
            }
        ]
    }

    configs_2 = {
        'repository': './test_data/repository',
        'devices': [
            {
                'name': 'storage_name_1',
                'input': '/path/to/folder/with/binary/files',
                'mount_point': '/path/to/concatenated/file'
            },
            {
                'name': 'storage_name_2',
                'input': '/path/to/folder/with/binary/files',
                'mount_point': '/path/to/concatenated/file'
            }
        ]
    }

    with raises(ValueError):
        validate_config(configs_1)

    with raises(ValueError):
        validate_config(configs_2)
