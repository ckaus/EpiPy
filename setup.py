import os
from setuptools import setup, find_packages

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
    packages=find_packages(exclude=["tests"]),
    # add all non python files
    package_data={'epipy': ['ui/*','resources/data/*','resources/pictures/*']},
    long_description=read('README'),
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
    entry_points = {'console_scripts': ['epipy = epipy.main',],},
)
