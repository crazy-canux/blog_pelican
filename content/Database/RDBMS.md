Title: RDBMS
Date: 2016-04-03 14:46:14
Tags: Database, RDBMS

# RDBMS

关系数据库管理系统。

***

# SQLite

# Oracle

# MSSQL

# Mysql

# Postgre

***

# c

安装ODBC一般能访问所有数据库。

# python

安装相应的数据库的python库。

# JavaScript

# go

***

# dataset

<https://github.com/pudo/dataset>

    import dataset
    db = dataset.connect('sqlite:///mydatabase.db')
    db = dataset.connect('mysql://user:password@localhost/mydatabase')
    db = dataset.connect('postgresql://scott:tiger@localhost:5432/mydatabase')

# pyodbc

<https://github.com/mkleehammer/pyodbc>

    import pyodbc
    cnxn = pyodbc.connect('DRIVER={MySQL};DATABASE=test;SOCKET=/var/lib/mysql/mysql.sock')
    cnxn = pyodbc.connect('DRIVER=MyOracle;DBQ=x.x.x.x:1521/orcl;UID=myuid;PWD=mypwd')
    cnxn = pyodbc.connect('DSN=MySQLServerDatabase;UID=myuid;PWD=mypwd') # from linux/unix
    cnxn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=test;DATABASE=test;UID=user;PWD=password') # from windows

***
