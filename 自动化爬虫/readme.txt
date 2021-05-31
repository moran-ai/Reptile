自动化爬虫  selenium+chromdriver

定位元素的方法
    find_element 获取满足条件的第一个元素
    find_elements 获取满足条件的所有元素
    find_element_by_id()  通过id定位元素
    find_element_by_name()   通过name定位元素
    find_element_by_class_name() 通过类样式名称定位元素
    find_element_by_tag_name()  通过标签名称定位元素
    find_element_by_link_text()  通过链接定位元素 a标签
    find_element_by_css_selector()  通过CSS定位元素
    find_element_by_xpath()  通过xpath语法定位元素

selenium的行为链
    导入行为链
        from selenium.webdriver.common.action_chains import ActionChains
    创建对象
        actions = ActionChains(driver)
    移动到某个元素
        actions.move_to_element(element)
    文本框填入内容
        actions.send_key_to_element(element, 'python')
    单击
        actions.click(element)

    双击：
        double_click(element)
    右键
        context_click(element)

selenium操作cookie
    1.获取所有cookie信息
        driver.get_cookies()
    2.获取指定的cookie信息
        driver.get_cookie('BAIDU')
    3.添加cookie
        driver.add_cookie({'name': zhangsan, 'value': 80890})
    4.删除cookie
        driver.delte_cookie('zhangsan')
        driver.delte_all_cookies()
