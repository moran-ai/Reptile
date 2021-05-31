import time
from selenium import  webdriver
from selenium.webdriver.support.ui import Select  # 下拉列表框

chrome = webdriver.Chrome()
chrome.get('https://kyfw.12306.cn/otn/regist/init')

# 获取下拉列表框对象
select = Select(chrome.find_element_by_id('cardType'))

# 获取下拉列表中的项
# ① 根据索引获取数据
# select.select_by_index(1)
# ② 根据Value属性获取
#select.select_by_value('B')
# 根据可见文本
select.select_by_visible_text('台湾居民来往大陆通行证')
time.sleep(5)
chrome.quit()
