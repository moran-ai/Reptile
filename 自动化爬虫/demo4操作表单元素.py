import time

from selenium import webdriver

chrome = webdriver.Chrome()

# chrome.get('https://www.douban.com/')
# 指定url
chrome.get('https://login.51job.com/login.php?loginway=1')

# 操作表单元素
# input_tag=chrome.find_element_by_class_name('s_ipt')
# input_tag.send_keys('python')

# 操作表单元素，复选框
check_box = chrome.find_element_by_class_name('check')
check_box.click()
time.sleep(5)
chrome.quit()
