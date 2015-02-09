===========
Cookiedozer
===========

`Cookiecutter`_ template for Python `Kivy`_ apps ready to be deployed to android devices with `Buildozer`_.


Features
--------

* Installable `PyPI`_ package featuring a ``setup.py`` and a ``TestCommand``
* Test suite running `pytest`_ that includes a fixture for your app using the ``InteractiveLauncher``
* `Sphinx`_ docs that can be used to generate a readable ``html`` documentation
* `Buildozer`_ spec file that is used to deploy your app to an Android mobile device
* ``Makefile`` featuring several targets for important tasks such as ``coverage`` and ``apk``


Usage
-----

Generate a Kivy project::

    cookiecutter https://github.com/hackebrot/cookiedozer


Tutorials
---------

Parts of this template are explained in great detail over the course of the following tutorials:

* Part 1: `Create Your Own Cookiecutter`_
* Part 2: `Extending Cookiedozer`_
* Part 3: `Wrapping up Cookiedozer`_


License
-------

Distributed under the terms of the `MIT license`_, Cookiedozer is free and open source software


Examples
--------

.. image:: https://raw.githubusercontent.com/hackebrot/cookiedozer/master/cookiedozer01.png
.. image:: https://raw.githubusercontent.com/hackebrot/cookiedozer/master/cookiedozer02.png


.. _`Buildozer`: https://github.com/kivy/buildozer
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Create Your Own Cookiecutter`: http://www.hackebrot.de/python/create-your-own-cookiecutter/
.. _`Extending Cookiedozer`: http://www.hackebrot.de/python/extending-cookiedozer/
.. _`Kivy`: https://github.com/kivy/kivy
.. _`MIT License`: http://opensource.org/licenses/MIT
.. _`PyPI`: https://pypi.python.org/pypi
.. _`Sphinx`: http://sphinx-doc.org/
.. _`Wrapping up Cookiedozer`: http://www.hackebrot.de/python/wrapping-up-cookiedozer/
.. _`pytest`: http://pytest.org/latest/
