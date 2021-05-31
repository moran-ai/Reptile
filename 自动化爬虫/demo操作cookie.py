from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

# 获取所有的cookie信息
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

print('-------------------------------------')

# 获取指定的cookie
cooie = driver.get_cookie('BAIDUID')
print(cooie)

# 添加cookie
driver.add_cookie({'name': 'zhangsan', 'value': '000000'})
print('**********************************')
for item in driver.get_cookies():
    print(item)

# 删除指定的cookie
driver.get_cookies('zhangsan')
driver.delete_cookie('zhansan')

# 删除所有的cookie
driver.delete_all_cookies()  # 删除浏览器端的所有cookie信息
