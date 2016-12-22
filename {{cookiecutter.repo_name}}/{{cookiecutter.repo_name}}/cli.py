#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ["KIVY_NO_ARGS"] = "1"

import click

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import {{cookiecutter.app_class_name}}


@click.command()
@click.option(
    '-l', '--language', help='Default language of the App', default='en',
    type=click.Choice(['en', 'es', 'de', 'fr'])
)
def main(language):
    """Run {{cookiecutter.app_class_name}} with the given language setting.
    """
    {{cookiecutter.app_class_name}}(language).run()
