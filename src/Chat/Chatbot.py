import requests
import json
from string import ascii_lowercase, digits
from os import getcwd
from random import choice

# GET API Key, website : https://brainshop.ai/
# GLOBAL variables
API_KEY = 'API KEY HERE'
ID_LIST = dict()
PATH = getcwd() + '/src/Chat'
ALL_CHARS = list(ascii_lowercase + digits)
ACTIVE_USERS_ID = list()
URL = str()

# Read file and look for saved IDs
with open('{}/ID_LIST.json'.format(PATH), 'r') as file:
    ID_LIST = json.loads(file.read())

SAVED_ID = [id[1] for id in ID_LIST.items()]
SAVED_USERNAME = [id[0] for id in ID_LIST.items()]

# Function to generate id
def generateId():
    new_id = str()
    for x in range(3):
        new_id += choice(ALL_CHARS)
    if new_id in SAVED_ID:
        generateId()
    else:
        ACTIVE_USERS_ID.append(new_id)
        return new_id

# Save ID_LIST to save logged
def saveID(userDiscordId):
    global ID_LIST
    ID_LIST[userDiscordId] = generateId()
    COPY = ID_LIST
    with open('{}/ID_LIST.json'.format(PATH), 'w') as file:
        file.write(json.dumps(COPY))
    with open('{}/ID_LIST.json'.format(PATH), 'r') as file:
        ID_LIST = json.loads(file.read())

# Check
def checkID(userDiscordId):
    if userDiscordId not in SAVED_USERNAME:
        saveID(userDiscordId)

# Main function
def getResponse(userDiscordId, message):
    checkID(userDiscordId)
    global URL
    global API_KEY
    URL = 'http://api.brainshop.ai/get?bid=163751&key={}&uid={}&msg={}'.format(API_KEY, ID_LIST.get(userDiscordId), "%20".join(message))
    r = requests.get(URL)
    return r.json()["cnt"]
