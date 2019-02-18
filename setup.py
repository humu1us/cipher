import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*folders):
    with codecs.open(os.path.join(here, *folders), encoding='utf-8') as fd:
        return fd.read()


def find_version():
    with open("VERSION", "r") as fd:
        return fd.read().rstrip()


def get_requirements(file_name):
    requires_file = read('requirements', file_name)
    return requires_file.splitlines()


long_description = read('README.rst')

setup(
    name='govision-cipher',

    version=find_version(),

    description='Encryption/decryption library',
    long_description=long_description,

    url='https://bitbucket.org/govisioncl/cipher',

    author='Felipe Ortiz',
    author_email='fortizc@gmail.com',

    license='',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='AES encryption decryption',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=get_requirements('default.txt'),
    setup_requires=get_requirements('test.txt'),
    test_suite='test',
    extras_require={},
    package_data={},
    data_files=[],
)
