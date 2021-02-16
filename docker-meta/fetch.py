import requests
import json
import sys
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client.testDB
data = json.loads(requests.get(f'https://hub.docker.com/v2/repositories/{sys.argv[1]}/tags').text)
tag_archs = {}
for tag in data['results']:
    archs = []
    for image in tag['images']:
        if image['architecture'] not in archs:
            archs.append(image['architecture'])
    tag_archs[tag['name']] = archs
print(tag_archs)
for x in db.images.find({"image":sys.argv[1]}):
    print(x)
    features = x['platform']['cpu']['features']
    hardware = x['platform']['hardware']
for item in features:
    for x in db.passthru.find({"platform": item}):
        print(x)
for item in hardware:
    for x in db.passthru.find({"platform": item}):
        print(x)
