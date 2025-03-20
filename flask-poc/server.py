from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_index_route():
    myuuid = uuid.uuid4()
    return "<p>" + str(myuuid) + "</p>"


@app.route('/hello', methods=['POST']) 
def hello():
    data = request.json
    print(data)
    json_data = jsonify(data)
    print(json_data)
    response = {
        "id": uuid.uuid4(),
        "message": "Hello, World!"
    }
    print(response)
    json_response = jsonify(response)
    print(json_response)
    return json_response
