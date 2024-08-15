FLASK_ENV ?= development

.PHONY: setup-env dependencies database start-app run-tests coverage

setup-env:
	python -m venv venv
	source venv/bin/activate

dependencies:
	source venv/bin/activate && \
	pip install -r requirements.txt

database:
	source venv/bin/activate && \
	python manage.py db init && \
	python manage.py db migrate && \
	python manage.py db upgrade

start-app:
	source venv/bin/activate && \
	FLASK_ENV=$(FLASK_ENV) python manage.py run

run-tests:
	source venv/bin/activate && \
	python manage.py test

coverage:
	source venv/bin/activate && \
	pytest --cov=app ./app/test