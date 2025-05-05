.PHONY: run-dev run-prod run-gunicorn logs install

run-dev:
	python start_app.py

run-prod:
	python start_app.py prod

run-gunicorn:
	gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

logs:
	tail -f logs/app.log

install:
	pip install -r requirements.txt
