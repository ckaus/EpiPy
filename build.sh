#!/usr/bin/env bash
################################################################################
# File: build.sh
# Author: ckaus
# Last change: 2016-10-02
# Version: 0.1.0
# Requirements: dh_make, dpkg-buildpackage
# Description: Create/build a .deb-Package from python package.
################################################################################
Help () {
  echo 'Usage:'
  echo '    bash './$(basename $0)' <source-path> [options]'
  echo
  echo 'Options:'
  echo '    -deb [.deb-options]     Create/Build .deb-Package'
  echo
  echo '.deb-options:'
  echo '    -b| --build            Build .deb-package folder structure'
  echo '    -c| --create            Create .deb-package folder structure'
  echo
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
  IFS=$'\r\n' command eval  'REQ_ARR=($(cat $CWD/requirements.txt))'
  APT_PKG_ARR=()

  for REQ in "${REQ_ARR[@]}"
  do
    REQ="$(sed -e 's/_/-/' <<< ${REQ})"
    PIP_PKG_NAME=$(grep -oP '[A-Za-z-]+' <<< ${REQ})
    ############################################################################
    # Search for <pacakge> in Apt
    ############################################################################
    APT_PKG_VRS="$(apt-cache show ${PIP_PKG_NAME} 2> /dev/null\
      | grep 'Version: ')"
    APT_PKG_VRS="$(sed -r '/Version: /s///' <<< ${APT_PKG_VRS})"
    if [ -z "${APT_PKG_VRS}" ]; then
      ##########################################################################
      # Search for python-<package> just in case <package> isnt available in Apt
      ##########################################################################
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
      ##########################################################################
      # Match Pip package version (if exist ) with Apt package version
      ##########################################################################
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
    APT_PKG_ARR+=("${APT_PKG}")
  done
}
################################################################################
# Create .deb-package folder structure
################################################################################
Deb_create ()
{
  Translate_req

  BUILD_PATH="/tmp/build"
  if [ -d $BUILD_PATH ]; then
    BUILD_PATH="/tmp/build-$(date +%s)"
  fi
  mkdir "$BUILD_PATH" "$BUILD_PATH/debian" "$BUILD_PATH/debian/sources"

  AUTHOR=$(python setup.py --author)
  AUTHOR_EMAIL=$(python setup.py --author-email)
  VERSION=$(python setup.py --version)
  MAINTAINER=$(python setup.py --maintainer)
  MAINTAINER_EMAIL=$(python setup.py --maintainer-email)
  DESCRIPTION=$(python setup.py --description)
  DESCRIPTION_LONG=$(python setup.py --long-description)
  HOMEPAGE=$(python setup.py --url)

  cp "CHANGELOG" "$BUILD_PATH/debian/changelog"

  touch "$BUILD_PATH/debian/watch"
  echo "9" > "$BUILD_PATH/debian/compat"

  echo "Source: $SRC_DIR
Section: science
Priority: optional
Maintainer: $MAINTAINER <$MAINTAINER_EMAIL>
Build-Depends: debhelper (>= 9.20150101+deb8u2), dh-python (>= 1.20141111-2)
XS-Python-Version: >= 2.7
Standards-Version: $VERSION

Package: $SRC_DIR
Architecture: all
Homepage: $HOMEPAGE
Depends: $APT_PKG_ARR
Description: $DESCRIPTION" >> "$BUILD_PATH/debian/control"

  YEAR=$(date +%"Y")
  echo "The Debian packaging is:

    Copyright (C) $YEAR $MAINTAINER <$AUTHOR_EMAIL>

and is licensed under the MIT license
" > "$BUILD_PATH/debian/copyright"

  cat "LICENSE" >> "$BUILD_PATH/debian/copyright"
  echo -e '#!/usr/bin/make -f
%:
\t dh $@' > "$BUILD_PATH/debian/rules"
  chmod +x "$BUILD_PATH/debian/rules"
  echo "3.0 (native)" > "$BUILD_PATH/debian/sources/format"

  #cp $RESOURCES/application.desktop .
  #sed -i "s/<NAME>/$SOURCE_DIR/g" ./application.desktop
  #sed -i "s/<VERSION>/$VERSION/g" ./application.desktop
  #sed -i "s/<COMMENT>/$DESCRIPTION/g" ./application.desktop
  #sed -i "s/<GenericName>/$SOURCE_DIR/g" ./application.desktop
  #sed -i "s/<ICON>/usr\/share\/icons\/$SOURCE_DIR.png/g" ./application.desktop
  #sed -i "s/<EXEC>/$SOURCE_DIR/g" ./application.desktop
  #echo "$RESOURCES/$SOURCE_DIR.desktop usr/share/applications" > install

  #cp $RESOURCES/application.png .
  #echo "$RESOURCES/$SOURCE_DIR.png usr/share/icons" > install

  if [ ! -d "$CWD/build" ]; then
    mkdir "$CWD/build"
  fi
  cp -r "$BUILD_PATH/debian" "$CWD/build/"
  rm -r "$BUILD_PATH"
}
################################################################################
# Build .deb-package
################################################################################
Deb_build ()
{
  if grep -q -E "<[a-zA-Z]{1,}>" "$CWD/build/debian/control"; then
    echo "[ERROR] Please edit the following fields in ./build/debian/control"
    grep -E "<[a-zA-Z]{1,}>" "$CWD/build/debian/control"
    exit 1
  fi

  python setup.py sdist --dist-dir="$CWD/build"

  cd "$CWD/build"

  PROJECT_NAME=$(grep -oP "Source:\s+\K\w+" debian/control)
  PROJECT_VERSION=$(grep -oP "Standards-Version:\s+\K\d.{1,}" debian/control)

  tar -xf "$SRC_DIR-$PROJECT_VERSION.tar.gz"
  cp -r "debian" "$PROJECT_NAME-$PROJECT_VERSION"
  cd "$PROJECT_NAME-$PROJECT_VERSION"
  dh_make --native -C s -c mit
  dpkg-buildpackage -i -I -rfakeroot
  # Check .deb package with lintian
  cd "$CWD/build/" && lintian *.deb
}

if [ $# -eq 0 ] || [ ! -d $1 ]; then
  Help
else
  CWD=$(pwd)
  SRC_DIR=$1
  SRC_PATH=$CWD/$SRC_DIR
fi

case $2 in
  -deb)
  case $3 in
    -c|--create) Deb_create;;
    -b|--build) Deb_build;;
    *|-*) Help;;
  esac;;
  *|-*|-h|--help) Help ;;
esac
