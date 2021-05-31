import requests

url = 'https://www.xslou.com/login.php?do=submit'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
data = {
    'username': '454545',
    'password': '5ew53535325',
    'usecookie': '0',
    'action': 'login',
    'submit': '(unable to decode value)'
}
resp = requests.post(url=url, data=data, headers=headers)
resp.encoding = 'gbk'
print(resp.text)
