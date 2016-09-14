# EpiPy

EpiPy is a tool for fitting epidemic models. This tool is developed for
the course [Softwareprojekt Mobilkommunikation](http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html)
at the [Freie Universität Berlin](http://www.fu-berlin.de/en/index.html).

## Table Of Contents:

[1. Features](https://github.com/ckaus/EpiPy#features)

[2. Installation](https://github.com/ckaus/EpiPy#installation)

  [2.1. Windows](https://github.com/ckaus/EpiPy#windows)

  [2.2 Debian/Ubuntu](https://github.com/ckaus/EpiPy#debianubuntu)

  [2.3 Build From Sources (Debian/Ubuntu)](https://github.com/ckaus/EpiPy#build-from-sources-debianubuntu)

[3. Documentation](https://github.com/ckaus/EpiPy#documentation)

[4. Data Sets](https://github.com/ckaus/EpiPy#data-sets)

  [4.1 Generated Data Sets](https://github.com/ckaus/EpiPy#generated-data-sets)

  [4.2. Real Data Sets](https://github.com/ckaus/EpiPy#real-data-sets)

[5. License](https://github.com/ckaus/EpiPy#license)

## Features

* Fitting epidemic data
* Plotting epidemic data and fitted epidemic model
* Manual and optimized manipulation epidemic model parameters
* Using different epidemic models:
  * **S**usceptible **I**nfected **R**ecovered (Simple, With births and deaths, With Vaccine)
  * **S**usceptible **I**nfected **R**ecovered **S**usceptible (Simple, With births and deaths)
  * **S**usceptible **E**xposed **I**nfected **R**ecovered (Simple)

## Installation

### Windows

Requirements: [Python 2.7.11][1] , [NumPy][2] >= 1.10.4, [matplotlib][3] >= 1.5.1, [SciPy][4] >= 0.17.0, [PyQt4][5] >= 4.11.4

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

### Build From Sources (Debian/Ubuntu)

Requirements: Python 2.7, PyQt4 >= 4.11.2, NumPy >= 0.10.4, SciPy >=
0.17.0, matplotlib >= 1.4.2, [EpiPylib](https://github.com/ckaus/epipylib) >= 0.1

1. Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git && cd EpiPy`
2. Build from sources: `$ python setup.py --command-packages=stdeb.command bdist_deb`
3. Install DEB-package: `$ cd deb_dist/ && sudo dpkg -i epipy_<version>_all.deb`

## Documentation

* [Project Website](http://ckaus.github.io/EpiPy/)
* [Wiki](https://github.com/ckaus/EpiPy/wiki)
* Source code documentation with [Sphinx](http://sphinx-doc.org/).
  * `$ cd EpiPy/doc/ && make html`

## Data Sets

* https://github.com/cmrivers/ebola
* http://opendata.stackexchange.com/questions/3484/2014-ebola-outbreak-dataset
* http://www.cdc.gov/flu/weekly/nchs.htm

### Generated Data Sets

* [data2.csv](http://userpage.fu-berlin.de/kies88/epipy/data/data2.csv): produced by R codes (beta=0.5, gamma=0.1)
* [data3.csv](http://userpage.fu-berlin.de/kies88/epipy/data/data3.csv): produced by epimodel (beta=0.5, gamma=0.1)
* [data4.csv](http://userpage.fu-berlin.de/kies88/epipy/data/data4.csv): produced by R codes (beta=0.7, gamma=0.2)

### Real Data Sets

* [australia_dengue.csv](http://userpage.fu-berlin.de/kies88/epipy/data/australia_dengue.csv)
Department of Health, National Notifiable Diseases Surveillance System, Australia,
http://www9.health.gov.au/cda/source/cda-index.cfm

* [japan_influenza.csv](http://userpage.fu-berlin.de/kies88/epipy/data/japan_influenza.csv),
National Institute of Infectious Diseases, Japan,
http://www.nih.go.jp/niid/en/flu-m/flutoppage/2099-idsc/iasr-flu-e/5924-iasr-inf-e20150910.html

* [liberia_ebola.csv](http://userpage.fu-berlin.de/kies88/epipy/data/liberia_ebola.csv),
WHO,
http://apps.who.int/gho/data/node.ebola-sitrep.ebola-country-LBR?lang=en

* [sierraleone_ebola.csv](http://userpage.fu-berlin.de/kies88/epipy/data/sierraleone_ebola.csv),
WHO,
http://apps.who.int/gho/data/node.ebola-sitrep.ebola-country-SLE?lang=en

* [usa_influenza.csv](http://userpage.fu-berlin.de/kies88/epipy/data/usa_influenza.csv),
CDC FluView,
http://gis.cdc.gov/grasp/fluview/fluportaldashboard.html

## License

[MIT License](https://github.com/ckaus/EpiPy/blob/master/LICENSE)
