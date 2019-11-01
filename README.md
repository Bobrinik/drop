## Motivation

We cannot trust cloud providers but still want to use their services. We need to encrypt data that we are storing. The bottleneck in this setup should be the speed with which your data is encrypted with.

### Configuration
- Configuration file should be named `.dropconfig`.
- It should contain the fields bellow.
```
{
    "repository":"./repository",
    "devices": [
        {
            "name": "str",
            "input": "./data",
            "mount_point": "./mount"
        }
    ]
}

```
- `repository`: this field contains a path to where all of the assembled binary filesa are going to be stored.
- `name`: this field contains a name that is going to be used for assembled binary file.
- `input`: this field contains where split binary files are located.
- `mount_point`: this field contains a path to a folder on which the assemble and decrypted binary file is going to be mounted.

### Example usage
```
$ drop mount name_from_dropconfig
$ drop unmount name_from_dropconfig
```