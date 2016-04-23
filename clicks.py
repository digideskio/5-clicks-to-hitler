import http.client
import json


conn = http.client.HTTPSConnection("en.wikipedia.org")

headers = {
    'cache-control': "no-cache",
}

conn.request("GET", "/w/api.php?action=query&format=json&prop=linkshere&pageids=801662&lhprop=pageid%7Ctitle&lhnamespace=0&lhlimit=50&lhcontinue=", headers=headers)

res = conn.getresponse()

data = res.read().decode("utf-8")

print(json.loads(data))
