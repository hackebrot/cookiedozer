===========
Cookiedozer
===========

Feature-rich `Cookiecutter`_ template for Python `Kivy`_ apps that greatly simplifies the deployment to Android devices using `Buildozer`_.

For a minimal `Kivy`_ app template please check out `cookiecutter-kivy`_.

Features
--------

* Installable `PyPI`_ package featuring a ``setup.py`` and a ``TestCommand``
* Test suite running `pytest`_ that includes a fixture for your app using the ``InteractiveLauncher``
* `Sphinx`_ docs that can be used to generate a readable ``html`` documentation
* `Buildozer`_ spec file that is used to deploy your app to an Android mobile device
* ``Makefile`` featuring several targets for important tasks such as ``coverage`` and ``apk``
* Comprehensive ``README.rst`` file that contains useful information about your app


Usage
-----

Generate a Kivy project::

    cookiecutter https://github.com/hackebrot/cookiedozer


Tutorials
---------

Parts of this template are explained in great detail over the course of the following tutorials:

* Part 1: `Create your own Cookiecutter template`_
* Part 2: `Extending our Cookiecutter template`_
* Part 3: `Wrapping up our Cookiecutter template`_


Constraints
-----------

The tool at hand for creating and deploying an apk, namely `Buildozer`_, is currently in beta stage.
Although it doesn’t depend on any library, you must have a Linux or OSX computer to be able to compile for Android.

See `Buildozer Docs`_.


License
-------

Distributed under the terms of the `MIT license`_, Cookiedozer is free and open source software


Issues
------

This template has been tested on Ubuntu Trusty Tahr as well as Mac OS X Yosemite.

If you encounter any problems, please `file an issue`_ along with a detailed description.


Examples
--------

.. image:: https://raw.githubusercontent.com/hackebrot/cookiedozer/master/cookiedozer01.png
.. image:: https://raw.githubusercontent.com/hackebrot/cookiedozer/master/cookiedozer02.png


.. _`Buildozer Docs`: http://buildozer.readthedocs.org/en/latest/index.html
.. _`Buildozer`: https://github.com/kivy/buildozer
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Create your own Cookiecutter template`: https://raphael.codes/blog/create-your-own-cookiecutter-template/
.. _`Extending our Cookiecutter template`: https://raphael.codes/blog/extending-our-cookiecutter-template/
.. _`Kivy`: https://github.com/kivy/kivy
.. _`MIT License`: http://opensource.org/licenses/MIT
.. _`PyPI`: https://pypi.python.org/pypi
.. _`Sphinx`: http://sphinx-doc.org/
.. _`Wrapping up our Cookiecutter template`: https://raphael.codes/blog/wrapping-up-our-cookiecutter-template/
.. _`cookiecutter-kivy`: https://github.com/hackebrot/cookiecutter-kivy
.. _`file an issue`: https://github.com/hackebrot/cookiedozer/issues
.. _`pytest`: http://pytest.org/latest/
