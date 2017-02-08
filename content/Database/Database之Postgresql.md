---
layout: post
title: Database之Postgresql
comments: true
date: 2016-07-08 12:56:19
updated:
tags:
- postgresql
categories:
- Database
permalink:
---

# postgresql

安装postgresql：

    sudo apt-get install postgresql

安装第三方库：

    sudo apt-get install postgresql-contrib-9.3 libpg-dev postgresql-server-dev-9.3

GUI工具： pgAdminIII
CLI工具： psql

# postgresql相关命令

    $passwd postgres # 修改默认管理员用户postgresql的密码
    $su - postgresql # 切换到默认的postgresql用户
    $createuser <username> # 在命令行添加用户
    $dropuser <username> # 在命令行删除用户
    $createdb <database> -O <username> # 在命令行添加数据库
    $dropdb <database> # 在命令行删除数据库
    $show

# pssql的命令

    $psql # 进入psql
    $psql <database> # 登陆数据库
    $psql -U <username> -d <database> # 登陆用户的数据库

    help # 查看所有信息
    \h # 查看sql命令
    \? # 查看psql命令
    \g # 执行sql语句
    \q # 退出psql

    \du # 查看所有用户信息
    \c <database> # 切换数据库
    \c <database> <username> # 登陆用户的数据库
    \l # 查询当前用户的所有数据库
    \d # 查看表关系
    \d <table> # 查询表结构

# SQL

    ALTER USER/ROLE <username> WITH PASSWORD <password>; #更改用户密码
    SELECT username/* FROM pg_user; # 查看所有用户
    SELECT username/* FROM pg_shadow; # 查看所有用户密码

    CREATE GROUP <groupname>; # 添加用户组
    ALTER GROUP <groupname> ADD USER <username>,<username1>,...; # 添加用户到组
    ALTER GROUP <groupname> DROP USER <username>,<username1>,...; # 从组删除用户

    CREATE ROLE <username> PASSWORD <password>; # 创建用户和密码
    CREATE ROLE <username> LOGIN;
    CREATE ROLE <username> SUPERUSER;
    CREATE ROLE <username> CREATEDB;
    CREATE ROLE <username> CREATEROLE;
    CREATE ROLE <username> REPLICATION;
    DROP ROLE <username>; # 删除role

    SELECT datname/* FROM pg_database; # 查询当前用户的所有数据库
    CREATE DATABASE <database> OWNER=<username>; # 创建数据库
    DROP DATABASE <database>; # 删除数据库

    SELECT tablename/* FROM pg_tables; # 查看所有表
    CREATE TABLE tablename(
    <type> <name>,
    ...
    ); # 创建表
    DROP TABLE <table>; # 删除表

    SELECT version();
    SELECT current_date;
    SELECT current_time;

# python

## psycopg

<http://initd.org/psycopg/>

安装库：

    sudo pip install psycopg2

使用：

    import psycopg2
    cxn = psycopg2.connect(database='postgres', user='postgres', passwd='*')
    cur = cxn.cursor()
    cur.execute(<sql query>)
    ...
    cur.close()
    cxn.close()

# java
