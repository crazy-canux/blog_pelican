Title: MongoDB
Date: 2017-04-16 14:46:14
Tags: Database, NoSQL, MongoDB



# MongoDB

<https://github.com/mongodb/mongo>

mongodb是一种开源的文档数据库，高性能，高可用性，自动裁剪．

mongodb的database和关系数据库中的database一样．

mongodb将BSON(mongo的JSON)文档存储在集合(collections)中，集合相当于关系数据库中的表table．

mongodb的collections中的域(field)，相当于关系数据库中的字段column.

mongodb的collections中的文档(document)，相当于关系数据库中的记录行row.

mongodb也支持index索引和primary key主键，但是不支持table joins表连接．

ubuntu安装:

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv0C49F3730359A14518585931BC711F9BA15703C6
    $ echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org

ubuntu启动:

    $ sudo service mongod start

安装完成默认的数据库是test.另外db, admin, local是保留的数据库名称．

mongod的默认端口是27017.

***

# mongo的命令

    mongo [options] [db address] [file names (ending in .js)]

mongo shell进入到指定数据库:

    $ mongo [db_name]

本地命令行执行sql语句：

    $ mongo [database] -e/--eval [javascript]

远程执行sql语句:

    $ mongo -u [username] -p [password] [ip]:[port]/[datbase] -e/--eval [javascript]

***

# CLI

先用mongo命令进入mongo命令行

    help    # 查看所有命令
    exit    # 退出mongo shell

    db    # 显示当前数据库

    show dbs    # 查看所有数据库
    db.help() # 查看所有database的方法

    show collections # 查看当前database的collections
    db.mycoll.help() # 查看所有collections的方法

    use <db_name>    # 切换到指定数据库, 不存在则创建．

***

# 数据类型

***

# CURD

mongo的CURD操作就相当于关系数据库中的sql操作．

CURD: create update read delete.

    > use <database_name> # 创建数据库
    > db.createCollection(collection_name) # 在当前数据库创建集合
    > db.dropDatabase() # 删除当前数据库
    > db.getCollectionNames() # 获取当前数据库的所有集合

    > db.mycollection.insert(obj) #　往集合mycollection中插入JSON对象obj.
    > db.mycoll.find([query],[fields]) # 查询文档
    > db.mycoll.remove(query) # 删除文档
    > db.mycoll.save(obj) # 替换已有的文档
    > db.mycoll.update( query, object[, upsert_bool, multi_bool] ) # 更新已有的文档
    > db.mycoll.drop() # 删除当前集合

***

# Python

<https://github.com/mongodb/mongo-python-driver>

    $ pip install pymongo

    from pymongo import MongoClient
    client = MongoClient("mongodb://mongodb0.example.net:27017")

***

# Java
