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

http api(restful)一般使用json格式的数据．

python和json数据类型对应关系参考WEB/JSON.

complex和class/def不能被编码.

    import json

classes:

functions:

    # 将转换后的json格式写入文件
    dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
    with open(file, 'w') as f:
        json.dump(dict_data, f)

    # 将dict类型转换成json格式
    dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
    json_data = json.dumps(dict_data)

    indent=4 # 写入自动缩进４个空格

    # 将读出的文件(json格式)转换成dict
    load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    with open(file, 'r') as f:
        dict_data = json.load(f)

    # json类型变成dict类型
    loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    response_dict = json.loads(response.content) # 使用requests获取的json数据,转化为dict类型

***
