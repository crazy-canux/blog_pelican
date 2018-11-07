Title: XSS
Date: 2018-07-28 16:08:54
Tags: Security, XSS



# XSS

XSS: Cross Site Scripting, 跨站脚本攻击

XSS攻击涉及到攻击者，客户端，和web应用三者.

XSS原理:

* Web应用未对用户提交请求的数据做充分的检查过滤,允许用户在提交的数据中掺入HTML代码(最主要的是“>”、“<”),并将未经转义的恶意代码输出到第三方用户的浏览器解释执行,是导致XSS漏洞的产生原因。

XSS目前主要手段和目的:

* 盗用cookie,获取敏感信息
* 利用植入flash，通过crossdomain权限设置获取更高权限．
* 利用iframe, frame, XMLHttpRequests等方式以用户身份执行一些管理操作．

XSS预防:

* 过滤特殊字符
* 使用http头指定类型
