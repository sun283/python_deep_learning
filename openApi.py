#1. Open API
# 실시간 영업소간 통행시간
# Request Url : http://data.ex.co.kr/openapi/trtm/realUnitTrtm

import requests
# Need to get new one
key = ''

type = 'json'
# 101 서울, 103 신갈
StartUnitCode = '101'
EndUnitCode = '103'
# Request URL
URL = 'http://data.ex.co.kr/openapi/trtm/realUnitTrtm?key='
url = URL + key + '&type=json&iStartUnitCode=' + StartUnitCode + '&iEndUnitCode=' + EndUnitCode

response = requests.get(url)
print(response)

json = response.json()
print(json)

cars = json['realUnitTrtmVO']
print(cars)

records = []
for car in cars:
  dic = {}
  dic['date'] = car['stdDate']
  dic['time'] = car['stdTime']
  dic['type'] = car['tcsCarTypeDivName']
  records.append(dic)
print(records)
