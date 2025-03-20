# Flask POC

### Usage

* Install
```
pip3 install -r requirements.txt
```

* Run
```
python3 -m flask --app server run
```

* Access the server
```
http://localhost:5000
```

### Requests

* curl -i -H "Content-Type: application/json" -X GET http://localhost:5000 
* curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:5000/hello

### Output
```shell
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000 

HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.10
Date: Thu, 20 Mar 2025 21:30:46 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 43
Connection: close

<p>1cd90601-321d-4223-a830-3cf93e0b38a7</p>%   
```

```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:5000/hello

HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.10
Date: Thu, 20 Mar 2025 21:29:32 GMT
Content-Type: application/json
Content-Length: 72
Connection: close

{"id":"283d52ad-abc6-4ad3-b2db-71af6b456ee5","message":"Hello, World!"}
```

* Server Output:
```shell
{'userId': '1', 'username': 'fizz bizz'}
<Response 38 bytes [200 OK]>
{'id': UUID('a226f633-fed4-4b67-b71b-1ecf91c9e9ba'), 'message': 'Hello, World!'}
<Response 72 bytes [200 OK]>
127.0.0.1 - - [20/Mar/2025 14:30:14] "POST /hello HTTP/1.1" 200 -
127.0.0.1 - - [20/Mar/2025 14:30:46] "GET / HTTP/1.1" 200 -
```
