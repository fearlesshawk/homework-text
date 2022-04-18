import requests

def serch_hero_id_intell(name_list):
    dictonary = {}
    for name in name_list:
        hero = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name).json()
        id = hero['results'][0]['id']
        hero = requests.get('https://superheroapi.com/api/2619421814940190/' + id).json()
        intelligence = hero['powerstats']['intelligence']
        dictonary.setdefault(name)
        dictonary[name] = {'id' : id, 'intelligence' : intelligence}
    return dictonary

def sort(dictonary):
    dictonary2 = {}
    sorted_keys = []
    for name in dictonary.keys():
        dictonary2.setdefault(name)
        dictonary2[name] = int(dictonary[name]['intelligence'])
    sorted_keys = sorted(dictonary2, key = dictonary2.get, reverse=True)
    return print('Наибольший интеллект у персонажа:', sorted_keys[0], '=', dictonary2[sorted_keys[0]])

name_list = ['Hulk', 'Captain America', 'Thanos']
dictonary = serch_hero_id_intell(name_list)
sort(dictonary)
