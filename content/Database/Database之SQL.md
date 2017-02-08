---
layout: post
title: Database之SQL
comments: true
date: 2016-05-25 22:06:13
updated:
tags:
- sql
- database
categories:
- Database
permalink:
---

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

## drop

## alert

***

# DML

DML: 数据操作语言

## select

查询操作:

    SELECT * FROM table

distinct关键字排除重复：

    SELECT DISTINCT column FROM table

where子句选取数据：

    SELECT column FROM table WHERE condition

where子句可用的运算符：

    =
    <> / !=
    >
    <
    >=
    <=
    BETWEEN
    LIKE

where子句多个条件可以使用的运算符：

    AND
    WHERE
    OR

order by子句对结果进行排序：

    SELECT column, column1 FROM table ORDER BY column
    SELECT column, column1 FROM table ORDER BY column, column1

order by子句和desc关键字降序排列：

    SELECT column, column1 FROM table ORDER BY column DESC

## insert into

向表格插入新的行：

    INSERT INTO table VALUES (value1, value2, ...)
    INSERT INTO table (column1, column2) VALUES(value1, value2)

## update

修改表中数据：

    UPDATE table SET column1=value1 WHERE condition

## delete

删除表中的行：

    DELETE FROM table WHERE condition
    DELETE FROM table # 删除所有行
