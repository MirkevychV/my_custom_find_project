import os


def file_in_path_generator(directory_path):
    """
    Generates a full path to a file in directory(path)
    """
    if is_path_valid(directory_path):  # Check if path exists
        for file in os.listdir(directory_path):
            # Build full link to a file
            file_path = os.path.abspath(os.path.join(directory_path, file))
            if os.path.isfile(file_path):
                yield file_path


def is_path_valid(directory_path):
    """
    Checks if the path is valid
    """
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(directory_path)
    return True
