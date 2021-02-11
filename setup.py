from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'pfdo_mgz2img',
    version          = '1.0.0',
    description      = 'An app to recursively walk down a directory tree and perform a mgz2imgslices on files in each directory. \
                        (optionally filtered by some simple expression)',
    long_description = readme,
    author           = 'Arushi Vyas',
    author_email     = 'dev@babyMRI.org',
    url              = 'https://github.com/FNNDSC/pl-pfdo_mgz2img',
    packages         = ['pfdo_mgz2img'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'pfdo_mgz2img = pfdo_mgz2img.__main__:main'
            ]
        }
)
