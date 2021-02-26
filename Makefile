compile:
	python -m compileall .

qb:
	python quickbelat.py

test:
	python -m pytest tests/

testcov:
	python -m pytest tests/ --cov=belat

req:
	python -m pip install -r ./requirements.txt

install:
	make req
	make compile
