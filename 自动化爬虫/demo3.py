from selenium import webdriver

chrome = webdriver.Chrome()

# 请求的url
chrome.get('https://cn.bing.com/')

# 定位元素 通过id
# input_tag = chrome.find_element_by_id('sb_form_q')

# 通过name定位元素
# input_tag = chrome.find_element_by_name('q')

# 通过类样式定位元素
# input_tag = chrome.find_element_by_class_name('b_searchbox')

#通过标签名定位元素
# input_tag = chrome.find_element_by_tag_name('input')

# 输入关键字
# input_tag.send_keys('python')
# inp_tag = chrome.find_element_by_class_name('b_searchboxSubmit')
# inp_tag.click()

# 根据链接文本定位元素
# a_tag = chrome.find_element_by_link_text('地图')
# a_tag.click()

# 通过CSS样式获取id
input_tag = chrome.find_element_by_css_selector('#sb_form_q')

# 通过CSS样式获取id
input_tag = chrome.find_element_by_css_selector('.b_searchbox')
# input_tag.send_keys('python')

# 通过Xpath语法获取
input_tag_xpath = chrome.find_element_by_xpath('//input[@class="b_searchbox"]')
input_tag_xpath.send_keys('python')