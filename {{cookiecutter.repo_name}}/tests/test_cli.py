import pytest
from click.testing import CliRunner

from {{cookiecutter.repo_name}}.cli import main


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture(params=['en', 'es', 'de', 'fr'])
def lang(request):
    return request.param


@pytest.fixture(params=['-l', '--language'])
def cli_param(request):
    return request.param


@pytest.fixture
def mock_app(mocker):
    return mocker.patch('{{cookiecutter.repo_name}}.cli.{{cookiecutter.app_class_name}}')


def test_language_to_app(runner, mock_app, cli_param, lang):
    result = runner.invoke(main, [cli_param,lang])
    assert result.exit_code == 0
    mock_app.assert_called_once_with(lang)


def test_abort_with_invalid_lang(runner, mock_app):
    result = runner.invoke(main, ['-l', 'foobar'])
    assert result.exit_code != 0
    assert not mock_app.called
