from random import choice
import json


def find_random():
    with open('/home/ianchu0317/Discord-bot/src/Random/random-facts.json', 'r') as file:
        data = file.read()
    return choice(json.loads(data).get('facts'))
