---
layout: post
title: Html之Form
comments: true
date: 2016-10-31 04:00:49
updated:
tags:
categories:
- Web
- Html
permalink:
---

# html表单

html表单用于搜集不同类型的用户输入。

# form

form元素定义html表单。支持全局属性和事件属性。

    <form action="action_page.py">
    <fieldset>
    <legend>Form information:</legend>
    First name:<br>
    <input type="text" name="firstname">
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    </fieldset>
    </form>

    # accept-charset属性规定服务器可处理的表单数据字符集。

    # action属性规定当提交表单时向何处发送表单数据。
    <form action="action_page.py">

    # autocomplete属性规定是否启用表单的自动完成功能
    on/off

    # enctype属性规定在发送表单数据之前如何编码
    application/x-www-form-urlencoded
    multipart/form-data
    text/plain

    # method属性规定用于发送form-data的http方法
    get/post

    # name属性规定表单名称
    # novalidate属性规定提交表单时不验证

    # target属性规定在何处打开URL。
    _blank/_self/_parent/_top

# input

input元素是最重要的表单元素。支持全局属性和事件属性。

    # type属性规定输入元素类型
    button
    checkbox
    file
    hidden
    image
    password
    radio
    reset
    submit
    text

    # name属性定义input元素名称
    # value属性定义input元素默认值
    readonly
    disabled
    size
    maxlength
    alt
    accept
    checked
    src

    autocomplete
    autofocus
    form
    formaction
    formenctype
    formmethod
    formnovalidate
    formtarget
    height
    width
    list
    max
    min
    multiple
    pattern
    placeholder
    required
    step

***

# fieldset

fieldset元素组合表单中的相关数据，支持全局属性和事件属性

    # disable属性规定应该禁用fieldset
    # form属性规定fieldset所属的一个或多个表单。
    # name属性规定fieldset名称。

# legend

legend元素为fieldset元素定义标题，支持全局属性和事件属性,支持样式。

***

# select

定义下拉列表。支持全局属性和事件属性。

    <form action="action_page.py">
    <select name="cars">
    <option value="volvo">volvo</option>
    <option value="audi">audi</option>
    </select>
    </form>

    # autofocus属性规定在页面加载后文本区域自动获得焦点
    # disable
    # form
    # multiple
    # name
    # required
    # size

# option

定义选项。支持全局属性和事件属性。

    # disabled
    # label
    # selected
    # value

***

# button

定义可点击的按钮，支持全局属性和事件属性。

    <button type="button" onclick="alert("hello world")">Click Me</button>

    # name属性规定按钮名称
    # type属性规定按钮类型
    # value属性规定按钮初始值
    # autofocus
    # disabled
    # form
    # formaction
    # formenctype
    # formmethod
    # formnovalidate
    # formtarget

***

# textarea

***

# datalist

# keygen

# output
