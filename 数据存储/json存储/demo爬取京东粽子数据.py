import csv
import requests
import json

url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1087591&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

resp = requests.get(url=url, headers=headers)
data = resp.text.replace('fetchJSON_comment98(', '').replace(');', '')
data_ = json.loads(data)
data_list = []
for d in data_['comments']:
    content = d['content'].replace('&hellip;', '')
    time = d['referenceTime'].split(' ')[0]
    data_list.append([content, time])

with open('京东销售最好的粽子数据.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['评价', '评价时间'])
    for i in data_list:
        writer.writerow(i)
