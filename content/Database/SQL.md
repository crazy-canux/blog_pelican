Title: SQL
Date: 2016-05-25 22:06:13
Tags: SQL

# SQL

sql是结构化查询语言。

sql是一种标准，几乎所有关系型数据库都遵守。

但是不同的数据库又有自己的扩展。

SQL分为两部分，DML和DDL。

SQL大小写敏感，文本使用单引号，数值不需要引号。

***

# DDL

DDL: 数据定义语言

## create

创建数据库：

    CREATE DATABASE database

建表：

    CREATE TABLE table(
        column1 type1,
        column2 type2
    )

创建索引：

    CREATE INDEX index ON table (column)
    CREATE UNIQUE INDEX index

创建视图：

    CREATE VIEW view AS SELECT column FROM table

## drop

删除数据库：

    DROP DATABASE database

删表：

    DROP TABLE table
    # 仅仅删除表中的数据，保留表
    TRUNCATE TABLE table

删除索引：

    # Sql server
    DROP INDEX table.index
    # Oracle
    DROP INDEX index
    # Mysql
    ALTER TABLE table DROP INDEX index

删除视图：

    DROP VIEW view

## alter

变更表：

    # 添加列
    ALTER TABLE table ADD (column type)
    # 删除列
    ALTER TABLE table DROP COLUMN column
    # 改变数据类型
    ALTER TABLE table ALTER COLUMN column type

***

# DML

DML: 数据操作语言

## select

查询操作:

    SELECT * FROM table
    # 单表查询
    SELECT column FROM table
    # 多表查询
    SELECT table1.column1, table2.column2 FROM table1, table2

where子句选取数据：

    SELECT column FROM table WHERE condition

where子句条件表达式可用的运算符：

    =
    <>
    !=
    >
    <
    >=
    <=

    BETWEEN [value1, value2]
    BETWEEN value1 AND value2
    NOT BETWEEN

    IN (value1, value2)
    NOT IN

    IS NULL
    IS NOT NULL

    LIKE
    NOT LIKE

like运算符的通配符：

    # ％替代一个或多个字符
    %
    # _替代一个字符
    _
    # 字符列中的任何单一字符
    [char list]
    # 不再字符列中的任何单一字符
    [^char list]
    [!char list]

where子句多个条件可以使用的运算符：

    AND
    WHERE
    OR

order by子句对结果进行排序,默认升序(ASC)：

    # 默认升序
    SELECT column, column1 FROM table ORDER BY column
    SELECT column, column1 FROM table ORDER BY column, column1
    SELECT column, column1 FROM table ORDER BY column ASC
    # DESC降序
    SELECT column, column1 FROM table ORDER BY column DESC
    SELECT column, column1 FROM table ORDER BY column DESC, column1 ASC
    # 根据第几个字段排序
    SELECT column, column1 FROM table ORDER BY number

top子句用于规定要返回的记录数目：

    # SQL Server
    SELECT TOP number * FROM table
    # mysql
    SELECT * FROM table LIMIT number
    # oracle
    SELECT * FROM table WHERE ROWNUM <= number

group by子句用来分组，放在where子句后面如果有的话:

    SELECT column1, column2 FROM table GROUP BY column1

having子句用来过滤group by的结果(相当where)，放在group by子句后面：

    SELECT column1, column2 FROM table GROUP BY column1 HAVING condition

distinct关键字排除重复：

    SELECT DISTINCT column FROM table

as关键字指定别名：

    # 指定表的别名
    SELECT alias_table1.column1, alias_table2.column2
    FROM table1 AS alias_table1, table2 AS alias_table2
    WHERE alias_table1.column2='test'
    # 指定字段别名
    SELECT column1 AS alias1, column2 AS alias2 FROM table

执行顺序：

    from -> where -> top -> group by -> having -> select -> order by

## insert into

向表格插入新的行：

    INSERT INTO table VALUES (value1, value2, ...)
    INSERT INTO table (column1, column2) VALUES(value1, value2)

## update set

修改表中数据：

    UPDATE table SET column1=value1 WHERE condition

## delete from

删除表中的行：

    DELETE FROM table WHERE condition
    DELETE FROM table # 删除所有行

***

# 函数

不同的数据库内置的函数不同．

sql内置两种函数：合计(aggregate)函数　和　标量(scalar)函数.

sql函数的语法：

    SELECT FUNCTION(args) FROM table ...

AVG()：　求平均值

COUNT(): 统计行数

FIRST(): 返回指定字段中第一个记录的值

LAST():　返回指定字段中最后一个记录的值

MAX():　返回一列中的最大值

MIN():　返回一列中的最小值

SUM():　返回一列的和

UCASE():　把字段的值转换为大写

LCASE():　把字段的值转换为小写

MID(column, start[, length]):　从文本字段中提取字符，start从１开始

LEN(): 返回文本字段中的长度

ROUND(column, decimals): 把数值字段舍入为指定的小数位数

FORMAT(column, format): 对字段进行格式化

***

# 高级知识

## join

join表示连接

inner join表示内连接

left join(left outer join)表示左连接

right join(right outer join)表示右连接

full join(full outer join)表示全连接

## union

union操作符用于合并两个或多个select语句的结果集．

union all

## select into

## 约束

NOT NULL:

UNIQUE:

PRIMARY KEY:

FOREIGN KEY:

CHECK:

DEFAULT:

