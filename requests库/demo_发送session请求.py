import requests

url = 'https://www.xslou.com/login.php?do=submit'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
data = {
    'username': 'handjiao',
    'password': 'cai201314',
    'usecookie': '0',
    'action': 'login',
    'submit': '(unable to decode value)'
}

# 发送session请求
session = requests.session()
resp = session.post(url=url, data=data, headers=headers)
resp.encoding = 'gbk'
# print(resp.text)

host_url = 'https://www.xslou.com/modules/article/uservote.php?id=5'
resp1 = session.get(host_url)
resp1.encoding = 'gbk'
print(resp1.text)
