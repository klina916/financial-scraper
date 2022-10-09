from wsgiref import headers
import requests
import json

url = 'https://mis.taifex.com.tw/futures/api/getQuoteList'

payload ={
    "MarketType":"0",
    "SymbolType":"F",
    "KindID":"1",
    "CID":"TXF",
    "ExpireMonth":"",
    "RowSize":"全部",
    "PageNo":"",
    "SortColumn":"",
    "AscDesc":"A"
}

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.post(url, data = json.dumps(payload), headers=headers)

print(response.json()['RtData']['QuoteList'])