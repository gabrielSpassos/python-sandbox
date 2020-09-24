# Basic Django Rest Api

* Using [Django Rest Framework](https://www.django-rest-framework.org/)

#### Install application

* Install Dependencies
```shell script
pip3 install -r requeriments.txt
```

#### Start/Create Project

* Create project 
```shell script
django-admin startproject $project_name
```

* Start app
```shell script
python3 manage.py startapp $application_name
```

* Execute migration
```shell script
python3 manage.py migrate
```

* Apply code migrations
```shell script
python3 manage.py makemigrations
```

* Clean database
```shell script
python3 manage.py flush
```

* Start server
```shell script
python3 manage.py runserver
```

#### Usage

[Swagger UI](http://localhost:8000/swagger/)

__or__

```shell script
curl --location --request POST 'http://localhost:8000/o/token/' \
--header 'content-type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=65ZBBuuDC0kpXvKAWbmN7Q042m2NNl8Lavo65Thd' \
--data-urlencode 'client_secret=6DppUQhKBoLtNGp8Z2UASgLgbHqkCMq809gGP3WyQzK8idIOjfPm6DZN6UP9MkpNVkqvUN1wb69lY9hn90QZtOFn2yfri2ZbGewWWp7Nq5whnTYc6Py7YiLvzQ7NVCQq' \
--data-urlencode 'username=gabriel' \
--data-urlencode 'password=senha123'
```

```shell script
curl --location --request GET 'http://localhost:8000/musics/' \
--header 'Authorization: Bearer bLoZXuQOhgtgUYNztHHC0j2Vc2wcJc'
```

__or__

import [postman collection](https://github.com/gabrielSpassos/python-sandbox/blob/master/basic_django_rest_api/Python%20Basic%20Django%20App.postman_collection.json)