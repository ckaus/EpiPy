#!/usr/bin/env bash
################################################################################
# File: build.sh
# Author: ckaus
# Last change: 2016-10-05
# Version: 0.1.3
# Requirements: dpkg-buildpackage
# Description: Create and build a .deb-Package from python package.
################################################################################
Help () {
  echo 'Usage: bash '$(basename $0)' <source-path>'
  exit 0
}
################################################################################
# Translate Pip package name/version into valid Apt package name/version.
# Pip             -> Apt
# foo             -> foo or python-foo
# foo==1.0.0      -> foo or python-foo
# foo>=1.0.0      -> foo (>= 1.0.0) or python-foo (>= 1.0.0)
# foo_bar==1.0.0  -> foo-bar or python-foo-bar
################################################################################
Translate_req ()
{
  IFS=$'\r\n' command eval 'REQ_ARR=($@)'
  APT_PKG_LIST=''
  for REQ in "${REQ_ARR[@]}"
  do
    REQ="$(sed -e 's/_/-/' <<< ${REQ})"
    PIP_PKG_NAME=$(grep -oP '[A-Za-z-]+' <<< ${REQ})
    # Search for <pacakge> in Apt
    APT_PKG_VRS="$(apt-cache show ${PIP_PKG_NAME} 2> /dev/null\
      | grep 'Version: ')"
    APT_PKG_VRS="$(sed -r '/Version: /s///' <<< ${APT_PKG_VRS})"
    if [ -z "${APT_PKG_VRS}" ]; then
      # Search for python-<package> just in case <package> isnt available in Apt
      APT_PKG_VRS="$(apt-cache show python-${PIP_PKG_NAME} 2> /dev/null\
        | grep 'Version: ')"
      APT_PKG_VRS="$(sed -r '/Version: /s///' <<< ${APT_PKG_VRS})"
      if [ -z "${APT_PKG_VRS}" ]; then
        echo "[ERROR] Cannot find package python-${PIP_PKG_NAME} or\
          ${PIP_PKG_NAME} in Apt Required package: ${PIP_PKG_NAME} will not add\
          to 'Depends' in debian/control."
        continue
      fi
      APT_PKG="python-${PIP_PKG_NAME}"
    else
      APT_PKG=${PIP_PKG_NAME}
    fi
    if [ ! -z "$(grep -oP '[A-Za-z]+[>=]=' <<< ${REQ})" ]; then
      # Match Pip package version (if exist ) with Apt package version
      PIP_PKG_VRS="$(grep -oP '[0-9]+.*' <<< $REQ)"
      if [ -z "$(grep -oP "$PIP_PKG_VRS" <<< $APT_PKG_VRS)" ]; then
        echo "[ERROR] Pip package version ${PIP_PKG_VRS} did not match Apt\
        package version $APT_PKG_VRS. Package will not add to'Depends' in\
        debian/control."
        continue
      fi
      DELIMITER="$(grep -oP '\>\=' <<< ${REQ})"
      if [ ! -z $DELIMITER ]; then
        APT_PKG="python-$PIP_PKG_NAME ($DELIMITER $APT_PKG_VRS)"
      fi
    fi
    APT_PKG_LIST+="${APT_PKG}, "
  done
  echo ${APT_PKG_LIST::-2}
}

if [ $# -eq 0 ] || [ ! -d $1 ]; then
  Help
fi
################################################################################
# Create and build .deb package in ./build/
################################################################################
PROJ_DIR=$(pwd)
SRC_DIR=$1
SRC_PATH="$(pwd)/$1"
BUILD_PATH="$PROJ_DIR/build"
if [ -d "$BUILD_PATH" ]; then
  rm -r "$BUILD_PATH"
fi
# Create debian folder structure in /tmp/build/
mkdir "$BUILD_PATH" "$BUILD_PATH/debian" "$BUILD_PATH/debian/sources"
# Build sources with setup.py
python "$PROJ_DIR"/setup.py build --build-lib $BUILD_PATH
# debian/control
SOURCE=$(python setup.py --name)
AUTHOR=$(python setup.py --author)
AUTHOR_EMAIL=$(python setup.py --author-email)
VERSION=$(python setup.py --version)
MAINTAINER=$(python setup.py --maintainer)
MAINTAINER_EMAIL=$(python setup.py --maintainer-email)
DESCRIPTION=$(python setup.py --description)
DESCRIPTION_LONG=$(python setup.py --long-description)
HOMEPAGE=$(python setup.py --url)
DEPENDS=$(Translate_req $(cat $SOURCE.egg-info/requires.txt))
# source directory must have the format <sourcepackage>-<upstreamversion>
mv $BUILD_PATH/$SOURCE $BUILD_PATH/$SOURCE-$VERSION
# debian/control"
echo -e "Source: $SOURCE
Section: science
Priority: optional
Maintainer: $MAINTAINER <$MAINTAINER_EMAIL>
Build-Depends: debhelper (>= 9.20150101+deb8u2), dh-python (>= 1.20141111-2)
XS-Python-Version: >= 2.7
Standards-Version: $VERSION
Homepage: $HOMEPAGE

Package: $SRC_DIR
Architecture: all
Depends: $DEPENDS, python-qt4
Description: $DESCRIPTION\n ${DESCRIPTION_LONG}" >> "$BUILD_PATH/debian/control"
# debian/changelog
cp "CHANGELOG" "$BUILD_PATH/debian/changelog"
# debian/watch
touch "$BUILD_PATH/debian/watch"
# debian/compate
echo "9" > "$BUILD_PATH/debian/compat"
# debian/copyright
echo "The Debian packaging is:
  Copyright (C) $(date +%"Y") $MAINTAINER <$AUTHOR_EMAIL>
and is licensed under the MIT license
" > "$BUILD_PATH/debian/copyright"
# debian/copyright
cat "LICENSE" >> "$BUILD_PATH/debian/copyright"
# debian/rules
echo -e '#!/usr/bin/make -f
%:
\t dh $@' > "$BUILD_PATH/debian/rules"
chmod +x "$BUILD_PATH/debian/rules"
# debian/sources/format/watch
echo "3.0 (native)" > "$BUILD_PATH/debian/sources/format"
# Build .deb package
cd $BUILD_PATH
dpkg-buildpackage -A -uc
# Move .deb and .changes to build path
mv "$PROJ_DIR/${SOURCE}_${VERSION}_all.deb" $BUILD_PATH
mv "$PROJ_DIR/${SOURCE}_${VERSION}_all.changes" $BUILD_PATH
lintian ${SOURCE}_${VERSION}_all.deb
