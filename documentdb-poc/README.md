# AWS Document DB POC

- 

### Usage

* Install
```
pip3 install -r requirements.txt
```

* Download global-bundle.pem and place it on the root folder of this project
```
wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

* Create ubuntu EC2 instance, put the ssh .pem file inside the the root folder of this project

* Create .env file and fill with the info
```
SERVICE_ENV= "local"
DB_USERNAME = "********"
DB_PASSWORD = "********"
DB_URI = "********.us-east-1.docdb.amazonaws.com"
DB_PORT = 27017
EC2_URL = "**********.compute-1.amazonaws.com"
EC2_KEY_NAME = "********"
```

* Run
```
python3 src/main.py
```