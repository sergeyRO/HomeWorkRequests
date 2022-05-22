import requests
from pprint import pprint
from datetime import timedelta, date

class Stackoverflow():

    def questions(self, data_start, data_end):
        url = 'https://api.stackexchange.com/'
        params = {'fromdate': data_start, 'min': data_end, 'tagged': 'Python', 'site': 'stackoverflow'}
        response = requests.get(url+'/2.3/questions', params=params)
        for item in response.json()['items']:
            print(item['title'])



if __name__ == '__main__':

    unit = Stackoverflow()
    date_end = date.today()
    date_start = date.today() - timedelta(days=2)
    unit.questions(date_start, date_end)
