---
layout: post
title: Database之MSSQL
comments: true
date: 2016-04-06 15:33:42
updated:
tags:
- mssql
- database
- pymssql
- pyodbc
- freetds
categories:
- Database
permalink:
---

# MSSQL

商业版：
1. 企业版
2. 商业智能版
3. 标准版

免费版：
1. Express
2. Developer
3. Compact
4. Web
5. SQL Azure

安装配置参考文档。

# mssql基本属性

system databases:
1. master 主数据库
2. model  模板数据库
3. msdb   自动机数据库
4. tempdb 零时交换数据库,不需要备份,挂载到独立的子系统。
5. resource

default port：1433

2008: max instance 16

2012: max instance 256

Client -> SNAC(OLE DB/ODBC) -> Network Libraries -> TDS <=> Server -> Endpoints -> SQL OS(relational engine/storage engine)

## XX.mdf & XX.ldf

sql server存储数据放在data file, 叫.mdf/.ndf,日志文件存放在log file，叫.ldf。

只能有一个.mdf。

Shinking, 自动收缩，不推荐。
database-file-dbcc-shrinks
database-file-auto-shrinks
database-datafile-auto-shrinks
database-logfile-auto-shrinks

Expanding,自动扩展。
database-file-auto-growths
database-datafile-auto-growths
database-logfile-auto-growths

connection-time
cpy-busy
io-busy
full-scans
connected-users
transactions
batch-requests
latches-waits
latches-wait-time
locks-waits
locks-timeouts
locks-deadlocks
sql-recompilations
sql-initcompilations
total-server-memory
mem-pool-data-buffer-hit-ratio
lazy-writes
page-life-expectancy
free-list-stalls
checkpoint-pages
database-online
database-free
database-used
database-backup-age
database-logbackup-age
failed-jobs
jobs-enabled
list-databases
list-datafiles
list-locks

***

# GUI

## SSMS

SQL Server Management Studio是mssql的图形化管理界面。

从模板中获取常用的SQL：

view -> template explorer + query -> specify values for template parameters.

## SSIS

数据集成服务。

## cliconfg.exe

用于给数据库取别名并分发。

***

# CLI

## sqlcmd

SQL Server的命令行界面。

    sqlcmd -? # 查看帮助
    sqlcmd /?

    sqlcmd -A # 管理员专用模式。

## bcp

数据库import/export工具

    bcp -? # 查看帮助
    bcp XXX out XXX -T -c

## sqlps

SQL Server的PowerShell命令行模式。

***

# Security

设置权限：
1. 数据库服务器级别权限
2. 数据库权限
3. 表级权限(schema)
4. 列级权限

* 数据库服务器的security
    1. 可以创建Logins用户，包括sa帐号和windows的AD帐号。

* 数据库的security
    1. 可以创建Users用户，用于连接这个数据库。
    2. 可以创建和设置schemas,默认dbo。

权限的设置在SSMS的 属性->权限 里面设置。

***

# data type

三种数据类型：
1. system data types
2. alias data types
3. user-defined data types

system data有下面类型：

可以通过SSMS查看。

    tinyint: 8bits
    smallint: 16bits
    int: 32bits
    bigint: 64
    decimal:
    numeric:
    smallmoney: 32bits
    money: 64bits
    bit: 0/1

    float: <=53bits
    real: 32bits

    date:
    datetime2:
    datetime:
    datetimeoffset:
    smalldatetime:
    time:

    char:
    nchar:
    varchar:
    nvarchar:
    varchar(max): <=2GB
    nvarchar(max): <=2GB

    rowversion:

## data attribution

    uniqueidentifer

    null
    not null

    unicode

    collate

## modfy data type

    cast

    convert

    try_convert

    parse

    try_parse

    Implicit data conversion(隐式的数据转换)。

***

# data structure

## tables

创建create，更新alert，删除drop都是标准sql。

插入insert，更改update，删除delete表的内容都是标准sql。

* merge

使用merge来快速插入，没有就insert，有就update。

## views

创建create，更新alert，删除drop都是标准sql。

* system views

    系统视图都是以sys开头的。

        SELECT * FROM [dbname].sys.databases # 查询所有数据库信息。
        SELECT * FROM [dbname].sys.servers
        SELECT * FROM [dbname].sys.services

* 用户自定义的view

## index

创建create，更新alert，删除drop都是标准sql。

table和view都有index。

***

# database actions

## administrator command

sa是数据库默认的管理员,dbcc需要sa权限执行。

    DBCC HELP('?') # 查询所有DBCC命令
    DBCC HELP('command') # 查询具体命令的帮助

创建/删除数据库：

    CREATE DATABASE databasename;
    DROP DATABASE databasename;

## replication

在不同的数据库服务器之间导数据。

## transaction log ship

在不同的数据库服务器之间导数据。

## db->tasks->import/export/copy

导入/导出/复制，以表为单位进行复制。

# programmability(T-SQL)

## sql query

和标准SQL操作一样。

    bulk insert

## Stored Procedures

* system stored Procedures(系统自带的SP)

    sys.sp_XXX是系统SP。
    sys.xp_XXX是扩展SP。

* 用户自定义的SP

1. 创建SP

        CREATE PROCEDURE <schema>.<procedure>
            @p1 type = value1
            @p2 type = value2
            ...
        AS
        BEGIN
            SELECT @p1, @p2, ...
        END
        GO


2. 修改SP

        ALERT PROCEURE <schema>.<procedure>
            @p1 type2 = value1
            @p2 type2 = value2
            ...
        AS
            SELECT @p1, @p2 ...
        GO

