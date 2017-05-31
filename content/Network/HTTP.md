Title: HTTP
Date: 2016-09-13 01:39:34
Tags: http, https, url, html, xml



# HTTP/HTTPS

http port: 80

https port: 443

http/https的命令：

    get # 从服务器取出资源
    post # 在服务器新建资源
    put # 在服务器更新资源，客户端提供改变后的完整资源
    delete # 从服务器删除资源
    patch # 在服务器更新资源，客户端提供改变的属性
    head # 获取资源的源数据
    options # 获取资源的哪些信息是客户端可以改变的信息

URL: Uniform Resource Locator

URI: Universal Resource Identifier

    prot_sch://net_loc/path;params?query#frag
    prot_sch: http/https/ftp/file
    net_loc: username:password@host:port
    path: /path/to/path
    params: options arguments
    query: connector&key-value
    frag:

***

# http命令

## curl

    $ curl [options] [URL...]

## httpie

python开发的类似于curl的命令行工具，同时还有wget的功能．

<https://github.com/jakubroztocil/httpie>

    $ sudo yum/apt-get install httpie

    $ http -a 'username:password' GET http://google.com

***

# python的http/url标准库

python2的http标准库
1. httplib for client
2. BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, cookielib, Cookie for server

python3的标准库
1. http

python2的url标准库：
1. urlparse
2. urllib
3. urllib2

python3的url标准库：
1. urllib

## urllib

## urllib2

## urlparse

## httplib

## BaseHTTPServer

## CGIHTTPServer

## SimpleHTTPServer

## cookielib

## Cookie

***

# python的http/url的第三方库

## httplib2

<https://github.com/httplib2/httplib2>

    $pip install httplib2

## urllib3

<https://github.com/shazow/urllib3>

    $pip install urllib3

## requests

<https://github.com/kennethreitz/requests>

从http/https获取内容,内置urllib3。

    pip install requests

    import requests
    requests.reqeust(method, url, **kwargs)
    requests.Method()
    requests.Request()

    # Method Request, 返回requests.Response类型的对象。
    get(url, params=None, **kwargs)
    post(url, data=None, json=None, **kwargs)
    put(url, data=None, **kwargs)
    delete(url, **kwargs)
    patch(url, data=None, **kwargs)
    head(url, **kwargs)
    options(url, **kwargs)

    # **kwargs
    # dict
    params=None
    data=None
    headers=None
    cookies=None
    files=None
    proxies=None
    # str/json
    json=None
    # tuple
    auth=('user', 'password')
    timeout=(connect timeout, read timeout)
    cert=(cert.pem, key.pem)
    # bool
    allow_redirects=True
    verify=True
    stream=True

Response:

    # Method Response:
    r.close()
    r.iter_content(chunk_size=1, decode_unicode=False)
    r.iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
    r.json(**kwargs)
    r.raise_for_status()
    # Data:
    r.content # 返回json数据, 通过json.loads转化为dict.
    r.text # 返回unicode类型
    r.headers # 返回headers
    r.apparent_encoding
    r.is_permanent_redirect
    r.is_redirect
    r.links
    r.ok # True/False
    r.status_code # ok:200
    r.url # 返回URL
    r.history
    # other data
    r.encoding # 查看或设置编码
    r.raw
    r.cookies
    r.elapsed.seconds/microseconds/days

Sessions

    from requests.sessions import Session
    from requests import Session

auth

    from requests.auth import HTTPBasicAuth

packages

    from requests.packages import urllib3

***

# python的html/xml的标准库

## HTMLParser

HTML和XHTML解析器

python3中更名为html.parser

## htmlentitydefs

html定义通用实体

python3更名为html.entities

## xml

XML解析器

***

# python的html/xml的第三方库

## bs4

<https://www.crummy.com/software/BeautifulSoup/>

从XML和HTML文件中提取数据

使用BeautifulSoup处理后文档都是unicode格式，输出都是utf-8格式。

安装bs4:

    $sudo apt-get install Python-bs4
    $pip install beautifulsoup4

安装解析器：

* python标准库的html解析器是HTMLParser（python3中改名为html.parser)
* python标准库的xml解析器是xml.
* lxml解析html
* lxml-xml解析xml
* html5lib解析html5

使用bs4和解析器，一般用lxml：

    from bs4 import BeautifulSoup

    # BeautifulSoup
    BeautifulSoup(markup='', features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, **kwargs)
    soup = BeautifulSoup(r.content, 'lxml') # 返回BeautifulSoup类型对象, 默认html格式
    soup = BeautifulSoup(r.content, "xml") # xml格式
    soup = BeautifulSoup(r.content, "lxml-xml") # 同上
    soup = BeautifulSoup(r.content, "html5lib") # html5格式
    # BeautifulSoup 解析出的python对象有四类： Tag, NavigableString, BeautifulSoup, Comment
    prettify(self, encoding=None, formatter='minimal')
    print(soup.prettify()) # 格式化后以unicode编码输出
    get_text(self, separator=u'', strip=False, types=(<class 'bs4.element.NavigableString'>, <class 'bs4.element.CData'>))
    soup.get_text() # 获取tag中所有内容，以unicode字符串返回
    find(self, name=None, attrs={}, recursive=True, text=None, **kwargs) # 搜索当前节点和子孙节点，查找第一个,返回一个Tag对象
    find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs) # 搜索所有节点，返回Tag对象的列表
    find_parent(self, name=None, attrs={}, **kwargs) # 搜索当前节点的父辈节点
    find_parents(self, name=None, attrs={}, limit=None, **kwargs) # 搜索当前节点的父辈节点
    find_next_sibling(self, name=None, attrs={}, text=None, **kwargs) # 往后搜索当前节点兄弟节点
    find_previous_sibling(self, name=None, attrs={}, text=None, **kwargs) # 往前搜索当前节点的兄弟节点
    ...

    # Tag
    tag = soup.<tag-name> # 返回一个Tag类型对象
    tag = soup.<tag-name>.<tag-name>...
    tag.name # tag名字
    tag.attrs # tag类型有很多属性,字典类型
    tag.contents # 将tag子节点以列表方式输出
    tag.children
    tag.parent
    tag.next_sibling # 返回下一个兄弟节点
    tag.previous_sibling # 返回上一个兄弟节点
    tag.next_element # 返回下一个字符串或tag
    tag.previous_element # 返回上一个字符串或tag
    ...

    # NavigableString
    ns = tag.string # 返回一个NavigableString类型对象
    unicode(ns) # 转换成unicode
    ns.replace_with(self, replace_with) # 修改内容
    ...

    # Comment, 一个特殊的NavigableString对象,只针对有注释的Tag
    comment = soup.<tag-with-comment>.string # 返回Comment类型对象

## lxml

<https://github.com/lxml/lxml>

XML和HTML的解析器

    from lxml import etree

    etree.fromstring(text, parser=None, base_url=None) # text是一个string，返回xml的根节点lxml.etree._Element类型的迭代器
    etree.Element(_tag, attrib=None, nsmap=None, **_extra) # 创建一个Element对象, _tag指定节点，比如xml。

    xml_root = etree.Element('xml')
    html_root = etree.Element('html')
    etree.SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra) # 往父节点添加子节点，返回Element实例
    tmp_root = etree.SubElement(xml_root, _tag)

## html5lib

<https://github.com/html5lib/html5lib-python>

## xmltodict

<https://github.com/martinblech/xmltodict>

***

# Java
