import urllib.request
import urllib.parse

url = 'https://www.xslou.com/login.php'
data = {
    'username': 'fdsfsaf',
    'password': 'fsfsfsfsf',
    'action': 'login'
}

# data = urllib.parse.urlencode(data).encode('utf-8')

# 发送post请求
resp = urllib.request.urlopen(url=url, data=bytes(urllib.parse.urlencode(data), encoding='utf-8'))
html = resp.read().decode('gbk')
print(html)
