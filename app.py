import datetime
import time

import requests

from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def parser(url):
    launches = []

    res = requests.get(url)
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


class AllLaunches(Resource):
    url = 'https://spaceflightnow.com/launch-schedule/'

    def get(self):
        return parser(self.url)


class TodayLaunches(Resource):
    def get_current_date(self):
        month = time.ctime(datetime.datetime.timestamp(datetime.datetime.now())).rsplit(' ')[1]
        day = time.ctime(datetime.datetime.timestamp(datetime.datetime.now())).rsplit(' ')[3]
        return month + ' ' + day

    url = 'https://spaceflightnow.com/launch-schedule/'

    def get(self):
        today_launches = []

        launches = parser(self.url)
        for launch in launches:
            if self.get_current_date() == launch['date']:
                today_launches.append(launch)

        return today_launches


api.add_resource(AllLaunches, '/api/all')
api.add_resource(TodayLaunches, '/api/today')


@app.errorhandler(404)
def help_links(e):
    return {
        'allLaunches': '/api/all',
        'todayLaunches': 'api/today'
    }


if __name__ == '__main__':
    app.run()
