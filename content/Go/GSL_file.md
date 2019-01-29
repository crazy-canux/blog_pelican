Title: GSL_file
Date: 2018-01-01 10:49:21
Tags: Go, path, encoding, text, html, gob, csv, json, xml, yaml



# path

## function

    func IsAbs(path string) bool
    func Join(elem ...string) string
    func Split(path string) (dir, file string)
    func Join(elem ...string) string
    func Dir(path string) string
    func Base(path string) string
    func Ext(path string) string
    ...

***

# path/filepath

## Constants

    const (
        Separator = os.PathSeparator
        ListSeparator = os.PathListSeparator
    )

## Variable

    var ErrBadPattern = errors.New("Syntax error in pattern")

    var SkipDir = errors.New("skip this diractory")

## function

    func IsAbs(path string) bool
    func Abs(path string) (string, error)

    // 返回 targpath 相对于 basepath 的 路径 （相当于返回 targpath - basepath)
    func Rel(basepath, targpath string) (string, error)

    func Split(path string) (dir, file string)
    func Join(elem ...string) string
    func Dir(path string) string
    func Base(path string) string
    func Ext(path string) string)
    func Walk(root string, walkFn WalkFunc) error

## WalkFunc

调用Walk时会对每个目录和文件调用该函数.

如果该函数返回错误，Walk函数会中止.

如果该函数返回SkipDir, Walk会掉过处理该目录，继续处理其它内容.

    type WalkFunc func(path string, info os.FileInfo, err error) error

***

# encoding

定义了供其它包使用的在字节和文本之间转换数据的接口.

    import "encoding"

***

# encoding/json

go和json数据类型对应关系，参考WEB/JSON.

在线获取json的go数据结构:

<https://github.com/mholt/json-to-go>

<https://mholt.github.io/json-to-go>

chan/complex/func类型不能编码为json.

    import "encoding/json"

## constants

## variables

## functions

    # 返回v的json编码(将go的对象转换为json对象), 可以打tag.
    > "-" 该字段不会输出到json
    > udName 用户自定义名字会出现在json
    > omitempty 如果该字段为空就不会出现在json
    > Type 如果指定类型，会转换成指定的类型出现在json
    json.Marshal(v interface{}) ([]byte, error)

    # 具有缩进功能
    json.MarshalIndent(v interface{}, prefix, indent string) ([]byte, error)

    # 将json对象data转换成go对象，存入v
    # 只有可导出字段才会在json中找到.
    > Bool                   对应JSON布尔类型
    > float64                对应JSON数字类型
    > string                 对应JSON字符串类型
    > []interface{}          对应JSON数组
    > map[string]interface{} 对应JSON对象
    > nil                    对应JSON的null
    json.Unmarshal(data []byte, v interface{}) error

    // 将json格式的src中的无用的空白字符剔除后写入dst.
    func Compact(dst *bytes.Buffer, src []byte) error

    // 格式化json，以便json编码能安全的嵌入html的<script>标签
    func HTMLEscape(dst *bytes.Buffer, src []byte)

    //
    func Indent(dst *bytes.Buffer, src []byte, prefix, indent string) error

## Marshaler

interface:

    type Marshaler interface {
        MarshalJSON() ([]byte, error)
    }

## Unmarshaler

interface:

    type Unmarshaler interface {
        UnmarshalJSON([] byte) error
    }

## Decoder

从输入流解码json对象

struct:

    type Decoder struct {}

function:

    func NewDecoder(r io.Reader) *Decoder

method:

    // 从dec读取下一个对象存入v.
    func (dec *Decoder) Decode(v interface{}) error

## Encoder

***

# encoding/csv

***

# encoding/gob

go binary, go的数据持久化包，用于编码器和解码器之间交换二进制数据.

## functions

    func Register(value interface{})

    func RegisterName(name string, value interface{})

## GobDecoder

## GobEncoder

## Decoder

管理从远端读取数据的类型和信息的解码操作.

struct:

    type Decoder struct {}

functions:

    // 返回一个从r读取数据的Decoder
    func NewDecoder(r io.Reader) *Decoder

methods:

    # 从dec读取下一个值并存入e
    func (dec *Decoder) Decode(e interface{}) error

    func (dec *Decoder) DecodeValue(v reflect.Value) error

## Encoder

管理数据类型和信息编码后发送到远端的操作.

struct:

    type Encoder struct {}

functions:

    // 返回一个将编码后数据写入w的Encoder
    func NewEncoder(w io.Writer) *Encoder

methods:

    // 将e编码后发送到enc
    func (enc *Encoder) Encode(e interface{}) error

    func (enc *Encoder) EncodeValue(value reflect.Value) error

## CommonType

    type CommonType struct {
        Name string
        Id typeId
    }

***

# text/template

***

# text/template/parse

***

# text/scanner

***

# text/tabwriter

***

# html

提供了用于转义和解转义html文本的函数．

    import "net"

## functions

    // 将　<, >, &, ', " 转义为字符实体 &lt, &gt, &#39,
     func EscapeString(s string) string

     func UnescapeString(s string) string

***

# html/template

实现了数据驱动模板，用于生成可对抗代码注入的安全html输出．

## functions

    // 将b转义后写入w．
    func HTMLEscape(w io.Writer, b []byte)

    // 转义s之后,返回结果字符串.
    func HTMLEscapeString(s string) string

    // 转义多个字符串，返回结果字符串.
    func HTMLEscaper(args ...interface{}) string

## FuncMap

定义函数名字符串到函数的映射，每个函数必须要1到2个返回值．

    type FuncMap map[string]interface{}

## Template

    type Template struct {
        Tree *parse.Tree
    }

function:

    // 创建名为name的模板
    func New(name string) *Template

    // 在err非nil时panic, 检测模板是否正确．
    // 通过template.New().Parse() 返回值作为参数.
    func Must(t *Template, err error) *Template

    // 创建一个模板，并解析filenames作为模板内容
    // 第一个文件名为模板名字(不包括扩展名)
    func ParseFiles(filenames ...string) (*Template, error)

    // 创建一个模板，并解析匹配pattern的文件．
    // 匹配的第一个文件名为模板名字(不包括扩展名)
    func ParseGlob(pattern string) (*Template, error)

methods:

    // 将字符串str解析为模板
    func (t *Template) Parse(str string) (*Template, error)

    // 将文件解析为模板
    func (t *Template) ParseFiles(filenames ...string) (*Template, error)

    //
    func (t *Template) ParseGlob(pattern string) (*Template, error)

    // 将解析好的模板应用到data上，并将输出写入wr.
    func (t *Template) Execute(wr io.Writer, data interface{}) (err error)

    // 使用和t关联的名为name的模板
    func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error

    // 注册函数到模板t, funcMap的key是模板中调用的函数名，value是实际的函数
    func (t *Template) Funcs(funcMap FuncMap) *Template

***

# yaml

<https://github.com/go-yaml/yaml>

***

# toml

<https://github.com/toml-lang/toml>

<https://github.com/BurntSushi/toml>
