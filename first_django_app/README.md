### Installation 

* Install Django
```
python3 -m pip install Django
```

### Usage

* Run server
```
python3 manage.py runserver
```
[Index](http://localhost:8000/)

[Basic template](http://localhost:8000/polls)

---

* Run tests
```
python3 manage.py test polls
```

* Create tables at database
```
python3 manage.py migrate
```

* Create polls tables
```
python3 manage.py makemigrations polls
```

* Check sql script
```
python3 manage.py sqlmigrate polls 0001
```

* Run migration
```
python3 manage.py migrate
```
---

* Create admin user
```
python3 manage.py createsuperuser
```

* [Admin page](http://localhost:8000/admin)