import pytest

from my_custom_find.old_file_generator import *
from constants import TEST_DIRECTORY


@pytest.mark.parametrize('path,file_time', [
    (TEST_DIRECTORY, 32556926)
])
def test_good_old_file_generator(path, file_time, mocker):
    mocker.patch('os.path.getctime', return_value=file_time)
    for file in old_file_generator(path):
        assert os.path.basename(file) in os.listdir(path)
