#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = find_version("", "__init__.py")

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

package_data = {
}

requires = []

extras_require = {}

tests_requires = [
    'pytest',
]

classifiers = [
    'Development Status:: 2 - Pre - Alpha',
    'Intended Audience :: Developers',
    'License :: Other/Proprietary License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='sb_nmt',
    version=version,
    description='Saddleback Neural Machine Translation',
    long_description=readme,
    packages=find_packages(),
    package_data=package_data,
    install_requires=requires,
    author='Samuel Tin',
    author_email='samuel.tin@gmail.com',
    license='Proprietary',
    classifiers=classifiers,
    setup_requires=['pytest-runner'],
    tests_require=tests_requires,
    extras_require=extras_require,
    include_package_data=True
)
