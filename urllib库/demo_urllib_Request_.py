"""
urllib发送Requst请求
"""
import urllib.request
from http import cookiejar

url = 'https://www.douban.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# 构建请求对象
req = urllib.request.Request(url=url, headers=headers)

# 发送请求
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))
