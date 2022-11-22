TARGET = ./fconv ./tests

install:
	pip install -r requirement.txt -r dev-requirement.txt

install-dev:
	make install &&\
	pip install --editable .

check:
	make test && \
		make lint

ci:
	make test && \
		black ${TARGET} --check && \
		isort ${TARGET} --check && \
		flake8 ${TARGET}

test:
	pytest --capture=no -vv

lint:
	make mypy-only && \
		black ${TARGET} && \
		isort ${TARGET} && \
		flake8 ${TARGET}

mypy-only:
	mypy ${TARGET}

build:
	pip install wheel twine &&\
	make clean &&\
		make check &&\
		python setup.py sdist bdist_wheel


publish-dev:
	make build &&\
		twine upload --repository testpypi dist/*

publish:
	make build &&\
		twine upload --repository pypi dist/*

clean:
	rm -rf dist build *.egg-info
