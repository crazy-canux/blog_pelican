Title: GSL_network
Date: 2018-01-01 10:49:21
Tags: Go, GSL, net



# net

网络IO接口，包括TCP/IP, UDP, SOCKET, DNS

    import "net"

## constants

    const (
        IPv4len = 4
        IPv6len = 16
    )

## variables


## functions

***

# net/http

http协议客户端和服务器的实现

    import "net/http"

## constants

    const (
        MethodGet = "GET"
        MethodHead = "HEAD"
        MethodPost = "POST"
        MethodPut = "PUT"
        MethodPatch = "PATCH"
        MethodDelete = "DELETE"
        MethodConnect = "CONNECT"
        MethodOptions = "OPTIONS"
        MethodTrace = "TRACE"
    )

## variables


## functions

    // 在w的header中添加Set-Cookie头．
    func SetCookie(w ResponseWriter, cookie *Cookie)

    func Handle(pattern string, handler Handler)

    func HandlerFunc(pattern string, handler func(ResponseWriter, *Request))

    func ListenAndServe(addr string, handler Handler) error


## Header

## Cookie

    type Cookie struct {
        Name string
        Value string
        Path string
        Domain string
        Expires time.Time
        RawExpires string
        MaxAge int
        Secure bool
        HttpOnly bool
        Raw string
        Unparsed []string
    }

method:

    // 返回cookie序列化的结果
    func (c *Cookie) String() string

## Request

    type Request struct {
        Method string
        URL *url.URL
        Proto string // "HTTP/1.0"
        ProtoMajor int // 1
        ProtoMinor int // 0
        Header Header
        Body io.ReadCloser
        ContentLength int64
        TransferEncoding []string
        Close bool
        Host string
        Form url.Values
        PostForm url.Values
        MultipartForm *multipart.Form
        Trailer Header
        RemoteAddr string
        RequestURI string
        TSL *tls.ConnectionState
    }

function:

    func NewRequest(method, urlStr string, body io.Reader) (*Request, error)

    func ReadRequest(b *bufio.Reader) (req *Request, err error)

method:

    // 解析并返回该请求的header设置的cookie
    func (r *Request) Cookies() []*Cookie

    // 返回请求中命名为name的cookie,如果未找到返回nil, ErrNoCookie.
    func (r *Request) Cookie(name string) (*cookie, error)

## Response

    type Response struct {
        Status string
        StatusCode int
        Proto string
        ProtoMajor int
        ProtoMinor int
        Header Header
        Body io.ReadCloser
        ContentLength int64
        TransferEncoding []string
        Close bool
        Trailer Header
        Request *Request
        TLS *tls.ConnectionState
    }

functions:

    func ReadResponse(r *bufio.Reader, req *Request) (*Response, error)

methods:

    func (r *Response) ProtoAtLeast(major, minor int) bool

    // 获取相应中的Set-Cookie设置的cookie
    func (r *Response) Cookies() []*Cookie

## Transport

## Client

***

# net/mail

***

# net/smtp

***

# net/rpc

***

# net/textproto

***

# net/url

***

