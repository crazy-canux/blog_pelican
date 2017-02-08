---
layout: post
title: Python之InternetProtocols
comments: true
date: 2016-08-12 14:21:36
updated:
tags:
categories:
- Python
permalink:
---

# Internet Protocols and Support

## webbrowser

## cgi

## cgitb

## wsgiref

***

# mail标准库

python邮件服务器MTA：smtp协议

python客户端MUA：本地协议pop3, 远程协议imap

## smtplib

    import smtplib

## smtpd

## poplib

## imaplib

***

# nntp标准库

network news transfer protocol

## nntplib

    import nntplib

***

# telnet标准库

## telnet

    import telnetlib

***

# ftp标准库

## ftplib

***

# xml库

## xmlrpclib

## SimpleXMLRPCServer

## DocXMLRPCServer

***

# url库

URL: Uniform Resource Locator

URI: Universal Resource Identifier

> prot_sch://net_loc/path;params?query#frag
> prot_sch: http/https/ftp/file
> net_loc: username:password@host:port
> path: /path/to/path
> params: options arguments
> query: connector&key-value
> frag:

python2的url标准库：
1. urlparse
2. urllib
3. urllib2

python3的url标准库：
1. urllib

## urllib

## urllib2

## urlparse

***

# http库

python2的http标准库
1. httplib for client
2. BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, cookielib, Cookie for server

python3的标准库
1. http

## httplib

## BaseHTTPServer

## CGIHTTPServer

## SimpleHTTPServer

## cookielib

## Cookie

