import requests
import openpyxl
import re

url = 'https://www.xiachufang.com/category/40076/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)

data = []
# 获取家常菜的名字
names = re.findall('<p.*?class="name">.*?<a.*?>(.*?)</a>.*?</p>', resp.text, re.S)
for name in names[3:]:
    n = name.replace(' ', '').replace('\n', '').strip().replace('<spanclass="ellipsis-line-2">', '').replace('</span>',
                                                                                                             '')
    # data.append(n)

# 获取食材
shicai = re.findall('<p.*?class="ing ellipsis">(.*?)</p>', resp.text, re.S)
for s in shicai:
    s_ = s.replace('<span>', '').replace('</span>', '')
    # print(s_)
    ss_ = re.findall('<a.*?>(.*?)</a>', s_)
    # print(ss_)
    # data.append(ss_)

# 获取菜品的链接
food_url = re.findall('<p.*?class="name">.*?<a.*?href=(".*?").*?>', resp.text, re.S)
for url in food_url[:-1]:
    u = 'https://www.xiachufang.com' + url.replace('"', '')
    # data.append(u)

coint = 0
for i in range(len(names)):
    name = names[i].replace(' ', '').replace('\n', '').strip().replace('<spanclass="ellipsis-line-2">', '').replace(
        '</span>', '')
    try:
        n = ','.join(re.findall('<a.*?>(.*?)</a>', shicai[i].replace('<span>', '').replace('</span>', '')))
    except:
        n = None
    url = 'https://www.xiachufang.com' + food_url[i].replace('"', '')
    data.append([coint, name, n, url])
    coint += 1
for _ in data:
    print(_)
