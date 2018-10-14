Title: Oracle
Date: 2016-06-01 22:40:22
Tags: Database, Oracle

# Oracle

oracle的GUI：
1. oracle sql developer(officer)
2. pl/sql
3. toad

oracle的CLI：
1. sqlplus

# Oracle命令

sys是oracle默认管理员权限

    $ sqlplus / as sysdba

system是oracle的默认最高权限，默认密码是manager，需要sys授权才能登陆

    $ sqlplus / as sysdba
    > alter user system account unlock;
    > alter user system identified by manager;
    > conn system/manager

scott是oracle的默热你的普通用户，默认密码是tiger，需要sys授权才能登陆

    $ sqlplus / as sysdba
    > alter user scott account unlock;
    > alter user scott identified by tiger;
    > conn scott/tiger

本地命令行执行sql语句：

    $ <sql query> | <sqlplus> <db user>/<db password>@<db sid> | sudo ORACLE_HOME=<oracle home> -i -u <oracle user>

dbsnmp是oracle的用户智能代理用户，用来监控和管理数据库相关性能。

sysman是oracle的数据库用户EM管理用户。

监听管理：

    su - oracle
    lsnrctl start
    lsnrctl stop
    lsnrctl status

# CLI

先用sqlplus命令进入oracle的命令行．

    help index
    ? index

查看命令帮助信息：

    help <command>

登陆和退出sqlplus：

    sqlplus
    exit/quit

调用sql语句：

    @

不退出sqlplus执行shell命令：

    host

用户登陆和退出：

    connect/conn <username>/<password>
    disconnect

清屏：

    clear
    ! clear
    clear scr

修改密码：

    password

查看变量：

    show

***

# 数据类型

***

# 函数

isnull函数:

　　　　NVL(column, 0)    column为null函数返回0

***

# SQL

创建用户：

    CREATE USER <username> IDENTIFIED BY <password>;

用户授权：

    GRANT DBA TO <username>;
    GRANT UNLIMITED TABLESPACE TO <username>;
    GRANT SELECT ANY TABLE TO <username>;
    GRANT SELECT ANY DICTIONARY TO <username>;

常用查询：

    SELECT * FROM global_name; 查看默认数据库
    SELECT * FROM dba_tables; DBA权限查询数据所有表
    SELECT * FROM all_users; 查看所有用户
    SELECT username FROM dba_users; 查看所有DBA用户
    SELECT user FROM dual; 查看当前登陆用户
    SELECT * FROM user_tables; 查询当前用户有哪些表
    SELECT * FROM all_tables; 查询当前用户可以访问的所有表
    SELECT banner FROM sys.v_$version; 查询数据库版本
    SELECT count(*) FROM v$version; 查询oracle连接数
    SELECT count(*) FROM v$version WHERE STATUS = 'ACTIVE'; 查询oracle并发连接数
    ALTER system SET processes = <number> scope = spfile; 修改数据库允许最大连接数
    SELECT value FROM v$parmeter WHERE name = 'processes'; 查询数据库允许最大连接数
    SELECT value FROM v$parmeter WHERE name = 'open_cursor'; 查询数据库允许最大游标数

***

# python

## cx_Oracle

<http://cx-oracle.sourceforge.net/>

需要安装oracle数据库或者oracle instant client并设置环境变量。

参考oracle网站下载安装配置oracle instant client

<http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html>

    import cx_Oracle

***

