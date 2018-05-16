Title: Testing Selenium
Date: 2017-02-25 09:41:39
Tags: Testing, QA, Selenium



# Selenium

<https://github.com/SeleniumHQ/selenium>

用于基于浏览器的web应用的自动化测试工具集．

    selenium1: deprecated.
    selenium2: 默认支持firefox<=46. 支持python2.6+, python3.2+
    selenium3: 支持firefox47+, 所有浏览器都需要安装webdriver.支持python2.6+, python3.3+, 必须重启OS.

支持python, java, javascript等API.

默认安装selenium3:

    $ pip install selenium

selenium3需要安装相应浏览器的driver, 然后重启OS:

selenium, driver, browser三个版本都需要兼容才能工作．

    winfows放在C:\Python\Scripts\
    linux放在/usr/local/bin/

<https://sites.google.com/a/chromium.org/chromedriver/downloads>

<https://github.com/mozilla/geckodriver/releases>

[Deprecated] Remote Control: 也就是selenium1.selenium2依然保留了selenium1的API.但是selenium3会彻底删除RC的API.

[Deprecated] IDE: selenium IDE是一个firefox的插件，用于记录浏览器上的测试步骤，能用于生成测试代码，并且转换成编程语言．但是已经被WebDriver取代．

***

# WebDriver

也就是selenium2.已经取代了selenium RC和selenium IDE.

python的API参考python博客．

***

# Grid

Selenium Grid用于分布式测试

***

# 定位元素

对应的python的API参考python博文．

selenium提供８种定位web页面中元素的方法：

* id
* name
* class
* tag
* link
* partial_link
* 通过xpath
* 通过css

在浏览器通过F12快捷键进入调试模式获取．

