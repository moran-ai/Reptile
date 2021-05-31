import requests
import re

url = 'https://www.qiushibaike.com/video/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
lst = []
info = re.findall('<source src="(.*)" type=\'video/mp4\' />', resp.text)
for item in info:
    i = 'https:' + item
    lst.append(i)

count = 0
for item in lst:
    count += 1
    resp = requests.get(item, headers=headers)
    with open('video/' + str(count) + '.mp4', 'wb') as file:
        file.write(resp.content)
print('视频下载完毕')
