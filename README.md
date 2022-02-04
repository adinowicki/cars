#Cars app

##Set up

Copy `postgres.env.example` to `postgres.env`, `django.env.example` to `django.env`,
change it as You wish, and run `make`.

##Make rules

`make`

Build Docker containers, migrate and start app.

`make build`

Build Docker containers.

`make migrate`

Migrate database.

`make qa`

Run isort, black and flake8 on project.

`make down`

Bring down Docker containers.
