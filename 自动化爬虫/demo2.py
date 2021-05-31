import time

from selenium import webdriver

chrome = webdriver.Chrome()

# 请求的url
chrome.get('https://www.baidu.com/')

time.sleep(5)

# 关闭当前页
chrome.close()
time.sleep(5)
chrome.quit()