Title: Postgre
Date: 2016-04-03 14:46:14
Tags: Database, Postgre



# PostgreSQL

安装postgresql：

    $ sudo apt-get install postgresql

安装第三方库：

    $ sudo apt-get install postgresql-contrib-9.3 libpg-dev postgresql-server-dev-9.3

GUI工具： pgAdminIII

CLI工具： psql

postgresql的端口是5432．

# postgresql命令

安装完成后默认的admin就是postgres, postgres里有默认数据库postgres.

    $passwd postgres # 修改默认管理员用户postgres的密码
    $su - postgres # 切换到默认的postgres用户

    $ psql [OPTION]... [DBNAME [USERNAME]]

    $createuser <username> -P # 在命令行添加用户
    $dropuser <username> # 在命令行删除用户

    $createdb <database> -O <username> # 在命令行添加数据库
    $dropdb <database> # 在命令行删除数据库

    # 交互式:
    $ psql -U [username] [database]

    # 非交互式：
    $ PGPASSWORD='password';psql -h <host> -p <port> -U <username> -d [database] -c "[psql command]"

导出数据：

    $ pg_dump dbname > out.sql

pgcli:

This is a postgres client that does auto-completion and syntax highlighting.

<https://github.com/dbcli/pgcli>

    $ pip install -U pgcli

# CLI

先用psql进入postgre的命令行.

    help # 查看所有信息
    \? # 查看psql命令
    \h # 查看sql命令
    \g # 执行sql语句
    \q # 退出psql

    \du # 查看所有用户信息
    \l # 查询当前用户的所有数据库
    \c <database> # 切换数据库
    \c <database> <username> # 登陆用户的数据库
    \dt 等效于show tables;
    \d # 查看表关系
    \d <table> # 查询表结构

***

# 数据类型

# 函数

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

***

