# Amazon EC2 POC

* Todo List:

- [ ] List ec2 instances from AWS 

### Usage

* Install dependencies
```
pip3 install -r requirements.txt
```

* Put [credentials](https://github.com/gabrielSpassos/python-sandbox/blob/master/ec2-poc/credentials) file into `~/.aws/credentials`

* Change the values `$change_this_value` into credentials to yours keys

* Maybe you wanna change the profile at [amazon_client](https://github.com/gabrielSpassos/python-sandbox/blob/master/ec2-poc/amazon_client.py)

```python
session = boto3.Session(profile_name='$profile')
```

* Just run
```
python3 index.py
```
