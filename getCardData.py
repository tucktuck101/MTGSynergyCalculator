import requests
import os
import json
dataUpdated = datalastUpdated.txt

def getLastUpdatedDate():
    if os.path.exsists

response = requests.get("https://api.scryfall.com/bulk-data")
bulkData = response.json()
##print(bulkData)
for file in bulkData["data"]