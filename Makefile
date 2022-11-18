install:
	pip install -e requirement.txt

test:
	pytest --capture=no -vv

lint:
	make mypy-only && black ./src ./tests && isort ./src ./tests

mypy-only:
	mypy ./src
