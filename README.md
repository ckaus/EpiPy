# EpiPy
A Tool for fitting epidemic models.

This tool is developed under the [MIT license][1] for the course [Softwareprojekt Mobilkommunikation][2] at the [Freie Universität Berlin][3]. 

## Requirements
 * Python 2.7.9
 * PyQt 4
 * [PyQtGraph][4] 0.9.10

## Installation
```bash
$ sudo apt-get intall python-qt4

$ git clone git@github.com:pyqtgraph/pyqtgraph.git
$ cd pyqtgraph/
$ sudo python setup.py install

$ git clone git@github.com:ckaus/EpiPy.git
```

You can build the documentation using [Sphinx][5]:
```bash
$ cd doc
$ make html
```
## Introduction

You can start EpiPy in terminal: `$ python src/main.py`

## What's new
 * 2015-10-13: Project start
 * 2015-11-10: First GUI

[1]: https://github.com/ckaus/EpiPy/blob/master/LICENSE "MIT license"         
[2]: http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html "Course"
[3]: http://www.fu-berlin.de/en/index.html "FU Berlin"
[4]: http://pyqtgraph.org/ "PyQtGraph"
[5]: http://sphinx-doc.org/ "Sphinx"
