Project "Teams and Participants".

This is a REST API implementation using Django. API documentation is available at localhost:8000/swagger.
The application has two main endpoints: /teams and /participants. Access rights are implemented here - all CRUD actions are available to the admin. An authorized user can only read information.

The postgres database is used with DEBUG=True and otherwise database is sqlite. There are two main entities in the database - Team and Participant. There is a one-to-many relationship between them.
Participant is necessarily tied to Team. In turn, a Team may not have participants.

It also implements a CI element with automatic code checking - flake8 and unit tests.

To run the project use the following commands:

Install requirements:
```shell
pip install requirements.txt
```
Run migrations:
```shell
python manage.py migrate
```
Run server:
```shell
python manage.py runserver
```

Or you can use docker's commands:

Build:
```shell
docker compose build
```
Run:
```shell
docker compose up
```