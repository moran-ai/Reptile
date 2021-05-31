import requests
from bs4 import BeautifulSoup

url = 'https://www.taobao.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'lxml')
a_list = soup.find_all('a')
for a in a_list:
    url = "a.get('href')"
    if url == None:
        continue
    if url.startswith('https') or url.startswith('http'):
        print(url)
