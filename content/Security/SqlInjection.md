Title: SQL Injection
Date: 2018-07-28 16:08:54
Tags: Security, SQLInjection



# SQL Injection

什么是sql injection:从数据库获取敏感信息,或者利用数据库的特性执行添加用户,导出文件等一系列恶意操作,甚至有可能获取数据库乃至系统用户最高权限。

原因:造成SQL注入的原因是因为程序没有有效过滤用户的输入.


预防：

* 严格限制数据库的操作权限
* 检查输入的数据格式是否符合要求
* 对进入数据库的特殊字符进行转义
* 数据库查询语句使用数据库提供的参数化查询接口
* 在发布之前使用专业的sql注入检测工具进行检测
* 避免网站打印sql错误信息

通过表单注入：

    username => myuser' or 'foo' = 'foo' --
    SELECT * FROM user WHERE username='myuser' or 'foo' = 'foo' --'' AND password='xxx'

mssql的sql语句可以执行dos命令:

    exec xp_cmdshell 'net user username 2546 /add' # 新建系统用户
    exec xp_cmdshell 'net localgroup administrator username /add' # 授权
