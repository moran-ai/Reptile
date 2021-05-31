"""
urllib.request() 发送http请求
"""
import urllib.request

url = 'http://www.zongheng.com/'

# 发送请求
resp = urllib.request.urlopen(url=url)
html = resp.read().decode('utf-8')
print(html)
