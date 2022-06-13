import requests
from pprint import pprint
import os

# Задача 3
import time
from datetime import datetime, timedelta
today = datetime.today()

class Stackoverflow:

    def find_questions(self, length):

        url = 'https://api.stackexchange.com/2.3/questions'
        params3 = {'fromdate': (today.date() - timedelta(days=2)), 'tagged': 'Python',
                   'site': 'stackoverflow', 'pagesize': '100', 'sort': 'votes',
                   'page': '1'}
        resp3 = requests.get(url, params=params3)
        finlist = resp3.json()['items']

        count = 1 + (length // 100)
        while resp3.json()['has_more'] == True and count > 1:
            count -= 1
            params3 = {'fromdate': (today.date() - timedelta(days=2)),
                       'todate': today.date(), 'tagged': 'Python',
                       'site': 'stackoverflow', 'pagesize': '100', 'sort': 'votes',
                       'page': count}
            resp3 = requests.get(url, params=params3)
            #На случай необходимости отслеживания скана
            #print(f'Страница номер {count + 1}')
            for i in resp3.json()['items']:
              finlist.append(i)

        for i in range(length):
            print(finlist[i]["link"])
        return

if __name__ == '__main__':
    data = Stackoverflow()
    how_many_qs = int(input('Введите количество вопросов, которое хотите увидеть'))
    data.find_questions(how_many_qs)