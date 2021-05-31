"""
不带参数的请求
"""
import requests

url = 'https://www.baidu.com/'

resp = requests.get(url=url)

resp.encoding = 'utf-8'
cookie = resp.cookies
headers = resp.headers

print('响应的状态码：', resp.status_code)
print('响应的cookie', cookie)
print('响应的请求头', headers)
print('响应的内容', resp.text)