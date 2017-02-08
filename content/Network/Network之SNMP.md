---
layout: post
title: Network之SNMP
comments: true
date: 2016-04-26 09:56:04
updated:
tags:
- snmp
- network
categories:
- Network
permalink:
---

# SNMP

Simple Network Management Protocol, 简单网络管理协议

MIB
SMI

# 安装和配置snmp

    sudo apt-get install snmp snmpd

***

# Python

## pysnmp

python的snmp包[pysnmp](https://github.com/etingof/pysnmp)

    import pysnmp

## netsnmp

[netsnmp](http://net-snmp.sourceforge.net/wiki/index.php/Python_Bindings)是[net-snmp](http://www.net-snmp.org/)内置的包。

需要安装net-snmp才能安装使用python包netsnmp。

***

# java

## snmp4j

java的snmp包[snmp4j](http://www.snmp4j.org/)

<http://www.snmp4j.org/doc/index.html>

    import org.snmp4j.*
