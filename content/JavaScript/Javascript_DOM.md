Title: Javascript_DOM
Date: 2017-03-15 09:36:32
Tags: Javascript, DOM



# DOM

DOM: document object model.

当网页被加载时，浏览器会创建页面的文档对象模型(DOM).

DOM操作需要在html加载完成后进程.

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

## 操作html元素或文本

操作标签或标签内的文本.

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

## 增删html元素

增加元素:

    var para = document.createElement("p");
    var node = document.createTextNode("new para");
    para.appendChild(node);

删除元素:

    var parent = document.getElementById("id");
    var child = document.getElementById("cid");
    parent.removeChild(child);

## 对事件做出反应

    function changetext(id) {
        id.innerHTML = "new text"
    }
    <h1 onclick="changetext(this)"></h1>

    document.getElementById(id).onclick=function(){...};

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
    readyState // loading/interfactive/complete

method:

    open()
    close()
    getElementById() # 返回id对应的第一个对象
    getElementsByName() # 返回对应的所有对象的集合
    getElementsByTagName() # 同上
    write()
    writeln()
    createElement()
    createTextNode()

***

# Element

element表示html元素,拥有元素，文本和注释的子节点.

attribution:

    tagName // tag名字
    innerHTML // 元素里面的文本内容
    id
    title
    style
    className
    length
    nodeName // 和tagName相同
    nodeType // 节点类型: 1= 元素节点，2= 属性节点, 3= 文本节点, 8= 注释
    nodeValue // 文本节点的值
    parentNode // 父节点
    childNodes // 子节点
    firstChild
    lastChild
    nextSibling
    previousSibling
    ownerDocument // 返回当前根节点文档对象
    accesKey
    attributes
    contentEditable
    dir
    lang
    namespaceURI
    tabIndex
    textContent
    clientHeight
    clientWidth
    offsetHeight
    offsetWidth
    offsetLeft
    offsetParent
    offsetTop
    scrollHeight
    scrollLeft
    scrollTop
    scrollWidth

method:

    appendChild(node) // 在元素后追加node
    InsertBefore() // 在元素前插入node
    removeChild()
    replaceChild()
    cloneNode()

    compareDocumentPosition()
    getAttribute()
    getAttributeNode()
    getElementsByTagName()
    getFeature()
    getUserData()
    hasAttribute()
    hasAttributes()
    hasChildNodes()
    isDefaultNamespace()
    isEqualNode()
    isSameNode()
    isSupported()
    normalize()
    removeAttribute()
    removeAttributeNode()
    setArrbitute()
    setArrtibuteNode()
    setIdAttribute()
    setIdArrtibuteNode()
    setUserData()
    toString()
    item() #

***

# Attribute

Attribute表示html属性

attribution:

    isId
    name
    value
    specified
    length

methods:

    gtNamedItem()
    item()
    removeNameItem()
    setNamedItem()

***

# Event

window事件:

    # 等待html加载完成
    onload
    window.onload = function(){};

    onunload

鼠标事件:

    onclick
    ondblclick
    onmousedown
    onmousemove
    onmouseout
    onmouseover
    onmouseup

键盘事件:

    onkeypress
    onkeydown
    onkeyup

表单事件:

    onsubmit

媒体事件:

    onabort
    onerror

