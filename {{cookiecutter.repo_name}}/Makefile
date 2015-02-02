.PHONY: docs

test:
	python setup.py test

coverage:
	python setup.py test -a '--cov={{cookiecutter.repo_name}} --cov-report=html'
	xdg-open htmlcov/index.html

docs:
	$(MAKE) -C docs html
	xdg-open docs/build/html/index.html

apk:
	buildozer -v android debug

deploy:
	buildozer android deploy logcat
