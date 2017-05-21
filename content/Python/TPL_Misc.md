Title: TPL_Misc
Date: 2017-03-27 21:18:33
Tags: Misc



# colorama

Simple cross-platform colored terminal text in Python

<https://github.com/tartley/colorama>

Install:

    $ pip install colorama

    from colorama import Fore, Back, Style, init
    init()
    print Fore.RED + 'show red' + Fore.RESET # 字体颜色
    print Back.CYAN + 'show cyan in background' + Back.RESET # 背景颜色

# decorator

decorator

<https://github.com/micheles/decorator>

    $ pip install decorator

# enum

<https://pypi.python.org/pypi/enum/0.4.6>

    from enum import Enum
    class Dataset(str, Enum):
        FIRST: 'one'
        SECOND: 'second'

    Dataset.FIRST.name # 'FIRST'
    Dataset.FIRST.value # 'one'
