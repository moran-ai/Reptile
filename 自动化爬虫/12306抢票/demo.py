import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  # 显示等待的条件
from selenium.webdriver.common.by import By

# 创建浏览器对象
driver = webdriver.Chrome()


class TranSpider():
    # 登录网址
    login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
    # 个人中心的网址
    profiel_url = 'https://kyfw.12306.cn/otn/view/index.html'
    # 余票查询网址
    leftTicket = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'

    def __init__(self, from_station, to_station, train_date):
        """
        :param from_station:   出发地
        :param to_station:     目的地
        :param train_date:     出发时间
        """
        self.from_station = from_station
        self.to_station = to_station
        self.train_date = train_date
        self.station_code = self.init_station_code()  # 初始化车站代码 返回值为dict

    def login(self):
        """
        打开登录的页面
        """
        driver.get(self.login_url)
        WebDriverWait(driver, 1000).until(
            ec.url_to_be(self.profiel_url)  # 等待直到url成为个人中心的页面
        )
        print('登录成功')

    def search_ticket(self):
        """
        余票查询
        :return:
        """
        # 打开余票查询的网址
        driver.get(self.leftTicket)
        # 通过id获取输入框
        # 隐藏的出发地input标签
        from_station_input = driver.find_element_by_id('fromStation')  # 出发地
        # 隐藏的目的地input标签
        to_station_input = driver.find_element_by_id('toStation')  # 目的地
        # 通过id找到出发时间的input标签
        train_date_input = driver.find_element_by_id('train_date')  # 出发时间

        # 输入出发地和目的地的代号
        from_station_code = self.station_code[self.from_station]  # 根据出发地找到出发点的代号
        to_station_code = self.station_code[self.to_station]  # 根据目的地找到目的地的代号
        # print(from_station_code, to_station_code)

        # 执行js代码，将出发地和目的地的代码放入隐藏的输入框 将出发时间放入输入框
        driver.execute_script('arguments[0].value="%s"' % from_station_code, from_station_input)
        driver.execute_script('arguments[0].value="%s"' % to_station_code, to_station_input)
        driver.execute_script('arguments[0].value="%s"' % self.train_date, train_date_input)

        # 执行点击查询按钮
        query_ticket_tag = driver.find_element_by_class_name('btn92s')
        query_ticket_tag.click()

        # 解析车次，显示车次，等待tTable的出现
        WebDriverWait(driver, 1000).until(
            ec.presence_of_element_located(By.XPATH, "//table/tbody[@id='queryLeftTable']/tr")
        )

        # 筛选有数据的tr,去掉属性为datatran的tr
        trains = driver.find_elements_by_xpath("//table/tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        # 遍历每一个车次
        for train in trains:
            infos = train.text.replace('\n', ' ').split(' ')
            print(infos)

    def run(self):
        """
        负责调用函数
        :return:
        """
        # 登录
        self.login()
        # 余票查询
        self.search_ticket()

    def init_station_code(self):
        """
        初始化车站代码
        :return:
        """
        wb = openpyxl.load_workbook('车站代号.xlsx')
        ws = wb.active  # 获取活动表
        lst = []  # 存储所有的车站代码及名称
        for row in ws.rows:  # 遍历所有行
            sub_list = []  # 用于存储每行的的车站代码，车站名称
            for cell in row:  # 遍历每一行的单元格
                sub_list.append(cell.value)
            lst.append(sub_list)
        return dict(lst)


def start():
    spider = TranSpider('长沙', '郑州', '2021-04-1')
    spider.run()
    # spider.init_station_code()


if __name__ == '__main__':
    start()
