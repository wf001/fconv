TARGET = ./fconv ./tests

install:
	pip install -r requirement.txt

check:
	make test && \
		make lint

test:
	pytest --capture=no -vv

lint:
	make mypy-only && \
		black ${TARGET} && \
		isort ${TARGET} && \
		flake8 ${TARGET} --doctest

mypy-only:
	mypy ${TARGET}

