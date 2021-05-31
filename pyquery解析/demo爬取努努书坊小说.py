import requests
from pyquery import PyQuery as pq

url = 'http://www.huaxiaci.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
# print(resp.text)

doc = pq(resp.text)

#  小说名
title = doc('span.s2 a')
titles = [tite.text for tite in title]

# 章节名
article = doc('span.s3 a')
article = [tite.text for tite in article]
# print(article)

# 作者
author = doc('span.s4')
authors = [a.text for a in author]
# print(authors)

# 时间
time = doc('span.s5')
times = [t.text for t in time]
# print(times)

