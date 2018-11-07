Title: Javascript_DOM
Date: 2017-03-15 09:36:32
Tags: Javascript, DOM



# DOM

DOM: document object model.

当网页被加载时，浏览器会创建页面的文档对象模型(DOM).

dom的对象: document/element/attribute/event.

js可以通过DOM访问html文档的所有元素.

* JavaScript 能够改变页面中的所有 HTML 元素
* JavaScript 能够改变页面中的所有 HTML 属性
* JavaScript 能够改变页面中的所有 CSS 样式
* JavaScript 能够对页面中的所有事件做出反应

## 查找html元素

找到返回该元素的对象，没找到返回null.

通过id:

    document.getElementById("id");

通过标签名:

    document.getElementsByTagName("tag");

通过类名:

    document.getElementsByName("name")

## 操作html元素

直接改变html内容:

    # 绝不要使用在文档加载之后使用 document.write()。这会覆盖该文档
    document.write(...);

改变元素的内容:

    document.getElementById(id).innerHTML = "new text";

## 操作html属性

改变元素属性:

    document.getElementById(id).attribute = "new value";

## 操作css

    document.getElementById(id).style.property = "new style"

## 对事件做出反应

    function changetext(id) {
        id.innerHTML = "new text"
    }
    <h1 onclick="changetext(this)"></h1>

    document.getElementById(id).onclick=function(){...};

windows事件:

    onload
    onunload

鼠标事件:

    onclick
    ondblclick
    onmouseover

键盘事件:

    onkeypress

表单事件:

    onsubmit

媒体事件:

## 增删html元素

增加元素:

    var para = document.createElement("p");
    var node = document.createTextNode("new para");
    para.appendChild(node);

删除元素:

    var parent = document.getElementById("id");
    var child = document.getElementById("cid");
    parent.removeChild(child);

***

# Document

集合:

    all[]
    anchors[]
    applets
    forms[]
    images[]
    links[]

attribution:

    body
    cookie
    domain
    lastModified
    referrer
    title
    URL

method:

    close()
    getElementById()
    getElementsByName()
    getElementsByTagName()
    open()
    write()
    writeln()

***

# Element

***

# Attribute

***

# Event
