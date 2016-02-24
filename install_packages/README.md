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

**With installation package (.deb)**

**!!!WARNING 24.02.16!!!** The library libstdc++6 delete libre office core and all depending packages and could break your package dependencies on Debian. Please install EpiPy **From sources**. 

Requirements:

* [gcc-5-base](https://packages.debian.org/stretch/gcc-5-base)
* [libstdc++6](https://packages.debian.org/stretch/libstdc++6)
* [python-numpy](https://packages.debian.org/stretch/python-numpy)
* [python-scipy](https://packages.debian.org/stretch/python-scipy)

1. Install all needed packages.
2. Install `epipy-1.0_all.deb`

**From sources**

1. Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git`.
2. Install as *root*:
    * `$ apt-get install python-dev python-qt4 pkg-config libfreetype6-dev libatlas-base-dev gcc gfortran g++`
    * `$ pip install -r requirements.txt`
3. Navigate to `EpiPy/` and install as *root*: `$ pip install .`
4. EpiPy is now available in terminal: `$ epipy` .
