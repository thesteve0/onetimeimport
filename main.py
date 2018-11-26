import json
import requests
from gbdx_auth import gbdx_auth

from gbdxtools import Interface


file = "./catalogid_whitelist.csv"

catids  = []

with open(file, 'r') as infile:
    for catid in infile:
        catids.append(catid.strip())

json_catids = json.dumps(catids)

gbdx = Interface()

url = "https://rda.geobigdata.io/v1/authorization/addCatalogIdsToOpenDataWhitelist"
payload = json_catids

r = gbdx.gbdx_connection.post(url, json=payload)
print(r.status_code)
print('content: ' + str(r.content))

print('done with ' + str(len(catids)))
    