Title: GSL_file
Date: 2018-01-01 10:49:21
Tags: Go, path, encoding, text, html, gob, csv, json, xml, yaml



# path

***

# path/filepath

***

# encoding

定义了供其它包使用的在字节和文本之间转换数据的接口.

    import "encoding"

***

# encoding/json

go和json数据类型对应关系，参考WEB/JSON.

chan/complex/func类型不能编码为json.

    import "encoding/json"

## constants

## variables

## functions

    # 返回v的json编码(将go的对象转换为json对象), 可以打tag.
    json.Marshal(v interface{}) ([]byte, error)

    # 具有缩进功能
    json.MarshalIndent(v interface{}, prefix, indent string) ([]byte, error)

    # 将json对象data转换成go对象，存入v
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

    //
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
