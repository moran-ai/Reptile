import urllib.request

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
#  构建请求对象
resp = urllib.request.Request(url=url, headers=headers)

# 获取opener对象
opener = urllib.request.build_opener()

# 发送请求
resp = opener.open(resp)

print(resp.read().decode('utf-8'))
