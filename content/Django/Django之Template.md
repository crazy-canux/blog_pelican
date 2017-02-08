---
layout: post
title: Django之Template
comments: true
date: 2016-10-04 04:12:49
updated:
tags:
- python
- django
categories:
- Python
- Django
permalink:
---

# 模板设置

模板引擎在settings.py设置, django有两套模板引擎：

    TEMPLATES = [
        # DjangoTemplates
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 定义项目的通用模板, mysite/templates
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            # True 表示在所有安装应用的application/templates中查找。
            'APP_DIRS': True,
            # 模板的选项：
            'OPTIONS': {
            'context_processors':
            'debug':
            'loaders':
            'string_if_invalid':
            'file_charset': 'utf-8'
            },
        },

        # Jinja2
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            # 定义项目的通用模板, mysite/templates
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            # True表示在所有已安装应用的application/jinja2中查找。
            'APP_DIRS': True,
            # 模板的选项：
            'OPTIONS': {
            'autoescape': True
            'loader':
            'auto_reload':
            'undefined':
            },
        },
    ]

BACKEND定义模板引擎,django内置的模板引擎有两个django.template.backends.django.DjangoTemplates(默认)和django.template.backends.jinja2.Jinja2

DIRS存放自定义的不在应用路径的模板，模板引擎按列表顺序搜索查找模板源文件,默认就是默认引擎的默认路径。

APP_DIRS告诉模板引擎是否进入安装应用的templates(jinja2的目录是jinja2)查找模板。

在视图中使用模板：

默认django会在项目的所有应用的templates中查找模板，所以为了防止多个应用有同名的模板，需要在templates下新建application同名的目录来存放模板

应用的模板文件需要在应用目录创建templates文件夹

默认模板放在polls/templates/polls/XXX.html

应用的静态文件需要在应用目录创建static文件夹

默认静态文件存放在polls/static/polls/XXX.css

静态文件夹用来集中存放和管理图片，js脚本和css样式表等静态文件。

django.template.loader定义了两个函数加载模板。

    get_template(template_name, dirs=<object object>, using=None)
    select_template(template_name_list, dirs=<object object>, using=None)

# 模板语言

django模板语言由四部分组成：
* 变量
* 标签
* 过滤器
* 评论

## 变量

    {{ var }}

显示字符串：

    string = "test string"
    return render(request, 'index.html', {'string': string})

    {{ string }}

显示字典：

    dict = {"key1": "value1", "key2": "value2"}
    return render(request, 'index.html', {'dict': dict})

    {{ dict.name1 }}

## 标签

    {% tag %}

参考内置标签：

<http://python.usyiyi.cn/translate/django_182/ref/templates/builtins.html#ref-templates-builtins-tags>

for标签：

遍历列表：

    list = ['val1', 'val2', 'val3']
    return render(request, 'index.html', {'list': 'list'})

    ```html
    {% for i in list %}
    {{ i }}
    {% endfor %}
    ```

遍历字典：

    ```html
    {% for key, value in dict.items %}
    {{ key }}: {{ value }}
    {% endfor %}
    ```

empty列表可能为空：

    ```html
    {% for i in list %}
    ...
    {% empty %}
    ...
    {% endfor %}
    ```

reversed反向循环：

    {% for i in list reversed %}

for循环有用的变量：

    forloop.counter    # 1 - indexed
    forloop.counter0    # 0 - indexed
    forloop.revcounter    # 1 - indexed
    forloop.revcounter0    # 0 - indexed
    forloop.first
    forloop.last
    forloop.parentloop

if标签：

    ```html
    {% if expression %}
    ...
    {% else %}
    ...
    {% endif %}
    ```

