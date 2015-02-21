#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{cookiecutter.repo_name}} import {{cookiecutter.app_class_name}}


def main():
    """Create an instance of :class:`{{cookiecutter.app_class_name}}` and call
    its `run` method which in turn invokes :meth:`{{cookiecutter.app_class_name}}.build`.
    """
    {{cookiecutter.app_class_name}}().run()


if __name__ == '__main__':
    main()
