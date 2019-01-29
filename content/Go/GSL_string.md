Title: GSL_string
Date: 2018-01-01 10:49:21
Tags: Go, strings, strconv, unicode, regexp, bytes, index



# strings

实现了用于操作字符的函数.

## functions

    func EqualFold(s, t string) bool

    func HasPrefix(s, prefix string) bool
    func HasSuffix(s, suffix string) bool

    func Count(s, sep string) int

    func Contains(s, substr string) bool
    ...

    func Index(s, sep string) int
    ...

    func LastIndex(s, sep string) int
    ...

    func Title(s string) string

    func ToLower(s string) string
    ...

    // 返回count个string
    func Repeat(s string, count int) string

    func Replace(s, old, new string, n int) string

    func Map(mapping func(rune) rune, s string) string

    func Trim(s string, cutset string) string
    ...

    // 返回将字符串按照空白分割的多个字符串
    func Fields(s string) []string
    // 按照f作为分隔符来分割字符串，返回切片
    func FieldsFunc(s string, f func(rune) bool) []string

    func Split(s, sep string) []string
    ...

    // 将一系列字符串连接为一个字符串，之间用sep来分割.
    func Join(a []string, sep string) string

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

    func NewBuffer(buf []byte) *Buffer
    func NewBufferString(s string) *Buffer

methods:

    func (b *Buffer) String() string

    func (b *Buffer) Read(p []byte) (n int, err error)
    func (b *Buffer) Write(p []byte) (n int, err error)

***

# strconv

实现了基本数据类型和字符串的相互转换.

## constants

    const InitSize = intSize

## Variables

    var ErrRange = errors.New("value out of range")
    var ErrSyntax = errors.New("invalid syntax")

## functions

    // 返回一个字符是否是可打印的
    func IsPrint(r rune) bool

    // 返回字符串s是否可以不被修改的表示为一个反引号字符串
    func CanBackquote(s string) bool

    func Quote(s string) string
    ...

    func Unquote(s string) (t string, err error)
    ...

    func AppendInt(dst []byte, i int64, base int) []byte
    ...

    // 字符串转换成其他类型
    func ParseInt(s string, base int, bitSize int) (i int64, err error)
    ...

    // 其他类型转换为字符串
    func FormatInt(i int64, base int) string
    ...

    // ParseInt(s, 10, 0)的简写, string -> int
    func Atoi(s string) (i int, err error)
    // FormatInt(i, 10)的简写, int -> string
    func Itoa(i int) string

## NumError

表示一次失败的转换

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

## functions

## Regexp

Regexp代表一个编译好的正则表达式．

    type Regexp struct {}

functions:

    func Compile(expr string) (*Regexp, error)

    func CompilePOSIX(expr string) (*Regexp, error)

    func MustCompile(str string) *Regexp

    func MustCompilePOSIX(str string) *Regexp

methods:


***

# regexp/syntax

***

# index/suffixarray
