import hashlib

from file_in_path_generator import file_in_path_generator


def duplicate_files_generator(path):
    for file in find_duplicate_files(path):
        yield file


def get_hash(file):
    """
    Gets a MD5 hash-code of a file
    """
    with open(file, 'rb') as file:
        hasher = hashlib.md5()
        buf = file.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(65536)
    return hasher.hexdigest()


def find_duplicate_files(directory_path):
    """
    Finds a duplicates files in directory using their hash-code.
    Returns a list of links to the duplicate files
    """
    files_dict = dict()
    for file in file_in_path_generator(directory_path):
        file_hash = get_hash(file)
        if file_hash in files_dict:
            # Append all duplicate files to theirs hash-code-keys
            files_dict[file_hash].append(file)
        else:
            files_dict[file_hash] = [file]
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
                for files in files_list:
                    duplicate_files_list.append(files)
        return iter(duplicate_files_list)
    else:
        return
