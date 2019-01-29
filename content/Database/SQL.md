Title: SQL
Date: 2016-05-25 22:06:13
Tags: Database, SQL



# SQL

sql是结构化查询语言。

sql是一种标准，几乎所有关系型数据库都遵守。

但是不同的数据库又有自己的扩展。

SQL分为两部分，DML和DDL。

SQL大小写敏感，文本使用单引号，数值不需要引号。

# sql语法

sql注释:

    # 多行注释
    /*
    comment multi lines
    in a sql file.
    */

    # 单行注释
    /* comment single line */

    # 单行注释还可以直接用 -- 表示
    select * from table -- where condition;
    -- select * from table where condition;

***

# DDL

DDL: 数据定义语言

## create

创建数据库：

    CREATE DATABASE database_name;

建表：

    CREATE TABLE table(
        column1 type1,
        column2 type2,
        ...
    );

create也可以用来创建索引和视图．

## drop

删除数据库：

    DROP DATABASE database_name;

删表：

    DROP TABLE table;
    # 仅仅删除表中的数据，保留表
    TRUNCATE TABLE table;

drop也可以用来删除索引和视图．

## alter

变更表：

    # 添加列
    ALTER TABLE table ADD COLUMN column type;

    # 删除列
    ALTER TABLE table DROP COLUMN column;

    # 改变列的数据类型
    # sql server
    ALTER TABLE table ALTER COLUMN column type;
    # mysql
    ALTER TABLE table MODIFY COLUMN column type;
    # mysql/oracle
    ALTER TABLE table MODIFY column type;

***

# DML

DML: 数据操作语言

## select

查询操作:

    SELECT * FROM table;
    # 单表查询
    SELECT column FROM table;
    # 多表查询
    SELECT table1.column1, table2.column2 FROM table1, table2;

where子句选取数据：

    SELECT column FROM table WHERE condition;

引号的使用：

    # 文本使用单引号，大部分数据库也接受双引号
    SELECT column FROM table WHERE name='text';
    # 数字不能使用引号．
    SELECT column FROM table WHERE id=number;

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

    %    替代一个或多个字符
    _    替代一个字符
    [char list]    字符列中的任何单一字符
    [^char list]    不在字符列中的任何单一字符
    [!char list]    和上面一个等效
    SELECT * FROM table WHERE name LIKE '[abc]%' # 以abc开头的name

where子句多个条件可以使用的运算符：

    AND    与运算
    SELECT * FROM table WHERE name='canux' AND id=10;
    OR    或运算
    SELECT * FROM table WHERE name='canux' OR id=10;

order by子句对结果进行排序,默认升序(ASC)：

    # 默认升序
    SELECT column, column1 FROM table ORDER BY column;
    SELECT column, column1 FROM table ORDER BY column, column1;
    SELECT column, column1 FROM table ORDER BY column ASC;
    # DESC降序
    SELECT column, column1 FROM table ORDER BY column DESC;
    SELECT column, column1 FROM table ORDER BY column DESC, column1 ASC;
    # 根据第几个字段排序
    SELECT column, column1 FROM table ORDER BY number;
    # 多个字段排序，优先级从前到后
    SELECT column FROM table ORDER BY column1, column2
    SELECT column FROM table ORDER BY column1 DESC, column2 DESC

top子句用于规定要返回的记录数目：

    # SQL Server
    SELECT TOP number * FROM table;
    # mysql
    SELECT * FROM table LIMIT number;
    # oracle
    SELECT * FROM table WHERE ROWNUM <= number;

    Top 一般需要order by
    # number最小的10个
    select top 10 from table order by number
    # number最大的10个
    select top 10 from table order by number desc

group by子句用来分组，放在where子句后面如果有的话:

group by一定要用合计函数(count, max, min, sum, avg, ...).

    SELECT column1, aggregate_function(column2) FROM table GROUP BY column1;

having子句用来过滤group by的结果(相当where)，放在group by子句后面：

