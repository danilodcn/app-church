RUNNER = poetry run

test:
	${RUNNER} python -m pytest --workers 2 --tests-per-worker auto -v -s