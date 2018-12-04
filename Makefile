.PHONY: test
.DEFAULT_GOAL :=test

deps:
		pip install -r requirements.txt
		pip install -r test_requirements.txt
   		python -m pip install -U selenium

lint:
		flake8 test

test:
		PYTHONPATH=. py.test Main.py

run:
		python Main.py
