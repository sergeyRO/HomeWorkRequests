import requests
from pprint import pprint

def intelligence(token,list):
    intelligence = {}
    for name in list:
        url = 'https://superheroapi.com/api/'+token
        hero_id = requests.get(url+'/search/'+name).json()['results'][0]['id']
        intelligence_hero = requests.get(url+'/'+hero_id+'/powerstats').json()['intelligence']
        intelligence[name] = int(intelligence_hero)
    print(intelligence)
    name_hero = ''
    intellect_hero = 0
    for key, val in intelligence.items():
        if intellect_hero < val:
            name_hero = key
            intellect_hero = val
    return f'Самый умный герой из списка {name_hero} ({intellect_hero})'


if __name__ == '__main__':

    TOKEN = '2619421814940190'
    list = ['Batman', 'Captain America', 'Hulk', 'Thanos']
    print(intelligence(TOKEN, list))