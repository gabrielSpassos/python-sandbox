# Amazon S3 Bucket's POC

* Get local file and send to Amazon S3 Bucket

* Todo List:

- [x] Get files from folder
- [x] Create folder if it isn't existing
- [x] Create file if folder is empty
- [x] Create Amazon S3 client
- [x] Send files to S3 bucket

### Usage

* Install dependencies
```
pip3 install -r requirements.txt
```

* Put [credentials](https://github.com/gabrielSpassos/python-sandbox/blob/master/s3-poc/credentials) file into `~/.aws/credentials`

* Change the values `$change_this_value` into credentials to yours keys

* Maybe you wanna change the profile at [amazon_client](https://github.com/gabrielSpassos/python-sandbox/blob/master/s3-poc/amazon_client.py)

```python
session = boto3.Session(profile_name='$profile')
```

* Change the bucket name at [index](https://github.com/gabrielSpassos/python-sandbox/blob/master/s3-poc/index.py)

```python
bucket_name = 'your_bucket_name'
```
