clean:
	rm -rf dist/ *.egg-info/ build

test: clean
	python3 -m venv venv
	./venv/bin/pip install --requirement requirements.txt
	./venv/bin/pip install pytest
	./venv/bin/python -m pytest

dist: test
	docker build -t kostz/sketches:canyon-notifier .
	docker push kostz/sketches:canyon-notifier
