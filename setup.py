import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "EpiPy",
    version = "0.1",
    author = "ckaus",
    description = ("A Tool for fitting epidemic models."),
    license = "MIT",
    keywords = "epidemic models",
    url = "",
    packages=['src', 'resources',
            'src.utils', 'src.model', 'src.ui'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: GUI",
        "Intended Audience :: Scientists",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Debian",
        "Programming Language :: Python",
        "Topic :: Tool",
        "License :: MIT",
    ],
    entry_points = {'console_scripts': ['epipy = src.test',],},
)
