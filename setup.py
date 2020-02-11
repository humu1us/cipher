import codecs
import os
import re
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*folders):
    with codecs.open(os.path.join(here, *folders), encoding='utf-8') as fd:
        return fd.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file,
                              re.M)
    if version_match:
        return version_match.group(1)

    raise RuntimeError("ERROR: version not found")


def get_requirements(file_name):
    requires_file = read('requirements', file_name)
    return requires_file.splitlines()


setup(
    name='humu1us-cipher',

    version=find_version('cipher', '__init__.py'),

    description='Encryption/decryption library',
    long_description=read('README.rst'),

    url='https://github.com/humu1us/cipher',

    author='Felipe Ortiz, Pablo Ahumada',
    author_email='fortizc@gmail.com, pablo.ahumadadiaz@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
    entry_points={'console_scripts': ['ciphercmd = cipher.cli.ciphercmd:main']}
)
