#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from epipy import __version__, __author__, __author_email__, \
    __maintainer__, __maintainer_email__, __description__

try:
    from PyQt4.Qt import PYQT_VERSION_STR

    if int(PYQT_VERSION_STR.replace('.', '')) < 486:
        raise ImportError('''Expect PyQt4 4.8.6 or higher''')

except ImportError as error:
    raise ImportError(error)
    exit()

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='epipy',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    description=__description__,
    long_description='''EpiPy is a tool for fitting epidemic models.
    This tool is developed for the course Softwareprojekt Mobilkommunikation
    at the Freie Universität Berlin.

    Epidemics have been an interesting subject to study in many disciplines.
    Not only in epidemiology but also in biology, mathematics, sociology,
    computer science and more, the study of epidemics offers many areas for
    application. Mathematicians over time have suggested various models to
    understand and foresee the development of epidemics.

    Several tools are available that can simulate epidemics and generate
    data with given parameter for an epidemic model. However, there is yet
    no tool for easy fitting of epidemic models. EpiPy simplifies the
    fitting of various models to data and aims to help you understand
    different epidemics models. It offers a range of possibilities for you
    to explore.
    ''',
    keywords='epidemic',
    url='https://github.com/ckaus/EpiPy',
    packages=find_packages(exclude=['doc', 'datasets']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    license='MIT License',
    platforms='Linux',
    entry_points={'console_scripts': ['epipy = epipy.main:main', ], },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
)
