install:
	pip install -e requirement.txt

test:
	pytest --capture=no -vv

lint:
	mypy ./src && black ./src
