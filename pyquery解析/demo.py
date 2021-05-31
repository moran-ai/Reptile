from pyquery import PyQuery as pq

html = """
    <html>
        <head>
            <title>pyQuery</title>
        </head>
        <body>
            <h1>pyQuery</h1>
        </body>
    </html>
"""
doc = pq(html) # 创建Pyquery的对象，进行一个类型转换，将str类型转为PyQuery类型
print(doc)
print(type(doc))
print(type(html))
print(doc('title'))