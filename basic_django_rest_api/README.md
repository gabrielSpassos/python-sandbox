# Basic Django Rest Api

* Using [Django Rest Framework](https://www.django-rest-framework.org/)

#### Install application

* Install Django Rest Framework
```shell script
pip3 install djangorestframework
```

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

* Start server
```shell script
python3 manage.py runserver
```

#### Usage

* [local](http://localhost:8000/musics)

__or__

```shell script
curl -X POST http://127.0.0.1:8000/musics/ -H 'content-type: application/json' -d '{"title": "Music name", "seconds": 400}'
```

```shell script
curl -X GET http://127.0.0.1:8000/musics/ -H 'Aceppt: application/json'
```