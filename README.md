# EpiPy
EpiPy is a tool for fitting epidemic models. This tool is developed for the course [Softwareprojekt Mobilkommunikation][1] at the [Freie Universität Berlin][2].

## Introduction
Epidemics have been an interesting subject to study in many disciplines. Not only in epidemiology but also in biology, mathematics, sociology, computer science and more, the study of epidemics offers many areas for application. Mathematicians over time have suggested various models to understand and foresee the development of epidemics.

Several tools are available that can simulate epidemics and generate data with given parameter for an epidemic model. However, there is yet no tool for easy fitting of epidemic models. EpiPy simplifies the fitting of various models to data and aims to help you understand different epidemics models. It offers a range of possibilities for you to explore.

## Installation

### Windows

Requirements:

* [Python 2.7.11](https://www.python.org/downloads/release/python-2711/)
* [matplotlib-1.5.1-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib)
* [numpy-1.10.4+mkl-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
* [scipy-0.17.0-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)
* [PyQt4-4.11.4-cp27-none-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)

1. Install all needed libraries with Pip.
1. Navigate to `install_packages` and execute `EpiPy-0.1.win-amd64.msi`
2. EpiPy is now available in `C:\Python27\Scripts\`.

### Unix

Requirements: Python 2.7, NumPy 1.10.4, matplotlib 1.4.2, SciPy 0.17.0, PyQt4

1. Install with Pip: `$ pip install -r requirements.txt` *or* follow the install instructions on [SciPy][7].
2. Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git`.
3. Navigate to `EpiPy/`.
4. Install EpiPy as *root*:
	* (Developer) `$ pip install -e .`
	* (User) `$ pip install .`
5. EpiPy is now available in terminal `$ epipy` .

## Features

* Fitting epidemic data
* Plotting epidemic data and fitted epidemic model
* Manual and optimized manipulation epidemic model parameters
* Using different epidemic models:
 * **S**usceptible **I**nfected **R**ecovered
   * Simple, With births and deaths, With Vaccine
 * **S**usceptible **I**nfected **R**ecovered **S**usceptible
   * Simple, With births and deaths
 * **S**usceptible **E**xposed **I**nfected **R**ecovered
   * Simple

## Screenshots

## Documentation
Take a look into our [wiki][4] and / or generate the documentation of the sources by using [Sphinx][5].

* `$ cd EpiPy/doc`
* `$ make html`

## License
[MIT][6] license

[1]: http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html "Course"
[2]: http://www.fu-berlin.de/en/index.html "FU Berlin"
[3]: http://sourceforge.net/projects/winpython/files/WinPython_2.7/2.7.10.3/ "WinPython 2.7"
[4]: https://github.com/ckaus/EpiPy/wiki "wiki"
[5]: http://sphinx-doc.org/ "Sphinx"
[6]: https://github.com/ckaus/EpiPy/blob/master/LICENSE "MIT license"
[7]: http://www.scipy.org/install.html
