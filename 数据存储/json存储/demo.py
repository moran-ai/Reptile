import json

# 将字符串转为对象
data = ' {"name": "asdf"}'
d = json.loads(data)
print(d)

# 将对象转为字符串
# data_ = ' {"name": "asdf"}'
da = json.dumps(d, ensure_ascii=False)
print(da)

# 把(dict)存在保存到文件中
json.dump(d, open('movie.txt', 'w',encoding='utf-8'), ensure_ascii=False)
