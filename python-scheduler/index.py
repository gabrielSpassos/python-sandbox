#!/usr/bin/python

from datetime import datetime
import schedule
import time
import requests

API_ENDPOINT_SWAPI_STARTSHIPS = "https://swapi.co/api/starships/"
START_STARSHIP_ID = 0


def task():
    print('Datetime:', datetime.now())
    print('### Request ###')
    print(get_star_wars_starship(get_starship_id()))


def get_star_wars_starship(starship_id):
    response = requests.get(url = buildUrl(starship_id))
    if(response.status_code == 200):
        return response.json()
    return "Error status: " + str(response.status_code)


def get_starship_id():
    global START_STARSHIP_ID
    START_STARSHIP_ID += 1
    return START_STARSHIP_ID


def buildUrl(starship_id):
    url = API_ENDPOINT_SWAPI_STARTSHIPS + str(starship_id)
    print('Request to url:', url)
    return url


schedule.every().minute.at(":21").do(task)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
