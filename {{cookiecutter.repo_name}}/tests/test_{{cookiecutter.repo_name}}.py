# -*- coding: utf-8 -*-

import pytest


def test_app_title(app):
    """Simply tests if the default app title meets the expectations.

    Args:
      app (:class:`{{cookiecutter.app_class_name}}`): Default app instance

    Raises:
      AssertionError: If the title does not match
    """
    assert app.title == '{{cookiecutter.app_title}}'


@pytest.fixture
def carousel(app):
    """Fixture to get the carousel widget of the test app."""
    return app.carousel


def test_carousel(carousel):
    """Test for the carousel widget of the app checking the slides' names and
    the text of one of the slide labels.

    Args:
      carousel (:class:`Carousel`): Carousel widget of :class:`{{cookiecutter.app_class_name}}`

    Raises:
      AssertionError: If the first slide does not contain *Hello*
      AssertionError: If the names of the slides do not match the expectations
    """
    names = [slide.name for slide in carousel.slides]
    expected = ['hello', 'kivy', 'cookiecutterdozer', 'license', 'github']
    assert names == expected
