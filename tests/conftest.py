import pytest

from constants import TEST_DIRECTORY
from constants import IMAGE_FILES
from constants import DUPLICATE_FILES
from constants import ANOTHER_FILES


def create_duplicates():
    """
    Creates duplicates files in test directory
    """
    for file in DUPLICATE_FILES:
        with open(TEST_DIRECTORY + file, 'w') as f:
            f.write('test')


def create_images():
    """
    Creates images in test directory
    """
    for file in IMAGE_FILES:
        with open(TEST_DIRECTORY + file, 'w'):
            pass


def create_another_files():
    """
    Creates testing files in test directory
    """
    counter = 0
    for file in ANOTHER_FILES:
        with open(TEST_DIRECTORY + file, 'w') as f:
            f.write(f'Another test file {str(counter)}')
        counter += 1


@pytest.fixture(scope="session", autouse=True)
def make_test_directory():
    """
    Creates all files for tests in test directory and after tests
    deletes them
    """
    create_duplicates()
    create_images()
    create_another_files()
