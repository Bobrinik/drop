## Motivation

We cannot trust cloud providers but still want to use their services. We need to encrypt data that we are storing. The bottleneck in this setup should be the speed with which your data is encrypted with.

### Examples
```
## Configuation file

{
    "devices": [
        {
            "name": "storage_name",
            "input": "/path/to/folder/with/binary/files",
            "outptut": "/path/to/concatenated/file"
        }
    ]
}

```

```
$ drop mount storage_name /folder/to/mount
$ drop unmount storage_name /folder/to/unmount
```

### Specification
- name: This flag is going to select a configuration from the device file
- mount: This command is going to concatenate all of the files in the input path and save the result in the output path using the `name` as a file name and will mount the file onto the folder passed into `mount` flag.
- umount: This command is going to unmount a folder break the file with `name` in it's output folder and store the resullts in the input folder after removing the files in the folder.