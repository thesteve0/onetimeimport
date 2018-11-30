import json
import requests
from gbdx_auth import gbdx_auth

from gbdxtools import Interface


file = "./catalogid_whitelist.csv"

catids  = []

with open(file, 'r') as infile:
    for catid in infile:
        catids.append(catid.strip())

gbdx = Interface()

url = "https://rda.geobigdata.io/v1/authorization/addCatalogIdsToOpenDataWhitelist"
payload = catids

r = gbdx.gbdx_connection.post(url, json=payload)
print(r.json)
print(r.status_code)
print('content: ' + str(r.content))

print('done with ' + str(len(catids)))
    