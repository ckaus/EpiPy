# Installation

## Windows

Requirements:

* [Python 2.7.11](https://www.python.org/downloads/release/python-2711/)
* [matplotlib-1.5.1-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib)
* [numpy-1.10.4+mkl-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
* [scipy-0.17.0-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)
* [PyQt4-4.11.4-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)

1. Install all needed libraries with Pip.
2. Install `EpiPy-1.0.win-amd64.msi`
3. EpiPy is now available in `C:\Python27\Scripts\`.

## Debian/Ubuntu
Requirements: Python 2.7, PyQt4 >= 4.11.2, NumPy >= 0.10.4, SciPy >= 0.17.0, matplotlib >= 1.4.2

1. Install needed libraries as *root*:
 * `apt-get install python python-dev python-qt4 python-pip libatlas-base-dev gcc gfortran g++`
 * `pip install cython`
2. Install SciPy from sources: 
 * `git clone https://github.com/scipy/scipy.git`
 * `cd scipy`, `git clean -xdf`, as *root*: `python setup.py install` (take a while)
3. Install EpiPy as *root*:
 * With .deb package: `epipy-1.0_all.deb` *or*
 * With [PyPi](http://pypi.python.org/pypi/epipy_fub): `$ pip install epipy_fub`
4. EpiPy is now available in terminal: `$ epipy`


