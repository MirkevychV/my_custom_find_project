import os
import re

from file_in_path_generator import file_in_path_generator


def large_files_generator(path, size):
    """
    Returns files in path:'path' which are bigger that value:'size'
    """
    bytes_size = convert_size_to_bytes(size)
    for file in file_in_path_generator(path):
        if os.path.getsize(file) >= bytes_size:
            yield file


def convert_size_to_bytes(user_size):
    """
    Converts user-input size to bytes
    """
    size = size_split(user_size)
    try:
        if size[1] == 'B':
            return float(size[0])
        elif size[1] == 'M':
            return float(size[0]) * 1048576
        elif size[1] == 'G':
            return float(size[0]) * 1073741824
        raise ValueError
    except ValueError:
        print('Invalid format of size')
        exit()  # Close a program, because input-value is invalid


def size_split(user_size):
    """
    Makes user-input size-value understandable for program. Splits
    user_size to a tuple with 2 values: (value, units of measurement)
    """
    size_with_dimension = re.split(r'(\d+)', user_size)
    # Delete a first value, because it's empty(side effect of the re.split)
    return tuple(size_with_dimension[1:3])
