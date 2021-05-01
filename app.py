import requests

from flask import Flask, abort, request
from flask_restful import Api, Resource

from bs4 import BeautifulSoup


app = Flask(__name__)
api = Api(app)


class AllLaunches(Resource):
    url = 'https://spaceflightnow.com/launch-schedule/'

    def get(self):
        launches = []

        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        datename_classes = soup.find_all('div', class_='datename')
        for dc in datename_classes:
            launch = {
                'mission': dc.find('span', class_='mission').text.rsplit(' • ')[1],
                'launchVehicle': dc.find('span', class_='mission').text.rsplit(' • ')[0],
                'date': dc.find('span', class_='launchdate').text
            }

            launches.append(launch)

        return launches


api.add_resource(AllLaunches, '/api/all')


if __name__ == '__main__':
    app.run()
