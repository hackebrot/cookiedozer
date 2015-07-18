#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')


def rename_kv_file():
    """Rename the generated kv file to be compatible with the original kivy kv
    file detection of `App.load_kv`.
    """
    logger.info('Renaming kv file')

    import os
    package_dir = '{{cookiecutter.repo_name}}'
    old_kv_file = os.path.join(
        package_dir, '{{cookiecutter.app_class_name}}.kv'
    )

    lower_app_class_name = '{{cookiecutter.app_class_name}}'.lower()
    if (lower_app_class_name.endswith('app')):
        lower_app_class_name = lower_app_class_name[:-3]
    new_kv_file = os.path.join(
        package_dir, '{}.kv'.format(lower_app_class_name)
    )

    os.rename(old_kv_file, new_kv_file)


def generate_i18n_locales():
    """Run 'make mo' to generate the locales from the po files. The app won't
    run without the translation files.
    """
    logger.info('Generating i18n translation files')

    import subprocess
    try:
        subprocess.check_call(['make', 'mo'])
    except subprocess.CalledProcessError:
        logger.warning('Unable to create i18n translation files.')


rename_kv_file()
generate_i18n_locales()
