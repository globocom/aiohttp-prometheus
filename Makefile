clean:
	@find . -iname '*.pyc' -delete
	@rm -rf *.egg-info dist

test: clean
	@coverage run --branch `which pytest` tests/
	@coverage report -m
	@flake8 aiohttp_prometheus tests

setup:
	@pip install -U -e .\[tests\]
