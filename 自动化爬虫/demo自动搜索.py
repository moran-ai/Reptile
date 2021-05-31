import time
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('https://cn.bing.com/')

# 获取网页元素
input_tag = chrome.find_element_by_id('sb_form_q')
input_tag.send_keys('python')

# 获取按钮
submit = chrome.find_element_by_id('sb_form_go')
submit.click()
print(chrome.page_source)

time.sleep(5)
chrome.quit()