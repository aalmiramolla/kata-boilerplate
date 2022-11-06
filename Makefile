lint:
	flake8 app tests
	black --check app tests
	isort --check-only app tests
	mypy app tests


test:
	pytest --cov
