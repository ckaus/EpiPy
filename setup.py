#!/usr/bin/env python

import os
import sys

try:
	from setuptools import setup, find_packages
except ImportError:
	raise ImportError("Install setup tools")

try:
	import PyQt4
except ImportError:
	raise ImportError("Install PyQt4")

try:
	import numpy as np
except ImportError:
	raise ImportError("Install Numpy")

try:
	import matplotlib
except ImportError:
	raise ImportError("Install matplotlib")

try:
	import scipy
except ImportError:
	raise ImportError("Install scipy")

if sys.version_info[:2] > (2, 7):
	raise RuntimeError("Python version 2.6, 2.7 required.")


def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
		name="EpiPy",
		version="0.1",
		author="ckaus",
		description="A Tool for fitting epidemic models.",
		license="MIT",
		keywords="epidemic models",
		url="https://github.com/ckaus/EpiPy",
		packages=find_packages(exclude=["tests"]),
		package_data={"epipy": ["ui/*", "resources/data/*", "resources/pictures/*"]},
		long_description=read('README.md'),
		install_requires=['pyqtgraph'],
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
