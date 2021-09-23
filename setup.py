from setuptools import setup, find_packages

setup(
    name='my_custom_find',
    version='1.0',
    packages=find_packages(),
    description='My custom find, test application',
    entry_points={
        'console_scripts':
            ['my_custom_find = my_custom_find.main:main']
    }
)