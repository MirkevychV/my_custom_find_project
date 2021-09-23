import os
import time

from file_in_path_generator import file_in_path_generator


def old_file_generator(path):
    one_epoch_year = 31556926  # One year in seconds

    for file in file_in_path_generator(path):
        if time.time() - os.path.getctime(file) >= one_epoch_year:
            yield file
