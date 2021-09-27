import pytest

from my_custom_find.main import *


def test_exception_main():
    with pytest.raises(TypeError):
        main()
