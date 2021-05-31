import requests
from lxml import etree

url = 'https://www.qidian.com/rank/yuepiao'
headers = {
    'cookie': 'e1=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C45%22%2C%22l1%22%3A5%7D; _yep_uuid=f65a9d23-77b0-640f-a812-a9d8e2dd08b4; _csrfToken=mARGZiz6GKTDFAIGLCv8uL0QWelcgyUnqRhBJDwr; newstatisticUUID=1615958634_783202365; se_ref=baidu; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C45%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A5%7D',
    'referer': 'https://www.qidian.com/rank',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
resp.encoding = 'utf-8'
print(resp.text)
# tree = etree.HTML(resp.text)
# title = tree.xpath('//div[@class="book-mid-info"]/h4/text()')
# print(title)
