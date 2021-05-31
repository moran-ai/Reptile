import re

s = 'I study Python3.8 every day'
print('------------match正则方法，从起始位置进行匹配-------------')
print(re.match('I', s).group())
print(re.match('\w', s).group())
print(re.match('.', s).group())

print('-------------search正则方法，从任意位置开始匹配，匹配第一个-----------')
print(re.search('study', s).group())
print(re.search('s\w', s).group())
# print(re.search())

print('--------------findall方法，从任意位置开始匹配，匹配多个----------------')
print(re.findall('y', s))
print(re.findall('Python3.8', s))
print(re.findall('P\w+.\d', s))
print(re.findall('P.+\d', s))

print('---------------sub方法的使用,用于替换---------------------------')
print(re.sub('study', 'like', s))
print(re.sub('s\w+', 'like', s))

