# Задача 1
import requests
from pprint import pprint


class Superhero:
    def __init__(self, token):
        self.token = token

    def sort_intel(self, superhero_list):
        superhero_dict = {}
        url = 'https://superheroapi.com/api/'
        access_token = self.token + '/'
        get_name = 'search/'
        power = '/powerstats'

        for hero in superhero_list:
            total_url = url + access_token + get_name + hero
            resp = requests.get(total_url)
            id = resp.json()['results'][0]['id']
            total_url = url + access_token + id + power
            resp = requests.get(total_url)
            superhero_dict[resp.json()['intelligence']] = hero
        sorted_keys = sorted(superhero_dict, key=superhero_dict.get,
                             reverse=True)
        print('Сортировка супергероев по уму (по убыванию):')
        for w in sorted_keys:
            print(f'{superhero_dict[w]}, {w}')


if __name__ == '__main__':
    mylist = ['Hulk', 'Captain America', 'Thanos']
    superhero = Superhero('2619421814940190')
    superhero.sort_intel(mylist)