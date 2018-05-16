Title: GSL_file
Date: 2018-01-01 10:49:21
Tags: Go, GSL, path, encoding, text, html



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

    # 返回v的json编码(将go的对象转换为json对象)
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

# text

***

# html
