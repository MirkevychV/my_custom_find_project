import pytest

from my_custom_find.find_large_files import *
from constants import TEST_DIRECTORY


@pytest.mark.parametrize('user_size,excepted_result', [
    ('10B', 10),
    ('352M', 369098752.0),
    ('13G', 13958643712.0)
])
def test_good_convert_size(user_size, excepted_result):
    actual_result = convert_size_to_bytes(user_size)
    assert actual_result == excepted_result


@pytest.mark.parametrize('user_size',
                         ['10R', '52r55', 'qwerty'])
def test_exception_convert_size(user_size):
    with pytest.raises(ValueError):
        convert_size_to_bytes(user_size)


@pytest.mark.parametrize('path,size', [(TEST_DIRECTORY, 0)])
def test_large_files_generator(path, size, mocker):
    mocker.patch('my_custom_find.find_large_files.convert_size_to_bytes',
                 return_value=0)
    mocker.patch('os.path.getsize', return_value=10)
    for file in large_files_generator(path, size):
        assert os.path.basename(file) in os.listdir(path)
