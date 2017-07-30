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

classes:

functions:

    # dict类型变成json类型
    dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
    dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
    json_data = json.dumps(dict_data)

    # json类型变成dict类型
    load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    response_dict = json.loads(response.content) # 使用requests获取的json数据,转化为dict类型

***

# TPL

相关的第三方库