if可用的布尔操作符：

    {% if expression1 and expression2 %}
    {% if not expression %}
    {% if expression1 or expression2 %}
    {% if not expression1 or expression2 %} # not优先级高于or
    {% if expression1 and not expression2 %} # not优先级高于and
    {% if expression1 and expression2 or expression3 %} # and优先级高于or
    {% if var == value %}
    {% if var != value %}
    {% if var < value %}
    {% if var > value %}
    {% if var <= value %}
    {% if var >= value %}
    {% if var in value %}
    {% if a > b and b > c %}
    {% if var|filter"arguments expression %} # if中使用过滤器

布尔操作符的优先级：

    or
    and
    not
    in
    ==, !=, <, >, <=, >=

include标签：

加载模板并以标签内的参数渲染。

    {% include 'XXX.html' %}

load标签：

加载自定义模板标签集。

    {% load foo bar from somelibrary %}

now标签：

显示最近的日期和事件。

spaceless标签：

删除html标签之间的空白格，包括制表符和换行。

url标签：

返回一个绝对路径的引用，该引用匹配一个给定的视图函数和一些可选的参数。

    {% 'some-url-name' v1 v2 %}

### 模板继承

block标签：

在底层模板定义一些通用的内容，block标签可以被子模板覆盖。

    ```html
    {% block XXX %}
    This is default content
    {% endblock %}}
    ```

extends标签：

表示当前模板继承自父模板。

extends标签必须放在子模板第一行。

extends用来调用底层的模板，然后修改block标签内容。

    ```html
    {% extends "XXX.html"/variable %}
    {% block XXX %}
    This is rewrite content
    {% endblock %}
    ```

block.super:

如果需要获取父模板的block中的内容，可以用block.super。

可以在父模板的block中增加内容，而不是完全覆盖。

## 过滤器

    {{ var|filter:arguments }}

参考内置过滤器

<http://python.usyiyi.cn/translate/django_182/ref/templates/builtins.html#ref-templates-builtins-filters>

add过滤器：

把add后的参数加给value。

    {{ value|add:"2" }} # value -> value+2
    {{ value|addslashes }} # "I'm string" -> "I\'m string"

addslashed过滤器：

在引号前面加\

    {{ value|addslashes }} # I'm canux -> I\'m canux

capfirst过滤器：

变量的第一个字母大写。

    {{ value|capfirst }}

center过滤器：

使value在给定的宽度范围内居中。

    {{ value|center:"15" }}

cut过滤器：

移除value中所有的与给出的变量相同的字符串。

    {{ value|cut:"cut" }} # 移除value中的字符串"cut"

date过滤器：

根据给定格式对一个date变量格式化。

default过滤器：

给value设定默认值，如果value没有赋值，就用默认值。

    {{ value|default:"default-value" }}

default_if_none过滤器：

仅当value是None使用默认值。

    {{ value:default_if_none:"nothing" }}

dictsort过滤器：

dictsortreversed过滤器：

divisibleby过滤器：

如果value可以被给出的参数整除，返回True。

    {{ value|divisibleby:"3" }}

escape过滤器：

escapejs过滤器：

filesizeformat过滤器：

格式化为人类可读的文件大小。

first过滤器：

返回迭代器的第一个元素。

floatformat过滤器：

force_escape过滤器：

get_digit过滤器：

iriencode过滤器：

join过滤器：

last过滤器：

length过滤器：

length_is过滤器：

linebreaks过滤器：

linebreaksbr过滤器：

linenumbers过滤器：

ljust过滤器：

lower过滤器：

把字符串转换成小写。

make_list过滤器：

phone2numeric过滤器：

pluralize过滤器：

pprint过滤器：

random过滤器：

romevetags过滤器：

rjust过滤器：

slice过滤器：

slugify过滤器：

stringformat过滤器：

striptags过滤器：

time过滤器：

timesince过滤器：

timeuntil过滤器：

title过滤器：

truncatechars过滤器：

truncatechars_html过滤器：

truncatewords过滤器：

truncatewords_html过滤器;

unordered_list过滤器：

upper过滤器：

将字符串转换成大写形式。

urlencode过滤器：

urlize过滤器：

urlizetrunc过滤器：

wordcount过滤器：

wordwrap过滤器：

yesno过滤器：

i18n过滤器：

l10n过滤器：

tz过滤器：

## 注释

单行注释：

    ```html
    {# this is single line comment #}
    ```

多行注释：

    ```html
    {% comment %}
    line1
    line2
    {% endcomment %}
    ```

# 自动html转义

当从模板生成html时，值可能包含影响html最终呈现的字符。

django的自动转义,默认是打开的：

    < 转义成 &lt;
    > 转义成 &gt;
    ' 转义成 &#39
    " 转义成 &quot;
    $ 转义成 &amp;

如果不需要自动转义可以关闭它

可以用safe过滤器关闭独立变量中的自动转义：

    data = <b>
    {{ data }} -> &lt;b&gt;
    {{ data|safe }} -> <b>

可以用autoescape标签关闭模板代码中的自动转义：

autoescape标签有off和on两个参数，表示关闭和打开自动转义。

父模板中的autoescape可以被子模板继承，也可以被include标签包含的模板继承。

    ```html
    {% autoescape off %}
    {{ name }}
    {% endautoescape %}
    ```

