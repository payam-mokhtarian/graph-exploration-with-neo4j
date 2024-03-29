# -*- coding: utf-8 -*-
"""graph_api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16fjPi3Qu6ikQgrmGmvHL9aoPtowOGDlH
"""

import requests
import json

HOST = ''
PORT = '7474'
ENDPOINT = '/db/neo4j/tx'
USER = 'neo4j'
PWD = ''

url = HOST+':'+PORT+ENDPOINT
print(url)

body = {
  "statements" : [ {
    "statement" : "MATCH (c:Country) RETURN c.name AS country"
  } ]
}

response = requests.post(url,
                         auth = (USER, PWD),
                         json=body)

data = response.json()
data['results']
