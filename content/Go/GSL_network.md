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

    // 注册一个handler和对应的pattern 到DefaultServeMux.
    func HandlerFunc(pattern string, handler func(ResponseWriter, *Request))

    // 为监听器收到的每个连接创建一个新的goroutine．
    // goroutine 会读取请求并调用handler回复该请求．
    func Serve(l net.Listener, handler Handler) error

    // 监听tcp地址addr, 使用handler参数调用Serve函数处理连接．
    // handler = nil 相当于DefaultServeMux
    func ListenAndServe(addr string, handler Handler) error

## File

    type File interface {
        io.Closer
        io.Reader
        Readdir(count int) ([]os.FileInfo, error)
        Seek(offset int64, whence int) (int64, error)
        Stat() (os.FileInfo, error)
    }

## FileSystem

    type FileSystem interface {
        Open(name string) (File, error)
    }

## Dir

    type Dir string

method:

    func (d Dir) Open(name string) (File, error)

## Handler

实现Handler接口的对象可以被注册为http的服务函数

    type Handler interface {
        ServeHTTP(ResponseWriter, *Request)
    }

function:

    // 对每个请求回复"404 page not found"
    func NotFoundHandler() Handler

    // 对每个请求使用状态码code重定向到url.
    func RedirectHandler(url string, code int) Handler

    func TimeoutHandler(h Handler, dt time.Duration, msg string) Handler

    // 将请求的URL.Path中的前缀prefix去除后再给h.
    func StripPrefix(prefix string, h Handler) Handler

    func FileServer(root FileSystem) Handler

## HandlerFunc

将普通函数转换成http的服务函数

    type HandlerFunc func(ResponseWriter, *Request)

method:

    // ServeHTTP会调用f(w, r)
    func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)

## ServeMux

ServeMux是http请求的多路转接器．

    type ServeMux struct {}

function:

    // 创建并返回一个新的*ServeMux
    func NewServeMux() *ServeMux

method:

    //
    func (mux *ServeMux) Handle(pattern string, handler Handler)

    func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request))

    func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)

    func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)

## Server

    type Server struct {
        Addr string
        Handler Handler
        ReadTimeout time.Duration
        WriteTimeout time.Duration
        MaxHeaderBytes int
        TLSConfig *tls.Config
        TLSNextProto map[string]func(*Server, *tls.Conn, Handler)
        ConnState func(net.Conn, ConnState)
        ErrorLog *log.Logger
    }

method:

    func (s *Server) SetKeepAlivesEnabled(v bool)

    func (s *Server) Serve(l net.Listener) error

    func (s *Server) ListenAndServe() error

    func (s *Server) ListenAndServeTLS(certFile, keyFile string) error

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

