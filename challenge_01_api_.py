# -*- coding: utf-8 -*-
"""챌린지 과제 1 (api 파싱).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pQf7xsXXNITW4dm9nQ92IH0PeZUokdq7
"""

import requests
import pandas as pd
import xml.etree.ElementTree as ET
from google.colab import userdata


url = "http://api.kcisa.kr/openapi/API_CCA_149/request"

params = {
    "serviceKey": userdata.get('serviceKey'),
    "pageNo": "1",
    "numOfRows": "10",
    "resultType" : "xml"
    }

response = requests.get(url, params)
response

root = ET.fromstring(response.text)

row_dict = {}

for i in root.findall('./body/items/item'):
  for j in i:
    #키가 존재하지 않으면 동적으로 추가
    if j.tag not in row_dict:
      row_dict[j.tag] = []
    row_dict[j.tag].append(j.text)

df = pd.DataFrame(row_dict)
df.head()

