import requests
import json

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = {
    'action': 'query',
    'format': 'json',
    'prop': 'linkshere',
    'pageids': 801662,
    'lhprop': 'pageid|title',
    'lhnamespace': 0,
    'lhlimit': 50,
    'lhcontinue': ''
}

r = requests.get(ENDPOINT, params=parameters)

print(json.loads(r.text))
