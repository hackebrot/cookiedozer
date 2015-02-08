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


License
-------

Distributed under the terms of the `MIT license`_, Cookiedozer is free and open source software


Examples
--------

.. image:: https://raw.githubusercontent.com/hackebrot/cookiedozer/master/cookiedozer01.png
.. image:: https://raw.githubusercontent.com/hackebrot/cookiedozer/master/cookiedozer02.png


.. _`Buildozer`: https://github.com/kivy/buildozer
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Kivy`: https://github.com/kivy/kivy
.. _`MIT License`: http://opensource.org/licenses/MIT
.. _`PyPI`: https://pypi.python.org/pypi
.. _`Sphinx`: http://sphinx-doc.org/
.. _`pytest`: http://pytest.org/latest/
