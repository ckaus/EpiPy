#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
    from PyQt4 import QtCore

    if QtCore.QT_VERSION_STR < '4.8.6':
        raise ImportError('Expect PyQt4 4.8.6 or higher')

except ImportError as error:
    raise ImportError(error)

setup(
    name='EpiPy',
    version='0.0.1',
    url='https://github.com/ckaus/EpiPy',
    author='ckaus, mitalbert, yenarhee',
    author_email='christian.kaus@fu-berlin.de',
    description='A Tool for fitting epidemic models.',
    long_description='''
    EpiPy is a tool for fitting epidemic models. This tool is developed for the course Softwareprojekt
    Mobilkommunikation at the Freie Universität Berlin.

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
    license='MIT',
    packages=find_packages(exclude=['epipy/tests', 'epipy/resources/data']),
    include_package_data=True,
    install_requires=[
        'numpy>=1.10.4',
        'scipy>=0.17.0',
        'matplotlib>=1.4.2'
    ],
    entry_points={'console_scripts': ['epipy = epipy.main:main', ],},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows :: Windows 7',
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
