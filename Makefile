TARGET = ./src ./tests

install:
	pip install -r requirement.txt

test:
	pytest --capture=no -vv

lint:
	make mypy-only && \
		black ${TARGET} && \
		isort ${TARGET} &&\
		flake8 ${TARGET} --doctest


mypy-only:
	mypy ${TARGET}
