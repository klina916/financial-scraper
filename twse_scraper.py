import requests
import json

response = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20221025&selectType=30&_=1666714015703')

print(response.json()['data'])