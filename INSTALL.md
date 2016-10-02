# Installation

Donwload EpiPy from our [website](http://ckaus.github.io/EpiPy/).

## Build .deb-Package

```bash
$ bash build.sh epipy -deb -c
$ bash build.sh epipy -deb -b
$ cd build/
$ sudo dpkg -i *.deb
```

## With Pip

Requirements: Pip (>= 1.5. 2)

```bash
$ sudo apt-get install python-qt4 python-pip
$ sudo pip install -r requirements.txt
```

```bash
$ cd <PATH/TO/FOLDER/>
$ sudo pip install .
```
