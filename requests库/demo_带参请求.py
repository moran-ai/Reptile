import requests

url = 'https://www.so.com/s'
params = {
    'q': 'python'
}
resp = requests.get(url=url, params=params)
resp.encoding = 'utf-8'
print(resp.text)
