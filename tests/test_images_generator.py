import pytest
import os

from my_custom_find.images_generator import *

from constants import IMAGE_FILES
from constants import TEST_DIRECTORY


@pytest.mark.parametrize('path, excepted_result', [
    (TEST_DIRECTORY, IMAGE_FILES)
])
def test_good_image_generator(path, excepted_result):
    for file in images_generator(path):
        assert os.path.basename(file) in excepted_result
