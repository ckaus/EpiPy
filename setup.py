#!/usr/bin/env python

import os

try:
    from setuptools import setup, find_packages
    import PyQt4
except ImportError as error:
    raise ImportError(error)


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="EpiPy",
    version="0.1",
    author="ckaus, malbert, yenarhee",
    description="A Tool for fitting epidemic models.",
    license="MIT",
    keywords="epidemic models",
    url="https://github.com/ckaus/EpiPy",
    packages=find_packages(exclude=["tests"]),
    package_data={"epipy": ["resources/data/*"]},
    long_description=read('README.md'),
    classifiers=[
        """\
Development Status :: 3 - Alpha
Environment :: Console
Environment :: GUI
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: MIT
Natural Language :: English
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Scientific/Engineering
Topic :: Tool
Operating System :: Unix
Operating System :: MacOS
"""
    ],
    entry_points={'console_scripts': ['epipy = epipy.main', ],},
)
