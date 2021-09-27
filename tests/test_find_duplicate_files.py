import os
import pytest

from my_custom_find.find_duplicate_files import *
from constants import TEST_DIRECTORY
from constants import DUPLICATE_FILES


@pytest.mark.parametrize('path', [TEST_DIRECTORY])
def test_duplicate_files_gen(path, mocker):
    mocker.patch('my_custom_find.find_duplicate_files.find_duplicate_files',
                 return_value=DUPLICATE_FILES)
    for file in duplicate_files_generator(path):
        assert os.path.basename(file) in os.listdir(path)


@pytest.mark.parametrize('files_dict', [
    {'123test_hash': ['test_duplicate1_1.txt',
                      'test_duplicate1_2.txt',
                      'test_duplicate1_3.txt',
                      'test_duplicate1_4.txt'],
     '123another_hash': ['another_file.txt']
     }
])
def test_get_duplicate_files(files_dict):
    for file in get_duplicate_files(files_dict):
        assert os.path.basename(file) in DUPLICATE_FILES


@pytest.mark.parametrize('directory_path', [
    TEST_DIRECTORY
])
def test_find_duplicate_files(directory_path, mocker):
    mocker.patch('my_custom_find.find_duplicate_files.get_hash',
                 return_value='test_hash')
    mocker.patch(
        'my_custom_find.file_in_path_generator.file_in_path_generator'
    )
    for file in find_duplicate_files(directory_path):
        assert os.path.basename(file) in os.listdir(TEST_DIRECTORY)
