.PHONY: all clean requirements develop test lint flake8 isort dist

all: clean requirements dist

default: develop

clean:
	find src -name '*.pyc' -delete
	find tests -name '*.pyc' -delete
	find . -name '*.egg-info' -delete

requirements:
	pip install --upgrade -e .

develop: clean requirements

test:
	py.test --nomigrations --reuse-db tests/

lint: flake8 isort

flake8:
	pip install flake8 flake8-debugger flake8-blind-except
	flake8 src/

isort:
	pip install isort
	isort --recursive --check-only --diff src tests


dist:
	./setup.py sdist bdist_wheel