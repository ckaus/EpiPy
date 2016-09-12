# EpiPy

EpiPy is a tool for fitting epidemic models. This tool is developed for
the course [Softwareprojekt Mobilkommunikation](http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html)
at the [Freie Universität Berlin](http://www.fu-berlin.de/en/index.html).

## Introduction

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

## Features

* Fitting epidemic [data](http://userpage.fu-berlin.de/kies88/epipy/data/index.html)
* Plotting epidemic data and fitted epidemic model
* Manual and optimized manipulation epidemic model parameters
* Using different epidemic models:
* **S**usceptible **I**nfected **R**ecovered

  -  Simple, With births and deaths, With Vaccine
* **S**usceptible **I**nfected **R**ecovered **S**usceptible

  - Simple, With births and deaths
* **S**usceptible **E**xposed **I**nfected **R**ecovered

  - Simple
  
## Documentation

Take a look into our [wiki](https://github.com/ckaus/EpiPy/wiki) and / or generate the documentation with
[Sphinx](http://sphinx-doc.org/).

*  `$ cd EpiPy/doc/ && make html`

## Installation

###Windows

Requirements: [Python 2.7.11][1] , [NumPy][2] >= 1.10.4, [matplotlib][3] >= 1.5.1, [SciPy][4] >= 0.17.0,
[PyQt4][5] >= 4.11.4

[1]: https://www.python.org/downloads/release/python-2711/
[2]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
[3]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
[4]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
[5]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4

1. Install all required libraries with [Pip][6].
2. Install [EpiPy-0.0.1.win-amd64.msi][7].
3. EpiPy is now available in command line and `C:\Python27\Scripts\epipy.exe`.

[6]: https://pip.pypa.io/en/latest/installing/
[7]: http://userpage.fu-berlin.de/kies88/epipy/packages/EpiPy-0.0.1.win-amd64.msi

### Debian/Ubuntu

Requirements: Python 2.7, PyQt4 >= 4.11.2, NumPy >= 0.10.4, SciPy >= 0.17.0, matplotlib >= 1.4.2

1. Install:
  * [NumPy](https://packages.debian.org/stretch/python-numpy)
  * `$ sudo apt-get install python-dev python-pip libatlas-base-dev gcc gfortran g++`
2. Install Cython: `$ sudo pip install cython`
3. Clone SciPy 0.17: `$ git clone git@github.com:scipy/scipy.git -b maintenance/0.17.x`
4. Compile SciPy (will take some minutes):
  * `$ cd scipy && git clean -xdf`
  * `$ sudo python setup.py install`
5. Download and install: `$ wget http://userpage.fu-berlin.de/kies88/epipy/epipy_0.0.1-1_all.deb`
6. EpiPy is now available in menu and terminal: `$ epipy`

### Build from sources (Debian/Ubuntu)

Requirements: Python 2.7, PyQt4 >= 4.11.2, NumPy >= 0.10.4, SciPy >=
0.17.0, matplotlib >= 1.4.2, [EpiPylib](https://github.com/ckaus/epipylib) >= 0.1

1. Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git && cd EpiPy`
2. Build from sources: `$ python setup.py --command-packages=stdeb.command bdist_deb`
3. Install DEB-package: `$ cd deb_dist/ && sudo dpkg -i epipy_<version>_all.deb`

Screenshots
-----------

[Debian][8], [Windows][9]

[8]: http://userpage.fu-berlin.de/kies88/epipy/screenshots/screenshot_debian_xfce.png
[9]: http://userpage.fu-berlin.de/kies88/epipy/screenshots/screenshot_windows.png

License
-------

[MIT License](https://github.com/ckaus/EpiPy/blob/master/LICENSE)
