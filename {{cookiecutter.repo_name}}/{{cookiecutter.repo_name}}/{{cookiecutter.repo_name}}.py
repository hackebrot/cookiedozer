# -*- coding: utf-8 -*-

"""
{{cookiecutter.repo_name}}
============================

The root of :class:`{{cookiecutter.app_class_name}}` is created from the kv file.
"""

import kivy
kivy.require('{{cookiecutter.kivy_version}}')

from kivy.app import App


class {{cookiecutter.app_class_name}}(App):
    """Basic Kivy App with a user defined title."""

    title = '{{cookiecutter.app_title}}'

    def build(self):
        return self.root
