Title: Beego Template
Date: 2018-09-27 01:33:42
Tags: Beego, Template



# Golang 模板

beego的模板和text/template, html/template差不多．

## 注释

    {{/* comment /*}}

## 变量

变量定义和使用

    申明变量不会产生输出．
    {{$Var := pipeline}}

    使用
    {{$Var}}

## actions

range和with会修改dot的值:

    {{.}}  当pipeline不为空，赋值给dot

if标签：

    {{if pipeline}} T {{end}}
    {{if pipeline}} T0 {{else}} T1 {{end}}
    {{if pipeline}} T0 {{else if pipeline}} T1 {{end}}

range标签：

只能用于array/slice/map/channel

    {{range pipeline}} T0 {{end}}
    {{range pipeline}} T0 {{else}} T1 {{end}}

with标签:

    {{with pipeline}} T0 {{end}}
    {{with pipeline}} T0 {{else}} T1 {{end}}

define标签：

定义模板

    {{define "name"}}
    ...
    {{end}}

template标签:

调用模板

    {{template "name"}}
    {{template "name" pipeline}}

## function

函数调用:

    {{"output" | function}}
    {{function "output"}}

预定义的全局函数:

    and
    or
    not
    len
    index
    print
    printf
    println
    html
    urlquery
    js
    call
