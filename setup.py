import codecs
import os
import re
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*folders):
    with codecs.open(os.path.join(here, *folders), encoding='utf-8') as f:
        return f.read()


def find_version():
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_file = read('cipher', '__init__.py')
    version_match = re.search(VSRE, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("ERROR: version not found")


def get_requirements(file_name):
    requires_file = read('requirements', file_name)
    return requires_file.splitlines()


setup(
    name='cipher',

    version=find_version(),

    description='encryption/decryption tools',
    long_description=read('README.rst'),

    url='https://github.com/humu1us/cipher',

    author='Pablo Ahumada, Felipe Ortiz',
    author_email='pablo.ahumadadiaz@gmail.com, fortizc@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: System',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='encrypt decrypt secrets credentials',
    packages=find_packages(exclude=['test']),
    install_requires=get_requirements('default.txt'),
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    test_suite='test',
    setup_requires=get_requirements('test.txt'),
)
