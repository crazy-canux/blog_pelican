---
layout: post
title: reStructuredText
comments: true
date: 2016-08-08 13:39:38
updated:
tags:
- reST
categories:
- Web
permalink:
---

# reStructuredText

<http://docutils.sourceforge.net/rst.html>

reST是易读所见即所得的文本标记语言，格式类似markdown。

主标题：

    Title
    =====

    =====
    Title
    =====

副标题：

    Subtitle
    -----

    --------
    Subtitle
    --------

次级标题：

    Content
    ^^^^^^^

星号斜体强调：

    *text*

双星号加粗重点强调：

    **text**

四个或以上的-表示分割线：

    ----

参考式链接：

    `hyperlink`_

    .. _hyperlink: http://hyperlink.org

行内式链接：

    `link <https://link.com>`_

图片：

    .. image:: https://path/image.png
        :alt: HTTPie compared to cURL
        :width: 679
        :heigh: 781
        :align: center

原样引用块：

双冒号加四个空格

    source code::

        print("source")
        return 0

文档测试块：

    >>> print doctest block.

无序列表：

    bullet lists:

    - This is item 1
    - This is item 2

有序列表：

    enumerated lists:

    1. this is first item
    2. this is second item

定义列表：

    definition lists:

    what
        Definition lists.

    how
        The term is a one-line phrase.

域列表：

    field lists:

    :Authors:
        Canux

    :Version: 1.0.0

选项列表：

    option lists:

    -a    option "a"
    -b file    option for filename

评论：

    .. This is commnet.
       As well.
