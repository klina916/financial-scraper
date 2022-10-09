import requests
import json

response = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20221007&selectType=24&_=1665281083382')

print(response.json()['data'])