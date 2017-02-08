---
layout: post
title: Html
comments: true
date: 2016-06-23 09:40:39
updated:
tags:
- web
- html
categories:
- Web
- Html
permalink:
---

# HTML

HTML是超文本标记语言

# XHTML

XHTML是更严谨的更纯净的HTML

# HTML5

HTML5是下一代HTML

***

# html元素和属性

html元素指从开始标签到结束标签的所有代码,包括元素内容：

html元素可以嵌套。

    <p> This is paragrph </p>
    <p></p> # 空内容的元素
    <br /> # 空元素，在开始标签中关闭

html标签可以拥有属性，属性总是以name='value'的形式出现，属性总是在html元素的开始标签中规定。

    <a href="http://www.test.com">This is a link</a>

html属性和值大小写不敏感，推荐使用小写,始终给属性值加引号。

## html的全局属性(标准属性)

参考：

<http://www.w3school.com.cn/tags/html_ref_standardattributes.asp>

## html的事件属性

参考：

<http://www.w3school.com.cn/tags/html_ref_eventattributes.asp>

## html字符实体

参考：

<http://www.w3school.com.cn/tags/html_ref_entities.html>

***

# DOCTYPE

    # 文档类型
    <!DOCTYPE html>
    <html>

    <head>
    ...
    </head>

    <body>
    ...
    </body>

    </html>

# 注释

    # 注释, 浏览器会忽略注释,没有任何属性
    <!-- This is a comment -->

# html

    # html文档,支持全局属性
    <html>
    ...
    </html>

    # mainfest属性，定义一个url，描述文档缓存信息

    # xmlns属性，定义XML的namespace属性

***

# html头部

## head

可以在head标签中使用的标签： link, style, base, meta, script, title.

    # html文档的头部, head支持全局属性
    <head>
    <base>
    <meta>
    <script>
    <title>
    ...
    </head>

    # profile属性

## title

定义文档标题，支持全局属性。

    # dir属性规定元素中内容的文本方向
    # lang属性规定元素中内容的语言编码
    # xml:lang属性规定xhtml文档中元素内容的语言编码

## base

定义页面所有的链接的默认地址和默认目标。

    # href属性规定页面中所有相对链接的基准url
    # target属性规定在何处打开页面中的链接

## meta

定义元数据,支持全局属性

    # content属性
    # http-equiv
    # name
    # scheme

***

## body

    # html文档的主体, 支持样式，支持全局属性和事件属性
    <body>
    ...
    </body>

## h1-h6

    # 标题,浏览器会自动在标题前后添加空行,支持样式
    <h1>This is the max heading</h1>
    ...
    <h6>This is the min heading</h6>

    # 支持部分全局属性
    # id,class,title,style,dir,lang,xml:lang

    # 支持部分事件属性
    # onclick,ondblclick,onmousedown,onmouseup,onmouseover,
    # onmousemove, ommouseout,onkeypress,onkeydown,onkeyup

## hr

    # 水平线分割线，支持样式，支持全局属性和事件属性
    <hr />

***

# html段落

## p

    # 段落, 浏览器会自动在段落前后添加空行,支持样式，支持全局属性和事件属性
    <p>This is a paragraph</p>

## br

    # 空行, 支持全局属性和事件属性
    <br />

    # clear属性

***

# 链接和图像

URL: Uniform Resource Locator

    scheme://host.domain:port/path/filename
    scheme: http/https/ftp/file

url只能使用ASCII字符集。

参考：

<http://www.w3school.com.cn/tags/html_ref_urlencode.html>

## a

支持全局属性和事件属性

    # href属性定义指向另一个文档的链接
    <a href="http://www.test.com">Click me as link</a>

    # target属性，定义被链接的文档在何处显示, blank在新窗口显示,rect, circle, poly
    <a href="http://www.test.com" target="_blank">Link</a>

    # name属性定义文档内的书签
    <a href="http://www.test.com" name="label">Link</a>

    # hreflang

    # rel

    # download

    # media

    # type

## img

支持全局属性和事件属性

    # src属性定义源
    <img src="url" />

    # alt属性，当图像不能显示，就显示alt的默认值。
    <img src="http://www.test.com/images/test.img" alt="default value"/>

    # height

    # ismap

    # longdesc

    # usemap

    # width

## map

支持全局属性和事件属性

    # id属性为map定义唯一的名称
    <map id="planetmap">
    ...
    </map>

    # name属性为image-map规定的名称

## area

支持全局属性和事件属性

    # alt
    # coords
    # href
    # nohref
    # shape
    # target

***

# html样式

内联样式,定义在html元素内部。style样式属性可以包含任何的css属性。

内联样式优先级最高。

    <h1 style="font-family:verdana">A heading</h1>
    <p style="font-family:arial;color:red;font-size:20px">A paragraph</p>

## style

内部样式表,位于head标签内部。支持全局属性和事件属性

优先级仅次于内联样式。

    <head>
    <style type="text/css">
    h1 {color: red}
    p {color: blue}
    </style>
    </head>

    # type属性规定样式表的MIME类型

    # media属性规定不同的媒体类型

## link

外部样式表,支持全局属性和事件属性

优先级仅高于浏览器缺省值。

    <head>
    <link rel="stylesheet" type="text/css" href="mystyle.css">
    </head>

    # href属性规定被链接文档的位置
    # hreflang属性规定被链接文档中文本的语言
    # media属性规定被链接文档被显示在什么设备
    # rel属性规定当前文档与被链接文档的关系
    # sizes属性规定rel='icon'的尺寸
    # type属性规定被链接文档的MINE类型

## div

