# EpiPy
A Tool for fitting epidemic models. For more information see [wiki][1].

## Requirements
Python 2.7, `numpy`, `matplotlib`, [SciPy][4], `pyqtgraph`, PyQt4

*Note:* Debian based operating systems need probably `pkg-config`.

## Project Structure
```
.
├── doc - Contains the documentation
├── epipy - Contains the sources
├── LICENSE
├── README.md - Description File 
└── setup.py - Installation script
```

## Install
Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git`

### Unix
1. Navigate to `EpiPy/`.
2. Install EpiPy as *root*:
	* (Developer) `$ pip install -e .`
	* (User) `$ pip install .`

EpiPy is now available in terminal `$ epipy` .

### Windows
1. We recommend [WinPython 2.7][6], which includes all [required packages][7].
2. Open your `WinPython Command Prompt` and navigate to `EpiPy/`.
3. Install EpiPy:
	* (Developer) `$ pip install -e .`
	* (User) `$ pip install .`

EpiPy is now available in terminal `$ epipy` .

## Uninstall

### Unix
Remove EpiPy as *root*
* (Developer)
	* Remove project path in file: `/usr/local/lib/python2.7/dist-packages/easy-install.pth`
	* `$ rm /usr/local/lib/python2.7/dist-packages/EpiPy.egg-link`
	* `$ rm /usr/local/bin/epipy`
* (User)
	* `$ pip uninstall epipy`

### Windows
(Developer/User): Open your `WinPython Command Prompt` and execute `$ pip uninstall epipy`.

## Screenshots

![Debian](https://github.com/ckaus/EpiPy/blob/master/doc/screenshots/epipy_alpha_debian.png "Debian")
![Windows](https://github.com/ckaus/EpiPy/blob/master/doc/screenshots/epipy_alpha_windows.png "Window")

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
[5]: http://www.scipy.org/install.html "SciPy"
[6]: http://sourceforge.net/projects/winpython/files/WinPython_2.7/2.7.10.3/ "WinPython 2.7"
[7]: http://sourceforge.net/p/winpython/wiki/PackageIndex_27/ "WinPython 2.7 Packages"