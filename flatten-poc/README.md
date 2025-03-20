# Flat List POC

### Usage

* Install dependencies
```shell
pip3 install -r requirements.txt
```

* Run
```shell
python3 src/main.py
```

### Output

```shell
List of list:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Numpy array of list of list:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Numpy flatten of list of list:
[1 2 3 4 5 6 7 8 9]

Numpy flatten to list of list of list:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

List of dictionaries:
[{'id': 1, 'foo': 'bar'}, {'id': 2, 'foo': 'bar'}, {'id': 3, 'foo': 'bar'}, {'id': 4, 'foo': 'bar'}, {'id': 5, 'foo': 'bar'}, {'id': 6, 'foo': 'bar'}, {'id': 7, 'foo': 'bar'}, {'id': 8, 'foo': 'bar'}, {'id': 9, 'foo': 'bar'}]

Other list of dictionaries:
[{'my_custom_id': 1, 'my_custom_name': 'gabriel'}, {'my_custom_id': 2, 'my_custom_name': 'john'}, {'my_custom_id': 3, 'my_custom_name': 'mike'}]
```