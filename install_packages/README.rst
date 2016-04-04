Installation
============

Windows
-------

Requirements:

-  `Python 2.7.11 <https://www.python.org/downloads/release/python-2711/>`__
-  `numpy-1.10.4+mkl-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`__
-  `matplotlib-1.5.1-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib>`__
-  `scipy-0.17.0-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy>`__
-  `PyQt4-4.11.4-cp27-none-win\_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4>`__

1. Install all needed libraries in list order with Pip.
2. Install ``EpiPy-0.0.1.win-amd64.msi``
3. EpiPy is now available in command line and ``C:\Python27\Scripts\epipy.exe``.

Debian/Ubuntu
-------------

Requirements: Python 2.7, PyQt4 >= 4.11.2, NumPy >= 0.10.4, SciPy >=
0.17.0, matplotlib >= 1.4.2

Note: Make sure you haven't installed ``python-scipy`` before. The official stable package ``python-scipy`` for Debian Jessie is 0.14.0-2. EpiPy need SciPy 0.17.0 or higher!

1. Install:

   - `NumPy <https://packages.debian.org/stretch/python-numpy>`__
   - ``sudo apt-get install python-dev python-pip libatlas-base-dev gcc gfortran g++``

2. Install: ``sudo pip install cython``
3. Clone SciPy: ``git clone https://github.com/scipy/scipy.git``
4. Compile SciPy (will take some minutes):

   -  ``cd scipy``
   -  ``git clean -xdf``
   -  ``sudo python setup.py install``

5. Download and install: ``wget https://github.com/ckaus/EpiPy/blob/master/install_packages/epipy_0.0.1-1_all.deb`` or 
   optional build from source - Requirements: stdeb >=0.8.5

   -  Navigate to main folder ``EpiPy/`` 
   -  Execute: ``python setup.py --command-packages=stdeb.command bdist_deb``
   -  DEB-package is now available in ``EpiPy/deb_dist`` 

6. EpiPy is now available in menu and terminal: ``$ epipy``

