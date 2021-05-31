import urllib.parse

# urllib.parse 用于解析url
# 编码
kw = {'wd': '还'}
data = urllib.parse.urlencode(kw)
print(data)

# 解码
d = urllib.parse.unquote(data)
print(d)
