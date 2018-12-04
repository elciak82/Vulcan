.PHONY: test
.DEFAULT_GOAL :=test

deps:
		pip install -r requirements.txt
		pip install -r test_requirements.txt

env:		
		"$VULCAN_PASSWORD" = password
		"$VULCAN_LOGIN" = loginName
		"$SMTP_LOGIN" = smtpLogin
		"$SMTP_PASSWORD" = smtpPassword
		"$EMAILS_TO_NOTIFY_TEST" = emailsToNotify

lint:
		flake8 test

test:
		python Main.py

run:
		python Main.py
