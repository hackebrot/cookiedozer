#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rename the generated kv file to be compatible with the original kivy kv file
detection of `App.load_kv`.
"""

import os


package_dir = '{{cookiecutter.repo_name}}'
old_kv_file = os.path.join(package_dir, '{{cookiecutter.app_class_name}}.kv')

lower_app_class_name = '{{cookiecutter.app_class_name}}'.lower()
if (lower_app_class_name.endswith('app')):
    lower_app_class_name = lower_app_class_name[:-3]
new_kv_file = os.path.join(package_dir, '{}.kv'.format(lower_app_class_name))

os.rename(old_kv_file, new_kv_file)
