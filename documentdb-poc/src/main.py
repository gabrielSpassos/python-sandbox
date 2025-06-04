import os
import pathlib
import uuid

import pymongo
from decouple import config
from pymongo.errors import ConnectionFailure, InvalidURI
from sshtunnel import SSHTunnelForwarder


class DBManager:
    def __init__(self, cluster_name: str, db_connection=None):
        self.cluster_name = cluster_name
        self.mongo_client = self.connect_mongo_client() if db_connection is None else db_connection

    @staticmethod
    def create_ssh_tunnel(port: int, db_uri: str):
        try:
            ec2_url = config("EC2_URL")
            ec2_key_name = config("EC2_KEY_NAME")

            server = SSHTunnelForwarder(
                (ec2_url, 22),
                ssh_username='ubuntu',
                ssh_pkey=os.fspath(pathlib.Path(__file__).parent.parent / ec2_key_name),
                remote_bind_address=(db_uri, port),
                local_bind_address=('127.0.0.1', port)
            )
            server.skip_tunnel_checkup = False
            server.start()
            server.check_tunnels()
            print(f"Tunnel is Up {server.tunnel_is_up}")
            print(f"Local is up {server.local_is_up(('0.0.0.0', port))}")
        except InvalidURI:
            print(f"Invalid MongoDB URI: {db_uri}")

    def connect_mongo_client(self):
        try:
            port = config('DB_PORT', default=27017, cast=int)
            db_uri = config("DB_URI")
            service_env = config("SERVICE_ENV")
            print('Env:', service_env)

            # If env is local replace the db_uri with localhost and use ssh tunnel to connect to AWS
            if config("SERVICE_ENV") == "local":
                self.create_ssh_tunnel(port, db_uri)
                db_uri = "127.0.0.1"

            mongo_client = pymongo.MongoClient(
                host=f"mongodb://{db_uri}:{port}/?tls=true&tlsCAFile=global-bundle.pem",
                port=port,
                username=config("DB_USERNAME"),
                password=config("DB_PASSWORD"),
                tlsCAFile=os.fspath(pathlib.Path(__file__).parent.parent / 'global-bundle.pem'),
                tls=True,
                authMechanism="SCRAM-SHA-1",
                tlsAllowInvalidHostnames=True,
                directConnection=True,
                retryWrites=False,
            )

            return mongo_client
        except ConnectionFailure:
            raise RuntimeError("DocumentDB Server not available")
        except Exception as e:
            raise RuntimeError(e.__str__())

dbManager = DBManager("testpoc")
##Specify the database to be used
db = dbManager.mongo_client.catalog

print(db.name)
print(db.list_collection_names())

print(db.my_collection.insert_one({"x": 10}).inserted_id)

db.products.drop()

product1 = {
  "name": "Product-1",
  "category": "Category-1",
  "value": 100.00,
  "isActive": True
}
db.products.insert_one(product1)

product2 = {
  "name": "Product-2",
  "category": "Category-2",
  "value": 50.00,
  "isActive": False
}
db.products.insert_one(product2)

for p in db.products.find():
  print('Products', p)

##Close the connection
dbManager.mongo_client.close()
