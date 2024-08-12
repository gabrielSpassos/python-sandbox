from flask import Flask
import time

app = Flask(__name__)

@app.route("/v1/person")
def getPerson():
    person = {
        'firstName': 'Gabriel',
        'lastName': 'Passos',
        'birthDate': '1990-01-01'
    }
    time.sleep(180)
    return person

@app.route("/v1/person", methods = ['POST'])
def createPerson():
    person = {
        'firstName': 'Gabriel',
        'lastName': 'Passos',
        'birthDate': '1990-01-01'
    }
    time.sleep(180)
    return person
