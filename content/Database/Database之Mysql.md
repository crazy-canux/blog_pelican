---
layout: post
title: Database之Mysql
comments: true
date: 2016-05-25 12:14:59
updated:
tags:
- mysql
categories:
- Database
permalink:
---

# Mysql

安装mysql服务器

    sudo apt-get install mysql-server
    sudo yum install mysql-community-server

安装mysql客户端

    sudo apt-get install mysql-client
    sudo yum install mysql-community-client

CLI工具： mysql

GUI工具： mysql workbench

安装完成默认的数据库是 mysql。

# mysql命令

    mysql db_name
    mysql --user=user_name --password=your_password db_name
    mysql db_name < script.sql > output.tab

初始化时需要用root用户进入mysql命令行

    mysql -u root -p
    mysql -h <mysql server> -P <port> -u root -p

创建用户后用其它用户登陆：

    mysql -u username -p
    mysql -u <mysql server> -P <port> -u <username> -p

导出数据命令:

    $mysqldump -u username -p databasename > dump.sql

# mysql的命令

先用mysql命令进入mysql的命令行。

?         (\?) Synonym for help.
help      (\h) Display this help.

exit      (\q) Exit mysql. Same as quit.
quit      (\q) Quit mysql.

clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit      (\e) Edit command with \$EDITOR.
ego       (\G) Send command to mysql server, display result vertically.
go        (\g) Send command to mysql server.
nopager   (\n) Disable pager, print to stdout.
notee     (\t) Don't write into outfile.
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.

    mysql> source /path/to/dump.sql # 从sql导入数据

status    (\s) Get status information from the server.
system    (\!) Execute a system shell command.
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
use       (\u) Use another database. Takes database name as argument.

    use database 切换到数据库

charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.

# sql query

查看版本：

    SELECT VERSION();

查看所有用户：

    SELECT DISTINCT(USER) FROM mysql.user;
    SELECT user,host,password FROM mysql.user;

查看当前用户：

    SELECT USER();

创建/删除用户：

    CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
    DROP USER 'username'@'hostname';

设置和更改密码：

    UPDATE mysql.user SET PASSWORD('password') WHRER USER='username' AND HOST='hostname';

查看所有数据库：

    show databases;

查看当前数据库：

    SELECT DATABASE();

创建/删除数据库：

    CREATE DATABASE databasename;
    DROP DATABASE databasename;

使用数据库：

    use databasename

指定数据库对用户授权：

    GRANT ALL PRIVILEGES ON databasename.* TO "username"@"hostname";
    FLUSH PRIVILEGES;

查看所有表：

    show tables;

查看表结构：

    desc tablename;

# Python

## pymysql

<https://github.com/PyMySQL/PyMySQL>

    sudo pip install PyMySQL

    import pymysql.cursors
    connection = pymysql.connect(host='localhost', user='user', password='password', database='db')
    # port = 3306 default
    # charset = utf8
    # connect_timeout
    # cursorclass = pymysql.cursors.DictCursor -> return value as dict.
    # cursorclass = pymysql.cursors.SSCursor -> return value as tupple.
    cursor = connection.cursor()
    cursor.execute(<sql query>)
    ...
    cursor.close()
    connection.close()

## connector/Python

<http://dev.mysql.com/doc/connector-python/en/>

<https://github.com/mysql/mysql-connector-python>

官方提供的python的API。

    sudo yum/apt-get install mysql-connector-python

    import mysql.connector

## MySQLdb

MySQLdb 1.X 是旧版本，<https://github.com/farcepest/MySQLdb1>

MySQLdb 2.X 是MySQLdb1的升级版，改名为moist，不稳定， <https://github.com/farcepest/moist>

mysqlclient 是MySQLdb1的升级版, <https://github.com/PyMySQL/mysqlclient-python>

# Java

## connector/J

<http://dev.mysql.com/doc/connector-j/5.1/en/>

<https://github.com/mysql/mysql-connector-j>

官方提供的java的API，下载java安装包安装。

