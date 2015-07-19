# -*- coding: utf-8 -*-


def test_app_title(app):
    """Simply tests if the default app title meets the expectations.

    Args:
      app (:class:`{{cookiecutter.app_class_name}}`): Default app instance

    Raises:
      AssertionError: If the title does not match
    """
    assert app.title == '{{cookiecutter.app_title}}'


def test_carousel(app):
    """Test for the carousel widget of the app checking the slides' names.

    Args:
      app (:class:`{{cookiecutter.app_class_name}}`): Default app instance

    Raises:
      AssertionError: If the names of the slides do not match the expectations
    """
    names = [slide.name for slide in app.carousel.slides]
    expected = ['hello', 'kivy', 'cookiecutterdozer', 'license', 'github']
    assert names == expected
