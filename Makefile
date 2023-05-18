.PHONY: format

format:
	black .

test:
	python3 -m pytest tests -s

lint:
	python3 -m pylint ./tektronix_oscilloscope
	python3 -m pylint ./tests

