---
layout: post
title: Python之InternetData
comments: true
date: 2016-08-14 21:22:40
updated:
tags:
categories:
- Python
permalink:
---

# Internet Data Handling

## email

## json

http的get和post一般返回json格式数据，类似于字典形式的字符串类型。

    import json
    json_data = json.dumps(dict_data) # dict类型变成json类型
    dict_data = json.loads(json_data) # json类型变成dict类型

## mailcap

## mailbox

## mimetypes

## base64

## binhex

## binascii

## quopri

## uu

***

# Structed Markup Processing Tools

## HTMLParser

HTML和XHTML解析器

python3中更名为html.parser

## htmlentitydefs

html定义通用实体

python3更名为html.entities

## xml

XML解析器