3. 执行SP

        EXECUTE/EXEC <Schema>.<Procedure> <value1> <value2> ...
        GO

4. 删除SP

        DROP PROCEDURE <procedure>

## Functions

* system functions

    系统自带的函数。

        SELECT @@VERSION
        SELECT @@SERVERNAME
        SELECT @@SERVICENAME

* scalar functions

    scalar-valued: 标量函数，返回单一值。

* table-valued functions

    表值函数，返回一个数据和类型对的表。
    inline table-valued: 内嵌的表值函数。
    multi-statement table-valued:

1. 创建scalar-valued函数

    CREATE FUNCTION <schema>.<function> (@p1 type1)
    RETURNS return_value_datatype
    WITH EXECUTE AS CALLER
    AS
    BEGIN
        body of the function
    END
    GO

2. 创建inline table-valued函数

3. 创建multi-statement table-valued函数

4. 删除函数

    DROP FUNCTION <schema>.<function>
    GO

## debug

11-16

RAISE ERROR

THROW error, 'msg', number;

***

# wmi

安装mssql之后提供mssql的wmi的类：

通过运行wql获取数据库属性。

    select * from Win32_PerfFormattedData_MSSQLSERVER_SQLServerLocks

# powershell

通过powershell运行sql语句或store procedure：

    $connection = new-object System.Data.SqlClient.SqlConnection "Server=$server;Database=$database";Trusted_Connection=True"
    $connection.Open()
    $sql = "select @@version"
    $command = new-object System.Data.SqlClient.SqlCommand $sql $connection
    $return = $command.ExecuteReader()

安装mssql之后提供mssql的powershell模块sqlps：

通过模块的命令运行sql语句和store procedure。

    import-module sqlps
    get-command -module sqlps
    invoke-sqlcmd -ServerInstance $serverinstance -Database $database -Query $sql

***

# freeTDS

> FreeTDS is a set of libraries for Unix and Linux that allows your programs to natively talk to Microsoft SQL Server and Sybase databases.

<http://www.freetds.org/>

<https://github.com/FreeTDS/freetds>

    sudo apt-get install freetds*

配置freetds，/etc/freetds/freetds.conf:

    # A typical Sybase server
    [egServer50]
            host = symachine.domain.com
            port = 5000
            tds version = 5.0

    # A typical Microsoft server
    [egServer70]
            host = ntmachine.domain.com
            port = 1433
            tds version = 7.0

***

# Python

通过python访问mssql需要安装相应的包，linux还需要安装freeTDS。

## pymssql

    import pymssql
    conn = pymssql.connect(server, user, password, database, timeout, login_timeout, charset, as_dict, appname, port)
    # charset='utf-8'
    # as_dict, appname, port 三个是关键字选项。
    # as_dict=true 表示每行以字典的形式返回，而不是默认的元组。
    cursor = conn.cursor()
    cursor.execute(SQL)
    ...
    cursor.close()
    conn.close()

debug:

<https://msdn.microsoft.com/en-us/library/dd327979.aspx?f=255&MSPPError=-2147217396>

(7391, 'The operation could not be performed because OLE DB provider "SQLNCLI10"
for linked server "euedcapp0049.edc.eu.corp" was unable to begin a distributed
transaction.DB-Lib error message 7391, severity 16:\nGeneral SQL Server error:
Check messages from the SQL Server\n')

## pyodbc

windows配置odbc即可，linux需要安装配置ODBC.

<https://msdn.microsoft.com/en-us/library/hh568449.aspx>
<http://www.unixodbc.org/>
<https://msdn.microsoft.com/en-us/library/hh568454.aspx>
<https://msdn.microsoft.com/en-us/library/hh568451.aspx>
<https://www.devart.com/odbc/sqlserver/download.html>

导入

    import pyodbc

windows连接

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=testdb;UID=me;PWD=pass')

linux连接

    cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=localhost;PORT=1433;DATABASE=testdb;UID=me;PWD=pass;TDS_Version=7.0')

通过ODBC配置了DSN的连接

    cnxn = pyodbc.connect('DSN=DataSourceName;UID=user;PWD=password')

使用

    cursor = cnxn.cursor()
    cursor.execute(SQL)
    ...
    cursor.close()
    cnxn.close()

***

# java

<https://msdn.microsoft.com/library/mt484311.aspx>

需要安装sqljdbc才能通过java访问mssql数据库

    Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
    String connectionUrl = "jdbc:sqlserver://localhost;database=AdventureWorks;integratedSecurity=true;"
    Connection con = DriverManager.getConnection(connectionUrl);

## Installation Instructions for the Microsoft Windows version of the JDBC Driver

Note: By downloading the Microsoft JDBC Driver 6.0 (Preview), 4.2, 4.1, or 4.0
for SQL Server, you are accepting the terms and conditions of the End-User
License Agreement (EULA) for this component. Please review the End-User License
Agreement (EULA) located on this page and print a copy of the EULA for your
records.

1. Download sqljdbc_<version>_<language>.exe to a temporary directory.

2. Run sqljdbc_<version>_<language>.exe.

3. Enter an installation directory when prompted. We recommend that you unpack
   this zip file in %ProgramFiles% with the default directory: "Microsoft JDBC
   Driver x.x for SQL Server".

## Installation Instructions for the UNIX version of the JDBC Driver

1. Download sqljdbc_<version>_<language>.tar.gz to a temporary directory.

2. To unpack the zipped tar file, navigate to the directory where you want
   the driver unpacked and type gzip -d sqljdbc_<version>_<language>.tar.gz.

3. To unpack the tar file, move it to the directory where you want the
   driver installed and type tar –xf sqljdbc_<version>_<language>.tar.
