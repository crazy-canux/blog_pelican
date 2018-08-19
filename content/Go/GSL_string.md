Title: GSL_string
Date: 2018-01-01 10:49:21
Tags: Go, GSL, strings, strconv, unicode, regexp, bytes, index



# string

实现了用于操作字符的函数.

## functions

    // 返回将字符串按照空白分割的多个字符串
    func Fields(s string) []string

    // 按照f作为分隔符来分割字符串，返回切片
    func FieldsFunc(s string, f func(rune) bool) []string

## Reader

## Replacer

***

# bytes

实现了操作[]bytes的常用函数.

## constants

## variables

## functions

## Reader

## Buffer

Buffer是一个实现了读写方法的可变大小的字节缓冲.

零值是一个空的可用于读写的缓冲.

struct:

    type Buffer struct {}

functions:

methods:

***

# strconv

实现了基本数据类型和字符串的相互转换.

## constants

    const InitSize = intSize

## Variables

    var ErrRange = errors.New("value out of range")
    var ErrSyntax = errors.New("invalid syntax")

## functions

    func ParseInt(s string, base int, bitSize int) (i int64, err error)

    // ParseInt(s, 10, 0)的简写, string -> int
    func Atoi(s string) (i int, err error)

    func FormatInt(i int64, base int) string

    // FormatInt(i, 10)的简写, int -> string
    func Itoa(i int) string

## NumError

struct:

    type NumError struct {
        Func string
        Num string
        Err error
    }

methods:

    func (e *NumError) Error() string

***

# unicode

***

# regexp

实现了正则表达式搜索



***

# regexp/syntax

***

# index/suffixarray