因为where不能和合计函数一起使用，所以使用having子句．

    SELECT column1, aggregate_function(column2) FROM table GROUP BY column1 HAVING aggregate_function(column) condition;

distinct关键字排除重复：

    SELECT DISTINCT column FROM table;

as关键字指定别名：

    # 指定表的别名
    SELECT alias_table1.column1, alias_table2.column2
    FROM table1 AS alias_table1, table2 AS alias_table2
    WHERE alias_table1.column2='test';

    # 指定字段别名
    SELECT column1 AS alias1, column2 AS alias2 FROM table;

执行顺序：

    from -> where -> group by -> having -> select -> distinct -> union -> order by -> top

## insert into

向表格插入新的行：

    # 一次插入完整行
    INSERT INTO table VALUES (value1, value2, ...);
    # 一次插入多行
    INSERT INTO table VALUES (val11, val12, ...) (val21, val22, ...) ...
    # 一次插入一行的一部分
    INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...);
    # 一次插入多行的一部分
    INSERT INTO table (col1, col2, ...) VALUES (val11, val12, ...) (val21, val22, ...)

## update set

修改表中数据：

    UPDATE table SET column1=value1 WHERE condition;

## delete from

删除表中的行：

    DELETE FROM table WHERE condition;
    DELETE FROM table; # 删除所有行

    TRUNCATE TABLE table; # mysql清空表的内容，不可恢复

***

# 函数

不同的数据库内置的部分函数不同．下面只列出大部分数据库都有的函数．

sql内置两种函数：合计(aggregate)函数　和　标量(scalar)函数.

sql函数的语法：

    SELECT FUNCTION(args) FROM table ...;

## aggregate function

    AVG()：　求平均值
    COUNT(): 统计行数
    FIRST(): 返回指定字段中第一个记录的值
    LAST():　返回指定字段中最后一个记录的值
    MAX():　返回一列中的最大值
    MIN():　返回一列中的最小值
    SUM():　返回一列的和

## scalar function

    UCASE():　把字段的值转换为大写
    LCASE():　把字段的值转换为小写
    MID(column, start[, length]):　从文本字段中提取字符，start从１开始
    LEN(): 返回文本字段中的长度
    FORMAT(column, format): 对字段进行格式化
    ROUND(column, decimals): 把数值字段舍入为指定的小数位数
    NOW()    返回当前的日期和时间

***

# join

为了从多个表中获取结果，就需要用join.

## inner join

inner join也就是默认的join.

全部匹配才返回．相当于table1和table2与.

    # 两张表连接
    SELECT table1.column, table2.column
    FROM table1 INNER JOIN table2
    ON table1.column = table2.column;

    # 三张表连接
    SELECT column
    FROM ((table1 INNER JOIN table2 ON table1.column1 = table2.column1) INNER JOIN table3
    ON table1.column2 = table3.column2);

## left join

左连接．返回左表table1的所有行，和右表table2匹配的行

    SELECT column
    FROM table1 LEFT JOIN table2
    ON table1.column = table2.column;

## right join

右连接，返回右表table2的所有行，和左表table1匹配的行

    SELECT column
    FROM table1 RIGHT JOIN table2
    ON table1.column = table2.column;

## full join

返回两张表的所有行．

    SELECT column
    FROM table1 FULL JOIN table2
    ON table1.column = table2.column;

***

# union

union操作符用于合并两个或多个select语句的结果集．

union只选取不同的值,也就是说table1和table2中的相同column只出现一次．

    SELECT column FROM table1
    UNION
    SELECT column FROM table2;

union all会列出所有的值，包括重复的．

    SELECT column FROM table1
    UNION ALL
    SELECT column FROM table2;

***

# select into

创建表的备份复件．

把table1的所有列插入到table2:

    SELECT * INTO table2 FROM table1 WHERE condition;
    # table2属于另外一个数据库externaldatabase
    SELECT * INTO table2 IN externaldatabase FROM table1 WHERE condition;

