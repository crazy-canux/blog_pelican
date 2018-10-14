Title: HTTP
Date: 2016-09-13 01:39:34
Tags: Network, http, https, url, html, xml



# HTTP/HTTPS

http port: 80

https port: 443

http/https的请求方式：

    get # 从服务器取出资源
    post # 在服务器新建资源
    put # 在服务器更新资源，客户端提供改变后的完整资源
    delete # 从服务器删除资源
    patch # 在服务器更新资源，客户端提供改变的属性
    head # 获取资源的源数据
    options # 获取资源的哪些信息是客户端可以改变的信息

URL: Uniform Resource Locator

URI: Universal Resource Identifier

    <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    scheme: http/https/ftp/file
    netloc: username:password@host:port
    path: /path/to/path
    params: options arguments
    query: connector&key-value
    fragment:

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

# python的http标准库

python2的http标准库

1. httplib for client
2. BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, cookielib, Cookie for server

python3的标准库

1. http

# python的url标准库

python2的url标准库：

1. urlparse
2. urllib
3. urllib2

python3的url标准库：

1. urllib

***
