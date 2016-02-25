#!/usr/bin/env python

import os

try:
    from setuptools import setup, find_packages
except ImportError as error:
    raise ImportError(error)


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='EpiPy',
    version='0.0.1',
    url='https://github.com/ckaus/EpiPy',
    author='ckaus, mitalbert, yenarhee',
    author_email='christian.kaus@fu-berlin.de',
    description=('A Tool for fitting epidemic models.'),
    long_description=read('README.rst'),
    license='MIT',
    packages=find_packages(exclude=['tests', 'install_packages']),
    package_data={'epipy': ['ui/view/*.ui']},
    include_package_data=True,
    install_requires=[
        'PyQt4>=4.8.6',
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