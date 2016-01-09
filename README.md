# EpiPy
A Tool for fitting epidemic models. For more information see [wiki][1]

## Requirements
Python 2.7, `matplotlib`, `scipy`, `pyqtgraph`, PyQt4

*Note:* Debian based operating systems need `pkg-config` to install `matplotlib`.

## Project Structure
```
.
├── doc - Contains the documentation
├── epipy - Contains the sources
├── LICENSE
├── README.md - Description File 
└── setup.py - Installation script
```

## Installation
1. Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git`
2. Navigate to `EpiPy/`.
3. Install EpiPy as *root*:
	* (Developer) `$ pip install -e .`
	* (User) `$ pip install .`

EpiPy is now available in terminal `$ epipy` .

## Remove
Remove EpiPy as *root*
* (Developer)
	* Remove project path in file: `/usr/local/lib/python2.7/dist-packages/easy-install.pth`
	* `$ rm /usr/local/lib/python2.7/dist-packages/EpiPy.egg-link`
	* `$ rm /usr/local/bin/epipy`
* (User)
	* `$ pip uninstall epipy`
 	* `$ rm /usr/local/bin/epipy`

## Literatur
 * [Papers][1]

## Documentation
* Project [wiki][2]
* Sources by using [Sphinx][3]:
  * `$ cd EpiPy/doc`
  * `$ make html`

## License
[MIT license][4]

[1]: https://www.dropbox.com/sh/3gtnm32uq6nn0cu/AAAbHY9DkdnRPuZo-vePaO1Fa?dl=0 "Paper"
[2]: https://github.com/ckaus/EpiPy/wiki "wiki"
[3]: http://sphinx-doc.org/ "Sphinx"
[4]: https://github.com/ckaus/EpiPy/blob/master/LICENSE "MIT license"
