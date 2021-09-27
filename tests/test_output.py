import pytest
import os

from my_custom_find.output import *
from constants import TEST_DIRECTORY
from constants import FAKE_DIRECTORY
from constants import EXCEPTED_LOG_FILES


@pytest.mark.parametrize('command,log_file', [
    ('duplicate_files_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[0]}'),
    ('large_files_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[1]}'),
    ('images_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[2]}'),
    ('old_file_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[3]}')
])
def test_good_write_to_file(command, log_file, mocker):
    mocker.patch('my_custom_find.output.work_info', return_value=command)
    write_to_file(command, log_file)
    assert os.path.basename(log_file) in os.listdir(TEST_DIRECTORY)


@pytest.mark.parametrize('command,log_file', [
    ('duplicate_files_generator', f'{FAKE_DIRECTORY}{EXCEPTED_LOG_FILES[0]}'),
    ('large_files_generator', f'{FAKE_DIRECTORY}{EXCEPTED_LOG_FILES[1]}'),
    ('images_generator', f'{FAKE_DIRECTORY}{EXCEPTED_LOG_FILES[2]}'),
    ('old_file_generator', f'{FAKE_DIRECTORY}{EXCEPTED_LOG_FILES[3]}')
])
def test_exception_write_to_file(mocker, command, log_file):
    mocker.patch('my_custom_find.output.work_info', return_value=command)
    with pytest.raises(IOError):
        write_to_file(command, log_file)


@pytest.mark.parametrize('command', [
    'duplicate_files_generator',
    'large_files_generator',
    'images_generator',
    'old_file_generator'
])
def test_output_to_console(command, capfd, mocker):
    mocker.patch('my_custom_find.output.work_info', return_value='some text')
    output(command)
    out, err = capfd.readouterr()
    assert out


@pytest.mark.parametrize('command,log_file', [
    ('duplicate_files_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[0]}'),
    ('large_files_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[1]}'),
    ('images_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[2]}'),
    ('old_file_generator', f'{TEST_DIRECTORY}{EXCEPTED_LOG_FILES[3]}')
])
def test_output_to_file(command, log_file, capfd, mocker):
    mocker.patch('my_custom_find.output.write_to_file')
    output(command, log_file)
    out, err = capfd.readouterr()
    assert not out


@pytest.mark.parametrize('text_iter', [
    '<Test text1>',
    '<Test text2>',
    '<Test text3>',
    '<Test text4>'
])
def test_exception_work_info(text_iter):
    with pytest.raises(IndexError):
        work_info(text_iter)
