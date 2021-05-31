from pyquery import PyQuery as pq

doc = pq('https://www.baidu.com/', encoding='utf-8')
print(doc('title'))
