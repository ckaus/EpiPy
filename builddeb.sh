#!/bin/bash
################################################################################
# Description: Build .deb package of EpiPy - ckaus - 20160928
#
# Requirements: Pip, dh_make, dpkg-buildpackage
#
# Usage:  $ sh builddeb.sh -o ../build
#         $ cd ../build/ && dpkg -i epipy_<version>_all.deb
################################################################################

help ()
{
  echo 'Usage:'
  echo '  builddeb [options]'
  echo 'Options:'
  echo '  -o, --outputdir <relativepath>  Build the package in relative path.'
  echo 'General Options:'
  echo '  -h, --help                      Show the help and exit.'
  echo 'Example:'
  echo '  sh builddeb.sh -o ../build'
  exit 0
}

VERSION=`python -c 'import epipy; print epipy.__version__'`
MAINTAINER=`python -c 'import epipy; print epipy.__maintainer__'`
MAINTAINER_EMAIL=`python -c 'import epipy; print epipy.__maintainer_email__'`
DESCRIPTION=`python -c 'import epipy; print epipy.__description__'`

OUTPUT_DIR=$(pwd)/build
case $2 in
  -o|--outputdir) OUTPUT_DIR=$(pwd)/$3 ;;
  -h|--help)  help ;;
esac

if [ ! -d $OUTPUT_DIR ]; then
  mkdir $OUTPUT_DIR
fi

if [ -d $OUTPUT_DIR/debian ]; then
  rm -r $OUTPUT_DIR/debian
fi

################################################################################
# Create .deb package files
mkdir $OUTPUT_DIR/debian
mkdir $OUTPUT_DIR/debian/source
echo '3.0 (native)' > $OUTPUT_DIR/debian/source/format
cp CHANGELOG $OUTPUT_DIR/debian/changelog
echo '[Desktop Entry]
Encoding=UTF-8
Name=EpiPy
Version=<VERSION>
Comment=<DESCRIPTION>
GenericName=EpiPy Science
Terminal=false
Icon=/usr/share/applications/epipy-logo.png
Type=Application
Exec=epipy
Categories=Science;Education;' >> $OUTPUT_DIR/debian/epipy.desktop
sed -i 's/<VERSION>/'$VERSION'/g' $OUTPUT_DIR/debian/epipy.desktop
sed -i 's/<DESCRIPTION>/'$DESCRIPTION'/g' $OUTPUT_DIR/debian/epipy.desktop
echo 'debian/epipy.desktop usr/share/applications' > $OUTPUT_DIR/debian/install
cp epipy-logo.png $OUTPUT_DIR/debian/
echo 'debian/epipy-logo.png usr/share/icons' >> $OUTPUT_DIR/debian/install
echo '9' > $OUTPUT_DIR/debian/compat
echo 'Source: epipy
Section: science
Priority: optional
Maintainer: <MAINTAINER> <<MAINTAINER_EMAIL>>
Build-Depends: debhelper (>= 9.20150101+deb8u2), dh-python (>= 1.20141111-2)
XS-Python-Version: >= 2.7
Standards-Version: <VERSION>

Package: epipy
Architecture: all
Homepage: https://github.com/ckaus/EpiPy
Depends: python-numpy (>= 1:1.8), python-numpy (<< 1:1.9), python-scipy (>= 0.14.0), python-scipy (<< 0.17.0), python-matplotlib (>= 1.4.2), python-qt (>= 4.8.6)
Description: Python GUI tool for fitting epidemic models.
 Several tools are available that can simulate epidemics and generate
 data with given parameter for an epidemic model. However, there is yet
 no tool for easy fitting of epidemic models. EpiPy simplifies the
 fitting of various models to data and aims to help you understand
 different epidemics models. It offers a range of possibilities for you
 to explore.' > $OUTPUT_DIR/debian/control
sed -i 's/<MAINTAINER>/'$MAINTAINER'/g' $OUTPUT_DIR/debian/control
sed -i 's/<MAINTAINER_EMAIL>/'$MAINTAINER_EMAIL'/g' $OUTPUT_DIR/debian/control
sed -i 's/<VERSION>/'$VERSION'/g' $OUTPUT_DIR/debian/control

echo 'The Debian packaging is:

    Copyright (C) 2016 <MAINTAINER> <MAINTAINER_EMAIL>

and is licensed under the MIT license.
' > $OUTPUT_DIR/debian/copyright
sed -i 's/<MAINTAINER>/'$MAINTAINER'/g' $OUTPUT_DIR/debian/copyright
sed -i 's/<MAINTAINER_EMAIL>/'$MAINTAINER_EMAIL'/g' $OUTPUT_DIR/debian/copyright
cat LICENSE >> $OUTPUT_DIR/debian/copyright
echo '#!/usr/bin/make -f
%:
	dh $@' > $OUTPUT_DIR/debian/rules
chmod +x $OUTPUT_DIR/debian/rules
touch $OUTPUT_DIR/debian/watch
################################################################################
# Build .deb package
python setup.py sdist --dist-dir=$OUTPUT_DIR
cd $OUTPUT_DIR && tar -xf epipy-$VERSION.tar.gz
cp -r $OUTPUT_DIR/debian epipy-$VERSION
cd epipy-$VERSION
dh_make --native -C s -c mit
dpkg-buildpackage -i -I -rfakeroot
# Check .deb package with lintian
lintian $OUTPUT_DIR/*.deb
