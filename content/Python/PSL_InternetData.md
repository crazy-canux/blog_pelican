Title: PSL_InternetData
Date: 2016-08-14 21:22:40
Tags: Python, Internet



# Internet Data Handling

## email

## mailcap

## mailbox

## mimetypes

## base64

    import base64

## binhex

## binascii

## quopri

## uu

## json

rest api一般使用json格式的数据．

json格式数据，类似于字典形式的字符串类型。

    import json
    json_data = json.dumps(dict_data) # dict类型变成json类型

    dict_data = json.loads(json_data) # json类型变成dict类型
    response_dict = json.loads(response.content) # 使用requests获取的json数据,转化为dict类型

***

# TPL

相关的第三方库

