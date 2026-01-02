# Websocket Broadcast POC

POC to test websockets lib with multiple clients

### Usage

* Configure venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

* Install dependencies

```bash
pip3 install -r requirements.txt
```

* Run server
```bash
python3 src/server.py
```

* Run individually client
```bash
python3 src/client.py
```

* Run multiple clients
```bash
./run-clients.sh
```

* Deactivate venv
```bash
deactivate
```