# EpiPy
A Tool for fitting epidemic models.

## Requirements
 * Python 2.7.9
 * PyQt 4
 * [PyQtGraph][2]
 * [SciPy][3] (+ gi-cairo)

## Installation
`$ git clone git@github.com:ckaus/EpiPy.git`

### Linux

* Download and install the package of [PyQtGraph][2] and [SciPy][7].
* Execute `$sudo apt-get install python-qt4 python-gi-cairo`.

## Start EpiPy
```
$ cd EpiPy/src
$ python main.py
```

## Literatur
 * [Papers][6]

## Documentation
* Project [wiki][1]
* Sources by using [Sphinx][4]:
  * `$ cd doc`
  * `$ make html`

## License
[MIT license][5]

[1]: https://github.com/ckaus/EpiPy/wiki "wiki"
[2]: http://pyqtgraph.org/ "PyQtGraph"
[3]: http://www.scipy.org/install.html "SciPy"
[4]: http://sphinx-doc.org/ "Sphinx"
[5]: https://github.com/ckaus/EpiPy/blob/master/LICENSE "MIT license"  
[6]: https://www.dropbox.com/sh/3gtnm32uq6nn0cu/AAAbHY9DkdnRPuZo-vePaO1Fa?dl=0 "Paper"
[7]: http://www.scipy.org/install.html#linux-packages "Scipy Linux"