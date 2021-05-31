from urllib.request import ProxyHandler
from urllib.request import build_opener

url = 'https://www.xslou.com/'
# 设置代理ip
pro = ProxyHandler({"https": '116.25.245.228:4216'})

# 构建一个opener对象
opener = build_opener(pro)

resp = opener.open(url)
print(resp.read().decode('gbk'))
