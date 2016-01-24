# EpiPy
EpiPy is a Tool for fitting epidemic models. This tool is developed for the course [Softwareprojekt Mobilkommunikation][1] at the [Freie Universität Berlin][2]. For more information see [wiki][3].

## Requirements
Python 2.7, NumPy, matplotlib, SciPy, PyQt4

*Note:* Debian based operating systems need probably `pkg-config`.

## Installation
Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git`.

### Unix
Make sure you have installed all [requirements](#requirements).

1. Navigate to `EpiPy/`.
2. Install EpiPy as *root*:
	* (Developer) `$ pip install -e .`
	* (User) `$ pip install .`
3. EpiPy is now available in terminal `$ epipy` .

### Windows
We recommend [WinPython 2.7][4], which includes all [requirements](#requirements).

1. Open your `WinPython Command Prompt` and navigate to `EpiPy/`.
2. Install EpiPy:
	* (Developer) `$ pip install -e .`
	* (User) `$ pip install .`
3. EpiPy is now available in terminal `$ epipy` .

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

## Literature
 * [Papers][5]

## Documentation
Generate documentation of sources by using [Sphinx][6]:
  * `$ cd EpiPy/doc`
  * `$ make html`

## License
[MIT license][7]


[1]: http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html "Course"
[2]: http://www.fu-berlin.de/en/index.html "FU Berlin"
[3]: https://github.com/ckaus/EpiPy/wiki "wiki"
[4]: http://sourceforge.net/projects/winpython/files/WinPython_2.7/2.7.10.3/ "WinPython 2.7"
[5]: https://www.dropbox.com/sh/3gtnm32uq6nn0cu/AAAbHY9DkdnRPuZo-vePaO1Fa?dl=0 "Paper"
[6]: http://sphinx-doc.org/ "Sphinx"
[7]: https://github.com/ckaus/EpiPy/blob/master/LICENSE "MIT license"
