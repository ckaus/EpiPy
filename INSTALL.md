# Installation

Requirements: Pip, NumPy, SciPy, matplotlib, PyQt4

Donwload EpiPy from our [website](http://ckaus.github.io/EpiPy/).

## Build .deb-Package

Requirements: dpkg-buildpackage

```bash
$ bash build.sh epipy
$ cd build/
$ sudo dpkg -i *.deb
```

## With Pip

```bash
$ sudo apt-get install python-qt4
$ sudo pip install -r requirements.txt
```

```bash
$ cd <PATH/TO/FOLDER/>
$ sudo pip install .
```
