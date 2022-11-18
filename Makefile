install:
	pip install -e requirement.txt

test:
	pytest --capture=no -vv

lint:
	make mypy-only && black ./src && isort ./src

mypy-only:
	mypy ./src
