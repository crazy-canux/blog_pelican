---
layout: post
title: Network
comments: true
date: 2016-04-03 14:46:19
updated:
tags:
- network
categories:
- Network
permalink:
---

# 网络基础

小端： 低字节在起始地址，高字节在高地址

大端： 高字节在起始地址，低字节在高地址

linux一般是小端，unix一般是大端

# 网络模型

## 传输层

TCP：传输控制协议，提供可靠的、面向连接的字节流服务。

    # 基于TCP的应用层
    FTP: 21,
    SSH: 22,
    Telnet: 23,
    SMTP: 25,
    DNS: 53,
    HTTP: 80,
    HTTPS: 443,
    POP3: 110,
    POP3 SSL: 995
    IMAP: 143,
    IMAP SSL: 993,
    NNTP: 119,
    NNTP SSL: 563,

UDP：数据报协议，提供不可靠的、面向数据报的服务。

    # 基于UDP的应用层
    SMTP: 25,
    DNS: 53,
    DHCP: 67,
    TFTP：69,简单文件传输协议。
    NTP/SNTP: 123,
    SNMP：161,简单网络管理协议。
    SNMPtrap: 162,

SCTP：流控制传输协议。

## 网络层

IP：网际协议，提供不可靠、无连接的数据报传送服务。

ICMP：Internet控制报文协议，传递差错报文和需要注意的信息，封装在IP数据报内部。

    # 基于ICMP的应用层：
    Ping:

IGMP：Internet组管理协议，用于支持主机和路由器进行多播，让一个物联网络上的所有系统知道主机当前所在的多播组，封装在IP数据报内部。

## 链路层

以太网帧结构：以太网首部+IP首部+TCP/UDP首部+应用数据+以太网尾部。

ARP：地址解析协议，为IP地址到硬件地址之间提供动态映射。

RARP：没有磁盘驱动器的系统使用。

## 动态选路协议

RIP：选路信息协议

OSPF：开放最短路优先

IGP-EGP-BGP：边界网关协议

CIDR：无类型域间选路

***

# File

File协议是本地文件协议

    file:///C:/

***

# NFS

NFS: network file system.

# SMB/CIFS

SMB/CIFS占用TCP和UDP的139和445端口。

SMB: server message block.

CIFS: common internet file system, 是SMB的升级版本。

# Samba

Samba: Linux/Unix上的SBM/CIFS,用于跨平台的共享。

***

# 远程桌面协议

RDP: remote desktop protocol， windows系统之间的远程桌面协议。

RFB(VNC): remote frame buffer, 跨平台的远程桌面协议，cs架构。

VNC: 跨平台的RFB（VNC）工具有realvnc, tightvnc, tigervnc.

remmina：基于gtk，支持RFB(VNC), RDP, SSH/SFTP协议。

krdc：基于kde，支持RFB(VNC), RDP协议。

***

# LDAP

LDAP占用tcp和udp的389端口。

使用SSL的LDAP占用tcp和udp的636端口。

Lightweight Directory Access Protocol.

<http://www.openldap.org/>

LDAP的windows工具：LDAPSoft LDAP Browser

## python

### python-ldap

<https://www.python-ldap.org/>

### pyldap

<https://github.com/pyldap/pyldap>
