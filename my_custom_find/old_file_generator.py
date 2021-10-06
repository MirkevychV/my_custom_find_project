import os
import time

from my_custom_find.file_in_path_generator import file_in_path_generator

one_epoch_year = 31556926  # One year in seconds


def old_file_generator(path):
    """
    Finds files older than 1 year
    """
    for file in file_in_path_generator(path):
        if time.time() - os.path.getctime(file) >= one_epoch_year:
            yield file
