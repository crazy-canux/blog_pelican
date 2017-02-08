---
layout: post
title: Markdown
comments: true
date: 2016-03-28 22:03:15
updated:
tags:
- Markdown
categories:
- Web
permalink:
---

# Markdown

## Markdown简介

Markdown是一种轻量级文本标记语言, Markdown的目标是实现易读易写。
Markdown和html有很大区别，html是一种发布格式，markdown是一种书写格式。

Markdown 中文手册：

<http://wowubuntu.com/markdown/index.html>

Markdown 英文手册：

<http://daringfireball.net/projects/markdown/syntax>

Markdown文件的扩展名是md。

## 两个需要特殊处理的字符

< 的表示方法：
> & l t ;

& 的表示方法：
> & a m p ;

***

# 区块元素

## 段落和换行

段落前后要有一个或以上的空行（空格或制表符都可以）。

## 标题

markdown支持两个语法格式的标题

### setext格式

任意个数下等号=表示大标题:

    Title
    ======

任意个数下减号表示副标题：

    Subtitle
    --------

### atx格式

一到六个#表示一到六阶标题,#后面有空格

    # 一阶标题

    ## 二阶标题

    ### 三阶标题

    #### 四阶标题

    ##### 五阶标题

    ###### 六阶标题

## 区块引用

使用>表示单层区块引用：

\> block
> block

使用多个>嵌套使用：

\>\> block
>> block

区块内也可以用标题，列表和代码区块等。

## 列表

### 无序列表

无序列表使用星号、加号或是减号作为列表标记,符号和字符之间有空格：

\* shopping list
> * shopping list

\+ shoppint list
> + shopping list

\- shopping list
> - shopping list

### 有序列表

有序列表使用数字和一个英文句点,符号和字符之间有空格：

1. numbered list
> 1. numbered list

## 代码区块

简单地缩进 4 个空格或是 1 个制表符,一个代码区块会一直持续到没有缩进的那一行或是文件结尾。

这是一个普通段落：

    这是一个代码区块。
        缩进
    代码区块结束。

## 分割线

三个以上的*-_都可以产生分割线:

\*\*\*
> ***

\-\-\-
> ---

\_\_\_
> ___

***

# 区段元素

## 链接

### 行内式链接

\[Link](https://github.com/crazy-canux)
> [Link](https://github.com/crazy-canux)

### 参考式链接

\[Link]\[id]

\[id]:https://github.com/crazy-canux

### 自动链接

网址:

&lt;https://github.com/crazy-canux>

> <https://github.com/crazy-canux>

邮箱：

&lt;canuxcheng@gmail.com>

> <canuxcheng@gmail.com>

## 强调

用一个*或_表示强调，符号和字符中间没有空格

斜体：\*italic\*
> *italic*

斜体： \_italic\_
> _italic_

粗体： \*\*bold\*\*
> **bold**

粗体： \_\_bold\_\_
> __bold__

## 代码

用反引号标记一小段代码：

\`monospace\`
> `monospace`

## 图片

### 行内式图片

\!\[pic](/path/to/img.jpg)
> ![Pic](/path/to/img.jpg)

### 参考式图片

\!\[pic]\[id]

\[id]: /path/to/img.jpg

***

# 反斜线

用反斜线\来转移字符

\\   反斜线

\`   反引号

\*   星号

\_   底线

\{}  花括号

\[]  方括号

\()  括弧

\#   井字号

\+   加号

\-   减号

\.   英文句点

\!   惊叹号
