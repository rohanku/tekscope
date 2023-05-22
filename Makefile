.PHONY: format

format:
	black .

test:
	python3 -m pytest --doctest-modules -s -v

lint:
	python3 -m pylint ./tekscope
	python3 -m pylint ./tests

