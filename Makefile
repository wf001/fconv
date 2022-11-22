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


publish:
	make clean &&\
		make check &&\
		python setup.py sdist bdist_wheel &&\
		twine upload --repository testpypi dist/*


clean:
	rm -rf dist build *.egg-info
