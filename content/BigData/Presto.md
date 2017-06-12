Title: SQL On Hadoop
Date: 2017-04-24 22:57:37
Tags: Hadoop, Presto



# Presto

<https://github.com/prestodb>

<https://prestodb.io/>

presto的client: presto-cli(rename to presto)


***

# presto-cli

    $ presto --server localhost:8080 --catalog hive --schema default

    # jdbc for presto
    $ jdbc:presto://host:port/catalog/schema