把table1的部分列插入到table2:

    SELECT column INTO table2 FROM table1 WHERE condition;
    # table2属于另外一个数据库externaldatabase
    SELECT column INTO table2 IN externaldatabase FROM table1 WHERE condition;

mysql需要用insert into ... select:

    # 如果table2已经存在
    INSERT INTO table2 SELECT * FROM table1 WHERE condition;
    # 如果table2不存在
    CREATE TABLE table2 AS SELECT * FROM table1 WHERE condition;

***

# constraints

constraints约束用于限制加入表的数据的类型．

## NOT NULL

not null强制约束列不能接受null值．

    CREATE TABLE tablename (
        id int NOT NULL,
        name varchar(255)
    );

## UNIQUE

unique约束唯一标识数据库表中的每条记录．

每个表可以有多个unique约束．

    # mysql:
    CREATE TABLE table (
        id int NOT NULL,
        name varchar(255),
        UNIQUE (id)
    );

    # sql server/oracle:
    CREATE TABLE table(
        id int NOT NULL UNIQUE,
        name varchar(255)
    );

给约束命名，并且标记多个列到unique:

    CREATE TABLE table (
        id int NOT NULL,
        firstname varchar(255),
        lastname varchar(255),
        CONSTRAINT constraintname UNIQUE (id, lastname)
    );

给已经存在的表添加约束：

    ALTER TABLE table ADD UNIQUE (id);
    # 给约束命名，并且标记多个列到unique
    ALTER TABLE table ADD CONSTRAINT constraintname UNIQUE (id, lastname);

撤销约束：

    # mysql:
    ALTER TABLE table DROP INDEX constraintname;
    # sql server/oracle:
    ALTER TABLE table DROP CONSTRAINTNAME constraintname;

## PRIMARY KEY

primary key主键必须包含唯一的值，主键列不能包含NULL值．

每张表最多只能有一个主键．

    # mysql:
    CREATE TABLE table (
        id int NOT NULL,
        firstname varchar(255),
        lastname varchar(255),
        PRIMARY KEY (id)
    );

    # sql server/oracle:
    CREATE TABLE table (
        id int NOT NULL PRIMARY KEY,
        firstname varchar(255),
        lastname varchar(255)
    );

给主键命名，并且添加多个列到primary key:

    CREATE TABLE table (
        id int NOT NULL,
        firstname varchar(255),
        lastname varchar(255),
        CONSTRAINT constraintname PRIMARY KEY (id, lastname)
    );

给已经存在的表添加约束：

    ALTER TABLE table ADD PRIMARY KEY (id);
    # 给约束命名，并且添加多个列到主键：
    ALTER TABLE table ADD CONSTRAINT constraintname PRIMARY KEY (id, lastname);

撤销约束：

    # mysql:
    ALTER TABLE table DROP PRIMARY KEY;
    # sql server/oracle:
    ALTER TABLE talbe DROP CONSTRAINT constraintname;

## FOREIGN KEY

一个表中的外键指向另一个表中的主键．

    # mysql:
    CREATE TABLE table1 (
        id_1 int NOT NULL,
        id_2 int,
        PRIMARY KEY (id_1),
        FOREIGN KEY (id_2) REFERENCES table2(id_2)
    );

    # sql server/oracle:
    CREATE TABLE table1 (
        id_1 int NOT NULL PRIMARY KEY,
        id_2 int FOREIGN KEY REFERENCES table2(id_2)
    );

给外键命名，并且添加多个列到foreign key:

    CREATE TABLE table1 (
        id_1 int NOT NULL,
        id_2 int,
        PRIMARY KEY (id_1),
        CONSTRAINT constraintname FOREIGN KEY (id_2) REFERENCES table2(id_2)
    );

