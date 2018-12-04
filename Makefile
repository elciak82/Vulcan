.PHONY: test
.DEFAULT_GOAL :=test

deps:
		pip install -r requirements.txt
		pip install -r test_requirements.txt

env:		
		VULCAN_PASSWORD
		VULCAN_LOGIN
		SMTP_LOGIN
		SMTP_PASSWORD
		MAILS_TO_NOTIFY_TEST

lint:
		flake8 test

test:
		python Main.py

run:
		python Main.py
