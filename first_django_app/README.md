### Usage

* Run server
```
python manage.py runserver
```
[Index](http://localhost:8000/)

[Basic template](http://localhost:8000/polls)

---


* Create tables at database
```
python manage.py migrate
```

* Create polls tables
```
python manage.py makemigrations polls
```

* Check sql script
```
python manage.py sqlmigrate polls 0001
```

* Run migration
```
python manage.py migrate
```
---

* Create admin user
```
python manage.py createsuperuser
```

* [Admin page](http://localhost:8000/admin)