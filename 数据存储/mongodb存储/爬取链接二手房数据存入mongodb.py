"""
网址：https://cs.lianjia.com/ershoufang/

https://cs.lianjia.com/ershoufang/pg2/
"""
import requests
import mysql.connector
import pymongo
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().random
}

data = []


class LianjiaSpider:
    def __init__(self):
        self.url = 'https://cs.lianjia.com/ershoufang/pg{}/'
        self.headers = headers

    def send_respone(self, url):
        """
        发送请求
        :param url:
        :return:
        """
        resp = requests.get(url=url, headers=headers)
        resp.encoding = 'utf-8'
        try:
            if resp.status_code == 200:
                return resp.text
        except Exception as e:
            raise e

    def parse_data(self, resp):
        """
        解析数据
        :param resp:
        :return:
        """
        soup = BeautifulSoup(resp, 'lxml')

        ul_ = soup.find('ul', class_='sellListContent')
        li_list = ul_.find_all('li')
        for item in li_list:
            # 名字
            name = item.find('div', class_='title').text

            # 地址
            address = item.find('div', class_='positionInfo').text.replace(' ', '')

            # 格式
            type_ = item.find('div', class_='houseInfo').text

            # 关注人数
            num = item.find('div', class_='followInfo').text.split('/')[0]

            # 发布时间
            time = item.find('div', class_='followInfo').text.split('/')[1]

            # 总价
            nums = item.find('div', class_='totalPrice').text

            # 单价
            price = item.find('div', class_='unitPrice').text

            data.append({'name': name,
                         'address': address,
                         'type_': type_,
                         'num': num,
                         'time': time,
                         'nums': nums,
                         'price': price})
        return data
        # self.save(data)

    def save(self, data):
        """
        保存数据到mysql数据库
        :return:
        """
        client = pymongo.MongoClient()
        db = client['schoo']
        collection = db.student
        # collection.insert_many(data)

        d = collection.find()
        for _ in d:
            print(_)

    def start(self):
        """
        爬虫开始
        :return:
        """
        for i in range(1, 4):
            url = self.url.format(i)
            resp = self.send_respone(url=url)
            data = self.parse_data(resp)
        self.save(data)


if __name__ == '__main__':
    lianjia = LianjiaSpider()
    lianjia.start()
