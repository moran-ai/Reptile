import requests
from pyquery import PyQuery as pq

url = 'https://www.qidian.com/rank/yuepiao'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
print(resp.text)
