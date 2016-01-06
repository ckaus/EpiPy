#!/bin/bash

# Debian
sudo pip install -r ../requirements.txt
cd ..
sudo python setup.py install

# sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
# sudo python setup.py install --record files.txt
