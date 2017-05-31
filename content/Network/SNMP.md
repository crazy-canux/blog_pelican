Title: SNMP
Date: 2016-04-26 09:56:04
Tags: SNMP



# SNMP

Simple Network Management Protocol, 简单网络管理协议

MIB

SMI

安装和配置snmp:

    $sudo apt-get install snmp snmpd

***

# snmp命令

***

# Python的第三方库

## pysnmp

python的snmp包[pysnmp](https://github.com/etingof/pysnmp)

    import pysnmp

## netsnmp

[netsnmp](http://net-snmp.sourceforge.net/wiki/index.php/Python_Bindings)是[net-snmp](http://www.net-snmp.org/)内置的包。

net-snmp的源代码内置一个python目录就是netsnmp的python包．

***

# java的第三方库

## snmp4j

java的snmp包[snmp4j](http://www.snmp4j.org/)

<http://www.snmp4j.org/doc/index.html>

    import org.snmp4j.*
