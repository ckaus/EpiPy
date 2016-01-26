EpiPy
=====

EpiPy is a Tool for fitting epidemic models. This tool is developed for
the course `Softwareprojekt
Mobilkommunikation <http://www.mi.fu-berlin.de/inf/groups/ag-tech/teaching/2015-16_WS/P_19308912_Softwareprojekt_Mobilkommunikation/index.html>`__
at the `Freie Universität
Berlin <http://www.fu-berlin.de/en/index.html>`__. For more information
see `wiki <https://github.com/ckaus/EpiPy/wiki>`__.

Requirements
------------

Python 2.7, NumPy, matplotlib, SciPy, PyQt4

*Note:* Debian based operating systems need probably ``pkg-config``.

Installation
------------

Clone EpiPy: ``$ git clone git@github.com:ckaus/EpiPy.git``.

Unix
~~~~

Make sure you have installed all `requirements <#requirements>`__.

1. Navigate to ``EpiPy/``.
2. Install EpiPy as *root*:

   -  (Developer) ``$ pip install -e .``
   -  (User) ``$ pip install .``

3. EpiPy is now available in terminal ``$ epipy`` .

Windows
~~~~~~~

We recommend `WinPython
2.7 <http://sourceforge.net/projects/winpython/files/WinPython_2.7/2.7.10.3/>`__,
which includes all `requirements <#requirements>`__.

1. Open your ``WinPython Command Prompt`` and navigate to ``EpiPy/``.
2. Install EpiPy:

   -  (Developer) ``$ pip install -e .``
   -  (User) ``$ pip install .``

3. EpiPy is now available in terminal ``$ epipy`` .

Uninstall
---------

Unix
~~~~

Remove EpiPy as *root*:

-  (Developer)

   -  Remove project path in file:
      ``/usr/local/lib/python2.7/dist-packages/easy-install.pth``
   -  ``$ rm /usr/local/lib/python2.7/dist-packages/EpiPy.egg-link``
   -  ``$ rm /usr/local/bin/epipy``

-  (User)

   -  ``$ pip uninstall epipy``

Windows
~~~~~~~

(Developer/User): Open your ``WinPython Command Prompt`` and execute
``$ pip uninstall epipy``.

Screenshots
-----------

.. figure:: https://github.com/ckaus/EpiPy/blob/master/doc/screenshots/epipy_alpha_debian.png
   :alt: Debian

   Debian
Literature
----------

-  `Papers <https://www.dropbox.com/sh/3gtnm32uq6nn0cu/AAAbHY9DkdnRPuZo-vePaO1Fa?dl=0>`__

Documentation
-------------

Generate documentation of sources by using
`Sphinx <http://sphinx-doc.org/>`__:

-  ``$ cd EpiPy/doc``
-  ``$ make html``

*Note:* If you edit ``README.md`` you can easley create the
``README.rst`` with:

-  ``$ cd EpiPy``
-  ``$ pandoc README.md --from markdown --to rst -s -o README.rst``

License
-------

`MIT license <https://github.com/ckaus/EpiPy/blob/master/LICENSE>`__
