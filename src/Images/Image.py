import requests
from random import choice
import pprint

# Get API KEY FOR PEXElS HERE: https://www.pexels.com/api/documentation/
API_KEY_PEXELS = 'API KEY HERE'
PEXELS_HEADER = {"Authorization": API_KEY_PEXELS}
 
WAIFU_HEADER = { "Accept": "application/vnd.api+json",
                 "Content-Type": "application/vnd.api+json"}

#  Get image from pexels
def get_image(query:list):
    url = 'https://api.pexels.com/v1/search?query=' + "%20".join(query) + "&per_page=16&page=1"
    print(url)
    r = requests.get(url, headers=PEXELS_HEADER)

    # Organize data
    photos = r.json().get('photos')
    random_photo = choice(photos)
    random_photo_url = random_photo.get('src').get('original')

    return random_photo_url


def get_waifu(*args):
    url = ''
    r = requests.get(url)