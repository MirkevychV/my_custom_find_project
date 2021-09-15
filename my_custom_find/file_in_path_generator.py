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
    else:
        return


def is_path_valid(directory_path):
    """
    Checks if the path is valid
    """
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError
        else:
            return True
    except FileNotFoundError:
        print(f'Path "{directory_path}" is not valid')
        exit()  # Close a program, because input-value is invalid
