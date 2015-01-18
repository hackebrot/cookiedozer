import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name = "{{cookiecutter.repo_name}}",
    version = "{{cookiecutter.version}}",
    author = "{{cookiecutter.full_name}}",
    author_email = "{{cookiecutter.email}}",
    description = "{{cookiecutter.short_description}}",
    license = "MIT",
    keywords=(
        "Python, cookiecutter, kivy, buildozer, pytest, projects, project "
        "templates, example, documentation, tutorial, setup.py, package, "
        "android, touch, mobile, NUI"
    ),
    url = "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires = ['kivy>=1.8.0'],
    package_data={
        '{{cookiecutter.repo_name}}': ['*.kv*']
    },
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}}={{cookiecutter.repo_name}}.main:main'
        ]
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: User Interfaces',
    ],
)
