# EpiPy
A Tool for fitting epidemic models.

## Project Structure
```
.
├── doc - Contains the documentation
├── epipy - Contains the sources
├── LICENSE
├── README.md - Description File 
├── requirements.txt - Contains the necessary libraries
├── scripts - Contains installation and remove scripts
└── setup.py - Installation script is using by `scripts/install.sh`
```

## Installation (Unix)
*The installation steps are tested on Debian 8.2 and Mac OS X 10.11.2*

1. Clone EpiPy: `$ git clone git@github.com:ckaus/EpiPy.git`
2. Navigate to install/remove scripts: `$ cd EpiPy/scripts/`
3. Comment out the installation instructions in `install.sh` for your operating system 
4. Run: `$ sh install.sh`

## Remove (Unix)
*The remove steps are tested on Debian 8.2 and Mac OS X 10.11.2*

1. Navigate to install/remove scripts: `$ cd EpiPy/scripts/`
2. Comment out the remove instructions in `remove.sh` for your operating system
3. Run: `$ sh remove.sh`

## Start EpiPy
Start EpiPy via terminal: `$ epipy`

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