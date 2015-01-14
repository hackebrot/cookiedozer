# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def basic_app():
    """Fixture for a default app.

    Returns:
      :class:`{{cookiecutter.app_class_name}}`: App instance
    """
    from {{cookiecutter.repo_name}} import {{cookiecutter.app_class_name}}
    return {{cookiecutter.app_class_name}}()


def test_app_title(basic_app):
    """Simply tests if the default app title meets our expectations.

    Args:
      basic_app (:class:`{{cookiecutter.app_class_name}}`): Default app instance

    Raises:
      AssertionError: If the title does not match
    """
    assert basic_app.title == "{{cookiecutter.app_title}}"