给已经存在的表添加约束：

    ALTER TABLE table1 ADD FOREIGN KEY (id_2) REFERENCES table2(id_2);
    # 给外键命名，并且添加多列到外键
    ALTER TABLE table1 ADD CONSTRAINT constraintname FOREIGN KEY (id_2) REFERENCES table2(id_2);

撤销约束：

    # mysql:
    ALTER TABLE table1 DROP FOREIGN KEY constraintname;
    # sql server/oracle:
    ALTER TABLE table1 DROP CONSTRAINT constraintname;

## CHECK

check用于限制列中的值的范围．

    # mysql:
    CREATE TABLE table (
        id int NOT NULL,
        firstname varchar(255),
        lastname varchar(255),
        CHECK (id>0)
    );

    # sql server/oracle:
    CREATE TABLE table (
        id int NOT NULL CHECK (id>0),
        firstname varchar(255),
        lastname varchar(255)
    );

给约束命名，并且添加多个列到约束：

    CREATE TABLE table (
        id int NOT NULL,
        firstname varchar(255),
        lastname varchar(255),
        CONSTRAINT constraintname CHECK (id>0 AND lastname='cheng')
    );

给已经存在的表添加约束：

    ALTER TABLE table ADD CHECK (id>0);
    # 给约束命名，并且添加多列到约束
    ALTER TABLE table ADD CONSTRAINT constraintname CHECK (id>0 AND lastname='cheng');

撤销约束：

    # mysql:
    ALTER TABLE table DROP CONSTRAINT constraintname;
    # sql server/oracle:
    ALTER TABLE table DROP CHECK constraintname;

## DEFAULT

default约束用于向列中插入默认值．

    CREATE TABLE table (
        id int NOT NULL,
        country varcha(255) DEFAULT 'china'
    );

给已经存在的表添加约束：

    # mysql
    ALTER TABLE table ALTER country SET DEFAULT 'china';
    # sqlserver/oracle
    ALTER TABLE table ALTER COLUMN country SET DEFAULT 'china';

撤销约束：

    # mysql:
    ALTER TABLE table ALTER country DROP DEFAULT;
    # sql server/oracle:
    ALTER TABLE table ALTER COLUMN country DROP DEFAULT;

***

# increment

auto increment在每次插入新记录时，自动创建主键字段的值．

    # mysql使用auto_increment
    CREATE TABLE table (
        id int NOT NULL AUTO_INCREMENT,
        firstname varchar(255),
        lastname varchar(255),
        PRIMARY KEY (id)
    );

    # sql server使用identity:
    CREATE TABLE table (
        id int PRIMARY KEY IDENTITY;
        firstname varchar(255),
        lastname varchar(255)
    );

    # oracle使用sequence对:
    CREATE SEQUENCE sequencename
    MINVALUE 1
    START WITH 1
    INCRREMENT BY 1
    CACHE 10
    # 使用nextval函数获取下一个值：
    INSERT INTO table (id, firstname, lastname) VALUES (sequencename.nextval, 'canux', 'cheng');

auto increment的默认起始值是1,每次插入一行默认加一，可以修改起始值：

    ALTER TABLE table AUTO_INCREMENT=10;

***

# index

创建索引可以快速高效查询数据，但是用户无法看到索引．

    # 在表中创建简单索引，允许使用重复的值:
    CREATE INDEX indexname ON table (column, column1, ...);

    # 在表中创建唯一索引，两个行不能有相同索引值:
    CREATE UNIQUE INDEX indexname ON table (column, column1, ...);

删除索引：

    # mysql:
    ALTER TABLE table DROP INDEX indexname;
    # sql server:
    DROP INDEX table.indexname;
    # oracle:
    DROP INDEX indexname;

***

# view

视图是基于sql语句的结果集的可视化的表：

    CREATE VIEW viewname AS SELECT * FROM table WHERE condition;

更新视图：

    CREATE OR REPLACE VIEW viewname AS SELECT column FROM table WHERE condition;

查询视图：

    SELECT * FROM viewname;

删除视图：

    DROP VIEW viewname;

***

