---
layout: post
title: Css
comments: true
date: 2016-06-23 09:40:45
updated:
tags:
- web
- css
categories:
- Web
- Css
permalink:
---

# CSS

CSS是叠层样式表

# CSS3

CSS3是最新的CSS标准

***

# CSS创建

优先级从上往下。

1. 内联样式， 在html中通过style属性定义，仅用于一个html元素。
2. 内部样式表，在html中通过style标签在头部定义,针对单个页面。
3. 外部样式表，在html中通过link标签在文档头部定义，方便将样式用于多个页面。
4. 浏览器的默认值。

# CSS基本语法

CSS由两部分组成，选择器和声明，选择器是html元素，声明由属性和值组成。

    selector {
      property1: value1;
      property2: value2;
      ...;
    }

多个声明用分号隔开，属性的值有空格要用引号。

CSS对大小写不敏感。

CSS注释:

    /* comment */

***

# 选择器

最常见的选择器是元素选择器,html元素是最基本的选择器。

## 选择器分组

同组的选择器使用相同的声明。

    h1,h2,h3,h4,h5,h6 {
      color: green;
    }

## id选择器

id选择器可以为标有特定id的html元素指定特定样式。

id选择器用#开头定义。

    #red {color: red;}
    #green {color: green;}

    <p id="red">This is red.</p>

id选择器常常用来建立派生选择器：

    #sidebar p {
      font-style: italic;
      text-align: right;
      margin-top: 0.5em;
    }

    <div id="sidebar">...</div>

## 类选择器

和id选择器功能类似，类选择器以.开头。

    .center {text-align: center}

    <h1 class="center">...</h1>

类选择器用于建立派生选择器：

    .fancy td {
      color: #f60;
      background: #666;
    }

    <td class="fancy">

也可以用：

    td.fancy {
      color: #f60;
      background: #666;
    }

    <td class="fancy">

## 属性选择器

为拥有指定属性的html元素设置样式。

    [title]
    {
      color: red;
    }

    <a title="title is red">...</a>

属性和值选择器：

    [title=w3c]
    {
      border: 5px solid blue;
    }

    <img title="w3c" src="/images/w3c.gif">

    # 属性和值选择器的操作符：
    =
    ~=
    |=
    ^=
    $=
    *=

## 后代选择器

## 子元素选择器

## 相邻兄弟选择器

***

# CSS样式

内联样式：

    <p style="background: #ff0000 url(/i/eg_bg_03.gif) no-repeat fixed center">...</h1>

样式表：

    p {
      background: #ff0000 url(/i/eg_bg_03.gif) no-repeat fixed center;
    }

## background样式

    background: # 可以定义所有背景的值

    background-color: gray # 背景颜色
    background-image: url(/images/test.gif) # 背景图片,默认水平和垂直都平铺
    background-repeat: repeat-x # 水平方向平铺
    background-repeat: repeat-y # 垂直方向平铺
    background-repeat: no-repeat # 不平铺
    background-position: center/top/buttom/left/right # 图像在背景中的位置
    background-attachment: fixed # 图像相对于可视区是固定的
    background-size
    background-origin
    background-clip

## 文本样式

    color: red # 设置文本颜色
    line-height # 设置行高
    letter-spacing # 设置字符间距
    word-spacing # 设置字间距
    text-indent # 缩进元素中文本首行
    direction: ltr/rtl # 设置文本方向
    text-align: left/right/center/justify # 对齐元素中的文本
    text-decoration: none/underline/overline/line-through/blink # 向文本添加修饰
    text-transform: none/capitalize/uppercase/lowercase # 控制元素的字母
    white-space: normal/pre/nowrap/pre-wrap/pre-line # 设置元素中空白的处理方式

## 字体样式

    font: # 定义所有和字体有关的属性
    font-family: # 设置字体系列
    font-size:  # 设置字体尺寸
    font-style: normal/italic/oblique # 设置字体风格
    font-variant: normal/small-caps # 设置字体变体
    font-weight: normal/bold/bolder/lighter/... # 设置字体粗细

## 链接样式

链接可以设置background，color，font等样式。

    a:link {background: red} # 普通的未被访问的链接
    a:visited {color: blue} # 用户已访问的链接
    a:hover {font: } # 鼠标指针位于链接的上方
    a:active {font: } # 链接被点击的时刻

## 列表样式

    list-style: # 定义所有和列表相关的属性
    list-style-image: # 把图像设置为列表项标志
    list-style-position: inside/outside # 设置列表项标志的位置
    list-style-type: # 设置列表项标志的位置

## 表格样式

    border-collapse: separate/collapse # 设置是否把表格边框合并为单一的边框
    border-spacing: # 设置分割单元边框距离
    caption-side: top/bottom # 规定表格标题设置方式
    empty-cells: hide/show # 设置是否现实表格中的空单元格
    table-layout: automatic/fixed # 设置现实单元，行和列的算法

## 轮廓样式

    outline: # 设置所有和轮廓相关的属性
    outline-color: # 设置轮廓颜色
    outline-style: none/dotted/dashed/solid/double/groove/ridge/inset/outset # 设置轮廓风格
    outline-width: # 设置轮廓宽度

***
