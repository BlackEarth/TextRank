config = {
  "name": "TextRank",
  "version": "0.1",
  "description": "",
  "url": "",
  "author": "",
  "author_email": "",
  "license": "LGPL 3.0",
  "classifiers": [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    "Programming Language :: Python :: 3"
  ],
  "entry_points": {},
  "install_requires": [],
  "extras_require": {
    "dev": [],
    "test": []
  },
  "package_data": {
    "": []
    },
  "data_files": [],
  "scripts": []
}

import os, json
from setuptools import setup, find_packages
from codecs import open

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, 'README.rst'), encoding='utf-8') as f:
    read_me = f.read()

setup(
    long_description=read_me,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    **config
)
