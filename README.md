# EpiPy
EpiPy is a tool for fitting epidemic models. This tool is developed for the course [Softwareprojekt Mobilkommunikation][1] at the [Freie Universität Berlin][2].

## Introduction
Epidemics have been an interesting subject to study in many disciplines. Not only in epidemiology but also in biology, mathematics, sociology, computer science and more, the study of epidemics offers many areas for application. Mathematicians over time have suggested various models to understand and foresee the development of epidemics.

Several tools are available that can simulate epidemics and generate data with given parameter for an epidemic model. However, there is yet no tool for easy fitting of epidemic models. EpiPy simplifies the fitting of various models to data and aims to help you understand different epidemics models. It offers a range of possibilities for you to explore.

## Installation

The installation instructions can be found [here][8].

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

## Documentation
Take a look into our [wiki][4] and / or generate the documentation of the sources with [Sphinx][5].

* `$ cd EpiPy/doc/ && make html`

## License
[MIT][6] license

[1]: http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html "Course"
[2]: http://www.fu-berlin.de/en/index.html "FU Berlin"
[3]: http://sourceforge.net/projects/winpython/files/WinPython_2.7/2.7.10.3/ "WinPython 2.7"
[4]: https://github.com/ckaus/EpiPy/wiki "wiki"
[5]: http://sphinx-doc.org/ "Sphinx"
[6]: https://github.com/ckaus/EpiPy/blob/master/LICENSE "MIT license"
[7]: http://www.scipy.org/install.html
[8]: https://github.com/ckaus/EpiPy/blob/master/install_packages "Installation of EpiPy"
