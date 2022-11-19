TARGET = ./former ./tests

install:
	pip install -r requirement.txt

check:
	make test &&\
		make lint

test:
	pytest --capture=no -vv

lint:
	mypy ${TARGET}
		black ${TARGET} && \
		isort ${TARGET} &&\
		flake8 ${TARGET} --doctest

