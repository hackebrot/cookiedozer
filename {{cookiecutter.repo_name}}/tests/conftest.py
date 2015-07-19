# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="session")
def app(request):
    """Uses the InteractiveLauncher to provide access to an app instance.

    The finalizer stops the launcher once the tests are finished.

    Returns:
      :class:`{{cookiecutter.app_class_name}}`: App instance
    """
    from kivy.interactive import InteractiveLauncher
    from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import {{cookiecutter.app_class_name}}
    launcher = InteractiveLauncher({{cookiecutter.app_class_name}}())

    def stop_launcher():
        launcher.safeOut()
        launcher.stop()

    request.addfinalizer(stop_launcher)

    launcher.run()
    launcher.safeIn()
    return launcher.app
