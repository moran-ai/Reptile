import requests

url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
resp = requests.get(url=url)
# print(resp.content)
with open('logo.png', 'wb') as f:
    f.write(resp.content)