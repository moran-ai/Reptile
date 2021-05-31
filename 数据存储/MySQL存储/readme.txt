mysql8.0版本启动
    1.启动mysql服务
        net start mysql80

    2.停止mysql服务
        stop start mysql80

    3.进入mysql服务
        mysql -uroot -p

    4.创建数据库
        create database 数据库名;
    5.显示所有数据库
        show databases;
    6.使用数据库
        use 数据库名;
    7.删除表
        drop table 表名;
    8.删除数据库
        drop database 数据库名;

二.修改表结构
    1.增加一列
        alter table 表名 add 列名 数据类型(长度)
    2.修改列的数据类型
        alter table 表名 modify 列名 数据类型(长度)
    3.修改列的名称
        alter table 表名 change 原列名 新列名 数据类型(长度)
    4.删除列
        alter table 表名 drop 列名

三.操作数据
    1.向表中插入数据
        insert into 表名[(字段列表)] values (值列表)

    2.修改表中的数据
        update 表名 set 字段1=值1,字段2=值2... [where]

    3.删除表中的数据
        delete from 表名 [where]

四.数据查询
    1.单表查询
        groupy by 分组
        order by 排序
        select ... from 表名 [wherer]... [groupy by]...[having]...[order by asc/desc]

        ① 查询表中的所有数据
            select * from 表名;

        ② 查询表中的部分数据
            部分列
                select 列名1,列名2,列名3 from 表名;

            部分行
                例如:
                    查询表中成绩大于100的姓名
                    select name from 表名 where score > 100;

           查询行和列
                例如：
                    查询表中成绩大于100的姓名,性别,成绩
                    select name,sex,score from student where score>100;
        ③ 对数据进行排序
            例如：
                对数据按照成绩进行排序
                select * from student order by score asc;  asc:升序
                select * from student order by score desc; desc:降序

    2.模糊查询
        只能与字符型一起使用的like关键字
            ① 查询数据中包含某个数据的数据    like
                例如： 查询姓名中包含J的所有学生
                    select * from student where name like '%J%';
            ② 查询姓名以J开头的学生   like
                    select * from student where name like 'J%';
                    select score from student where name like 'J%';
                    select name,score from student where name like 'J%';
            ③ 查询姓名中第二个是J的学生  _代表一个字符  like
                    select * from student where name like '_J';
        区间范围的 between ... and ..
            ① 查询数据中多少到多少的数据
                例如：
                    查询表中学生成绩在100到300之间的学生信息
                        select * from student where score between 100 and 300;
                    查询表中学生成绩在100到300之间的学生信息,按照降序
                        select * from student where score between 100 and 300 order by score desc;
        在给定的值中进行选择的 in
            ① 查询学生姓名，性别为男，300的学生信息
                select * from student where name in ('男', 300);

    3.分组函数  带函数的查询
        count()  行的个数
            ① 统计表中的数据的个数
            select count(*) from 表名;

            ② 统计表中指定字段的个数
                例如：统计表中性别为男性的人数
                    select count(*) from student where sex='男';
        sum()     求和
            ① 查询总成绩
                select sum(score) from student;
                select sum(score) from student where name='wang';
        avg()     平均值
            ① 查询平均成绩
                select avg(score) from student;
        max()     最大值
            ① 查询最高成绩
                 select max(score) from student;
        min()     最小值
            ① 查询最低成绩
                select min(score) from student;

    4.分组查询 group by ...having  与分组函数count,max,min,avg,sum一起使用
        ① 查询男女生的人数，性别，成绩
            select sex,score count(*) from student group by sex;

        ② 按照成绩进行查询，查询成绩大于30的
            select score,count(*) from student group by score having score>30;


五.多表查询
    inner join 内连接查询
        select ... from 表1 Inner join 表2 on 连接条件 ..[where]...

    left/right 外连接查询
        select ... from 表1 left/right join 表2 on 连接条件 ..[where]...

六.连接mysql
1.安装mysql-connector
    导入
        import mysql.connector

2.创建数据库连接
    mysql5.0版本的连接
    connect(host,user,passwd,database)
    ① 创建连接对象
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='itcast',
            database='python_test'
        )
    返回连接对象代表连接成功
        <mysql.connector.connection.MySQLConnection object at 0x000002C95FD946D8>

    ② 创建游标
        # 获取游标
            cursor = db.cursor()

    ③ 编写sql语句
        # 编写sql语句
            sql = 'insert into student(id,name) values (%s,%s)'
            values = (1, '张三')
    ④ 执行插入一条语句
        cursor.execute(sql,values)

        插入一个列表
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

    ⑤ 提交
        db.commit()


    mysql8.0版本的连接 加上 auth_plugin='mysql_native_password'
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='itcast',
        database='python_test',
        auth_plugin='mysql_native_password'
    )
