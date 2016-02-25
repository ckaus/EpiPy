Installation
============

Windows
-------

Requirements:

-  `Python 2.7.11 <https://www.python.org/downloads/release/python-2711/>`__
-  `matplotlib-1.5.1-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib>`__
-  `numpy-1.10.4+mkl-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`__
-  `scipy-0.17.0-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy>`__
-  `PyQt4-4.11.4-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4>`__

1. Install all needed libraries with Pip.
2. Install ``EpiPy-1.0.win-amd64.msi``
3. EpiPy is now available in ``C:\Python27\Scripts\``.

Debian/Ubuntu
-------------

Requirements: Python 2.7, PyQt4 >= 4.11.2, NumPy >= 0.10.4, SciPy >=
0.17.0, matplotlib >= 1.4.2

1. Install as *root*:

   - `Numpy <https://packages.debian.org/stretch/python-numpy>`__
   - ``apt-get install python-dev python-qt4 python-matplotlib python-pip libatlas-base-dev gcc gfortran g++``

2. Install as *root*: ``pip install cython``
3. Clone SciPy: ``git clone https://github.com/scipy/scipy.git``
4. Compile SciPy (will take some time):

   -  ``cd scipy``
   -  ``git clean -xdf``
   -  As *root*: ``python setup.py install``

5. Download ``epipy-1.0_all.deb`` and install *root*: ``apt-get install epipy-1.0_all.deb``
6. EpiPy is now available in terminal: ``$ epipy``

