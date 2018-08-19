Title: GSL_network_data
Date: 2018-01-01 10:49:21
Tags: Go, GSL, html



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

## Template

    type Template struct {
        Tree *parse.Tree
    }

function:

    // 创建名为name的模板
    func New(name string) *Template

    func Must(t *Template, err error) *Template

methods:

    func (t *Template) Parse(src string) (*Template, error)

    func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error


