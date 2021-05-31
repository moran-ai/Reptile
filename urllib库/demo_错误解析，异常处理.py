import urllib.request
import urllib.error

# url = 'http://www.google.com'
# url = 'http://www.google.cn'
# try:
#     resp = urllib.request.urlopen(url)
# except urllib.error.URLError as e:
#     print(e.reason)

url = 'https://www.douban.com/'

try:
    resp = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print('错误原因:', e.reason)
    print('响应状态码:', e.code)
    print('响应数据：', e.headers)
