import os.path
import pytest

from my_custom_find.file_in_path_generator import *
from constants import TEST_DIRECTORY
from constants import FAKE_DIRECTORY


@pytest.mark.parametrize('directory_path',
                         [TEST_DIRECTORY])
def test_good_is_path_valid(directory_path):
    assert is_path_valid(directory_path)


@pytest.mark.parametrize('directory_path',
                         [FAKE_DIRECTORY])
def test_except_is_path_valid(directory_path):
    with pytest.raises(FileNotFoundError):
        is_path_valid(directory_path)


@pytest.mark.parametrize('directory_path',
                         [TEST_DIRECTORY])
def test_file_in_path_generator(directory_path):
    excepted_result = (os.path.abspath(os.path.join(directory_path, file))
                       for file in os.listdir(directory_path))
    for file in file_in_path_generator(directory_path):
        assert file in excepted_result
