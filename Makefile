all: build migrate
	docker-compose run --rm --service-ports web ./manage.py runserver 0.0.0.0:8000

build:
	docker-compose build

migrate:
	docker-compose run --rm -T --service-ports  web ./manage.py migrate

qa:
	docker-compose run --rm -T web isort --skip=.git --skip=venv .
	docker-compose run --rm -T web black .
	docker-compose run --rm -T web flake8 .

test:
	docker-compose run --rm -T web ./manage.py test

down:
	docker-compose down
