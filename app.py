import requests

from flask import Flask, abort, request
from flask_restful import Api, Resource

from bs4 import BeautifulSoup


app = Flask(__name__)
api = Api(app)


def scrapper(url):
    launches = []

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    datename_classes = soup.find_all('div', class_='datename')
    for dc in datename_classes:
        launch = {
            "mission": dc.find('span', class_='mission').text,
            "date": dc.find('span', class_='launchdate').text
        }

        launches.append(launch)

    return launches


class AllLaunches(Resource):
    def get(self):
        return scrapper('https://spaceflightnow.com/launch-schedule/')


api.add_resource(AllLaunches, '/api/all')


if __name__ == '__main__':
    app.run()