分类块级元素,支持样式，支持全局属性和事件属性

    <div> 使用样式属性

## span

分类行内元素，支持样式，支持全局属性和事件属性

    <span> 定义文档中的行内的块

***

# html格式化

## 文本格式化标签

    <b> 定义粗体文本
    <big> 定义大号字
    <em> 定义着重文字
    <i> 定义斜体字
    <small> 定义小号字
    <strong> 定义加重语气
    <sub> 定义下标字
    <sup> 定义上标字
    <ins> 定义插入字
    <del> 定义删除字

## 计算机输出标签

    <code> 定义计算机代码
    <kbd> 定义键盘码
    <samp> 定义计算机代码样本
    <tt> 定义打字机代码
    <var> 定义变量
    <pre> 定义预格式文本

## 引用和术语标签

    <abbr> 定义缩写
    <p><abbr title="Hyper Text Markup Language">HTML</abbr>is perfect.</p>

    <acronym> 定义首字母缩写
    <address> 定义地址
    <bdo> 定义文字方向
    <blockquote> 定义长的引用
    <q> 定义短的引用
    <cite> 定义著作的标题
    <dfn> 定义一个项目或缩写

***

# 表格

    <table border="1">
    <caption>The title</caption>
      <tr>
        <th>Month</th>
        <th>Saving</th>
      </tr>
      <tr>
        <td>Jan.</td>
        <td>$100</td>
      </tr>
    </table>

## table

定义表格,支持事件属性和全局属性

    # border属性规定表格边框宽度
    # cellpadding属性规定单元边沿与其内容之间的空白
    # cellspacing属性规定单元格之间的空白
    # frame属性规定外侧边框的哪个部分是可见的
    # rules属性规定内侧边框的哪个部分是可见的
    # summary属性规定表格的摘要
    # width属性规定表格的宽度

## caption

定义表格标题,支持样式，支持事件属性和全局属性

## tr

定义表格的行,支持事件属性和全局属性

    # align属性定义表格内容对齐方式
    # char属性规定根据哪个字符来进行文本对齐
    # charoff属性规定第一个对齐字符的偏移量
    # valign属性规定表格中内容的垂直对齐方式

## th td

th定义表格表头,支持全局属性和事件属性

td定义表格单元,支持全局属性和事件属性

    # abbr属性规定单元格中内容的缩写版本
    # align属性规定单元格内容的水平对齐方式
    # axis属性对单元进行分类
    # char
    # charoff
    # colspan
    # headers
    # rowspan
    # scope
    # valign

## col

定义用于表格的属性

## colgroup

定义表格的组

***

# 列表

## ol

定义有序列表,支持全局属性和事件属性

    <ol>
      <li>first one</li>
      <li>second one</li>
    </ol>

    # reversed属性规定列表顺序为降序
    # start属性有序列表的起始值
    # type属性规定在列表中使用的标记类型

## ul

定义无序列表,支持样式，支持全局属性和事件属性

    <ul>
      <li>coffee</li>
      <li>tea</li>
    <ul>

## li

定义列表项,支持样式，支持全局属性和事件属性

## dl dt dd

dl定义定义列表,dt定义定义项目,dd定义定义的描述,都支持全局属性和事件属性

    <dl>
      <dt>computer</dt>
      <dd>used to monitor...</dd>
    </dl>

***

# 网站布局

使用html5的网站布局标签.

    <head>
    <style>
    header {}
    nav {}
    section {}
    footer {}
    </style>
    </head>

    <body>
    <header>...</header>
    ...
    <footer>...</footer>
    </body>

也可以使用id选择器：

    <head>
    <style>
    #header {}
    ...
    #footer {}
    </head>
    </style>

    <body>
    <div id="header">...</div>
    ...
    <div id="footer">...</div>
    </body>

## header标签

## nav标签

## section标签

## article标签

## aside标签

## footer标签

## details标签

## summary标签

***

# 框架

框架可以在一个html添加多个页面。

垂直框架：

    <frameset cols="50%, 50%">
      <frame src="a.html">
      <frame src="b.html">
    </frameset>

水平框架：

    <frameset rows="50%, 50%">
      <frame src="a.html">
      <frame src="b.html">
    </frameset>

混合框架：

    <frameset rows="50%, 50%">
    <frame src="a.html">

    <frameset cols="%25, 75%">
    <frame src="b.html">
    <frame src="c.html">
    </frameset>

    </frameset>

## frameset标签

    # cols属性定义框架中列的数目和尺寸
    # rows属性定义框架中行的数目和尺寸

    # 标准属性：
    id,class,title,style

## frame标签

定义frameset中的一个特定的窗口。

    # frameborder属性规定是否现实框架周围的边框
    # longdesc属性
    # marginheight属性
    # marginwidth属性
    # name属性
    # scrolling属性
    # src属性

    # 标准属性：
    id,class,title,style

## iframe标签

内联框架。

把内容放在iframe标签中，在无法理解iframe的浏览器显示。

支持事件属性和全局属性。

    # frameborder属性
    # height属性
    # width属性
    # longdesc属性
    # marginheight属性
    # marginwidth属性
    # name属性
    # scrolling属性
    # src属性
    # sandbox
    # seamless
    # srcdoc

***

# 脚本

在html中插入javascript脚本。

## script标签

定义客户端脚本，支持全局属性

    <script type="text/javascript">
    document.write("hello javascript")
    </script>

    # type属性指定脚本MIME类型
    # async
    # charset
    # defer
    # src

## noscript标签

为不支持客户端脚本的浏览器定义替代内容,支持全局属性

    <noscript>Your browser does not support javascript</noscript>
