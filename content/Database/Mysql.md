Title: Mysql
Date: 2016-05-25 12:14:59
Tags: Database, Mysql



# Mysql

安装mysql服务器

    $ sudo apt-get install mysql-server
    $ sudo yum install mysql-community-server

    $ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
    # 注意mysql的/etc/mysql/my.cnf和相关文件如果设置了bind-address = 127.0.0.1就无法远程访问，需要注释掉．

安装mysql客户端

    $ sudo apt-get install mysql-client
    $ sudo yum install mysql-community-client

安装开发工具：

    $ sudo apt-get install libmysqlclient-dev

CLI工具： mysql

GUI工具： mysql workbench

安装完成默认的数据库是 mysql。

mysqld的默认端口是3306.

# mysql命令

    $ mysql [OPTIONS] [database]

初始化时需要用root用户进入mysql命令行

    $ mysql -uroot -p
    $ mysql -h<host> -P<port> -uroot -p<password>

创建用户后用其它用户操作：

    $ mysql -u<user> -p

本地执行sql语句或mysql客户端命令:

    $ mysql -u<username> -p<password> <database> -e/--execute <sql query>

远程执行sql语句或mysql客户端命令:

    $ mysql -h<host> -P<port> -u<username> -p<password> <database> -e/--execute <sql query>

启用'load data local'命令：

    # 交互式
    $ mysql --local-infile=1 -uroot -ppassword
    # 非交互式
    $ mysql --local-infile=1 -uroot -pchengca w3c -e "LOAD DATA LOCAL INFILE '/home/user/customers.txt' INTO TABLE Customers COLUMNS TERMINATED BY '\t' LINES TERMINATED BY '\n';"

导出数据命令:

    $ mysqldump -u<username> -p<password> <databasename>  >  dump.sql

mycli:

A command line client for MySQL that can do auto-completion and syntax highlighting.

<https://github.com/dbcli/mycli>

    $ pip install -U mycli

# CLI

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
    mysql> use database # 切换到数据库

    charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
    warnings  (\W) Show warnings after every statement.
    nowarning (\w) Don't show warnings after every statement.

其它可以在mysql客户端执行的命令：

    # 从本地一个文件导入数据，列分隔符为\t,行分隔符为\n
    LOAD DATA LOCAL INFILE '/home/user/customers.txt' INTO TABLE Customers COLUMNS TERMINATED BY '\t' LINES TERMINATED BY '\n';

***

# 数据类型

***

# 函数和运算符

date and time：

<https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html>

    NOW() // '2018-11-18 16:00:28'
    UTC_TIMESTAMP() // '2018-11-18 08:01:04'
    CURDATE()  // '2018-11-18'
    UTC_DATE() // '2018-11-18'
    CURTIME()  // '16:02:18'
    UTC_TIME() // '08:03:36'

    UNIX_TIMESTAMP() // '1542528051'
    DATE()
    TIME()
    DATEDIFF()

control flow:：

    CASE

    IF()
    IFNULL(column, 0)
    NULLIF()

comparison:

    COALESCE(column, 0)

    ISNULL()
    IS NULL

    IN()
    NOT IN()

***

# SQL

注意：hostname 指定能连接的server，%表示任何server．

查看版本：

    SELECT VERSION();

查看所有用户：

    SELECT DISTINCT(USER) FROM mysql.user;
    SELECT user,host FROM mysql.user;

查看当前用户：

    SELECT USER();

创建/删除用户：

    CREATE USER 'username'@'%' IDENTIFIED BY 'password';
    DROP USER 'username'@'%';

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

    GRANT ALL PRIVILEGES ON databasename.* TO 'username'@'%';
    FLUSH PRIVILEGES;

查看权限：

    SHOW GRANTS FOR 'username'@'%';

查看所有表：

    show tables;

查看表结构：

    desc tablename;

***

# Issue

1. mysql8  workbench 连不上的问题 :

issue:

    authentication plugin 'caching_sha2_password' cannot be loaded: the specified module could not be found。

fix：

    alter user 'sandbox'@'%' identified with mysql_native_password by 'password';

2. max_commection 问题:

issue:

    当连接池连接数量超过最大连接数就无法再建立连接

fix:

    set global max_connections = 5000;
