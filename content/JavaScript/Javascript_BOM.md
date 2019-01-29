Title: Javascript_BOM
Date: 2018-03-15 09:36:32
Tags: Javascript, BOM



# BOM

Browser Object Model

介绍浏览器对象，不过缺乏规范.

# window

window对象是最顶层对象，有6大属性,属性本身也是对象.

window对象的document属性也是对象，document对象有5大属性.

引用当前窗口时，可以省略window对象.

eg:

    window.document
    document

    window.alert()
    alert()

对象集合:

    frames[]

attribution:

    document # DOM的Document对象
    history # History对象
    location # Location对象
    Navigator # Navigator对象
    Screen # Screen对象
    window # 等价于self

    closed
    defaultStatus
    status
    innerheight
    innerwidth
    outerheight
    outerwidth

method:

    alert() // 弹出警告框
    confirm() // 和alert差不多，带确定和取消按钮，确定返回true
    prompt() // 输入提示框,返回输入内容
    find() // 查找

    // 子窗口的opener属性反过来引用打开她的那个窗口(父窗口)
    subwin = open() // 打开一个新窗口, _parent在当前窗口打开, 返回子窗口的window对象.
    subwin.opener // 表示window

    moveTo()
    moveBy()
    resizeTo()
    resizeBy()

    setTimeout()
    clearTimeout()

    setInterval()
    clearInterval()

    close()

# location

attribution:

    hash
    host
    hostname
    href
    pathname
    port
    protocol
    search

methods:

    assign()
    reload()
    replace()

# history

attribution:

    lehgth

method:

    back()
    forward()
    go()

# navigator

对象集合:

    plugins[] # Plugin对象的数组
    navigator.plugins.length # 插件个数
    navigator.plugins[i].name # 第i个插件名字
    navigator.plugins[i].filename # 第i个插件文件名

attribution:

    appName # 浏览器名称
    appVersion # 浏览器版本
    userAgent # user-agent 头部信息
    platform # win32/

method:

    javaEnabled()
    taintEnabled()

# screen

attribution:

    width
    height
    availHeight
    availWidth
