import hashlib
from collections import defaultdict

from my_custom_find.file_in_path_generator import file_in_path_generator

BLOCK_SIZE = 65536


def duplicate_files_generator(path):
    for file in find_duplicate_files(path):
        yield file


def get_hash(file):
    """
    Gets a 'SHA256' hash-code of a file
    """
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        file_buffer = f.read(BLOCK_SIZE)
        while len(file_buffer) > 0:
            file_hash.update(file_buffer)
            file_buffer = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()


def find_duplicate_files(directory_path):
    """
    Finds a duplicates files in directory using their hash-code.
    Returns a list of links to the duplicate files
    """
    files_dict = defaultdict(list)
    for file in file_in_path_generator(directory_path):
        file_hash = get_hash(file)
        files_dict[file_hash].append(file)
    return get_duplicate_files(files_dict)


def get_duplicate_files(files_dict):
    """
    Unpacks dict of duplicate files to one list, and then returns
    iterator object of its files
    """
    if any(files_dict):
        duplicate_files_list = []
        for hash_code, files_list in files_dict.items():
            # If 1 hash-code has more than 1 file its a duplicate
            if len(files_list) > 1:
                duplicate_files_list.extend(files_list)
        return iter(duplicate_files_list)
