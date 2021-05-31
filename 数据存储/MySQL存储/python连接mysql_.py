import mysql.connector

# 创建连接对象
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='itcast',
    database='python_test'
)

# 获取游标
cursor = db.cursor()

# 编写sql语句
sql = 'insert into student(id,name) values (%s,%s)'

# 列表赋值
vals = [
    (3, '上海'),
    (4, '成都'),
    (5, '北京'),
    (6, '长沙'),
]

# 插入多条数据
cursor.executemany(sql,vals)
db.commit()
print('插入多条数据成功')