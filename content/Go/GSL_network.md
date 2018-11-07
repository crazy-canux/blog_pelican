Title: GSL_network
Date: 2018-01-01 10:49:21
Tags: Go, net



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

## Addr

代表一个网络终端地址．

TCPAddr, UDPAddr, IPAddr, UnixAddr 都实现了该接口

    type Addr interface {
        Network() string
        String() string
    }

## TCPAddr

function:

    func ResolveTCPAddr(net, addr string) (*TCPAddr, error)

## UDPAddr

function:

    func ResolveUDPAddr(net, addr string) (*UDPAddr, error)

## IPAddr

function:

    func ResolveIPAddr(net, addr string) (*IPAddr, error)

## UnixAddr

function:

    func ResolveUnixAddr(net, addr string) (*UnixAddr, error)

## Conn

该接口代表通用的面向流的网络连接．

    type Conn interface {
        Read()
        Write()
        Close()
        LocalAddr()
        RemoteAddr()
        SetDeadline()
        SetReadDeadline()
        setWriteDeadline()
    }

function:

    // tcp: "tcp"、"tcp4"、"tcp6"、
    // unix: "unix", "unixpacket"
    // unix: "unixgramh"
    // udp: "udp"、"udp4"、"udp6"、
    // ip: "ip"、"ip4"、"ip6"、
    func Dail(network, address string) (Conn, error)

    func DialTimeout(network, address string, timeout time.Duration) (Conn, error)

    func Pipe() (Conn, Conn)

## PacketConn

该接口代表通用的面向数据包的网络连接．

    type PacketConn interface {
        ReadDrom()
        WriteTo()
        Close()
        LocalAddr()
        SetDeadline()
        SetReadDeadline()
        SetWriteDeadline()
    }

function:

    // ip: "ip"、"ip4"、"ip6"、
    // udp: "udp"、"udp4"、"udp6"、
    // unix: "unixgram"
    func ListenPacket(net, laddr string) (PacketConn, error)

## Listener

通用的面向流的网络协议的公用的网络监听接口．

    type Listener interface {
        Addr() addr
        Accept() (c Conn, err error)
        Close() error
    }

function:

    // tcp: "tcp"、"tcp4"、"tcp6"、
    // unix: "unix", "unixpacket"
    func Listen(net, laddr string) (Listener, error)

## IPConn

实现了Conn和PacketConn接口．

function:

    func DilIP(netProto string, laddr, raddr *IPAddr) (*IPConn, error)
    func ListenIP(netProto string, laddr *IPAddr) (*IPConn, error)

method:

## UDPConn

实现了Conn和PacketConn接口.

function:

    func DialUDP(net string, laddr, raddr *UDPAddr) (*UDPConn, error)
    func ListenDUP(net string, laddr *UDPAddr) (*UDPConn, error)

method:

## TCPConn

实现了Conn接口.

function:

    func DialTCP(net string, laddr, raddr *TCPAddr) (*TCPConn, error)

method:

## TCPListener

function:

    func ListenTCP(net string, laddr *TCPAddr) (*TCPListener, error)

method:

    func (l *TCPListener) Accept() (Conn, error)

## UnixConn

实现了Conn和PacketConn接口.

function:

    func DialUnix(net string, laddr, raddr *UnixAddr) (*UnixConn, error)
    func ListenUnixgram(net string, laddr *UnixAddr) (*UnixConn, error)

method:

## UnixListener

function:

    func ListenUnix(net string, laddr *UnixAddr) (*UnixListener, error)

method:

    func (l *UnixListener) Accept() (c Conn, err error)
    func (l *UnixListener) AcceptUnix() (*UnixConn, error)

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

定义了运行http服务端的参数．

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

## Client

代表一个http客户端.

    type Client struct {
        Transport RoundTripper
        CheckRedirect func(req *Request, via []*Request) error
        Jar CookieJar
        Timeout time.Duration
    }

## Header

代表http的头部.

    type Header map[string][]string

method:

    func (h Header) Get(key string) string
    func (h Header) Set(key, value string)
    ...

## Cookie

代表一个http回复的头部中SetCookie头的值，或http请求的头部里面的cookie值．

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

代表一个服务端接收的或客户端发送的http请求.

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

    // 解析并返回该请求r的header设置的cookie
    func (r *Request) Cookies() []*Cookie

    // 返回请求r中命名为name的cookie,如果未找到返回nil, ErrNoCookie.
    func (r *Request) Cookie(name string) (*cookie, error)

    //解析r.URL中的查询字符串，并将解析结果更新到r.Form字段.
    // post和put的body会同时更新到r.PostForm和r.Form.
    func (r *Request) ParseForm() error

    // 将请求的主体作为multipart/form-data解析.
    func (r *Request) ParseMultipartForm(maxMemory int64) error

## Response

代表一个http请求的回复r

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

    func Head(url string) (resp *Response, err error)
    func Get(url string) (resp *Response, err error)
    func Post(url string, bodyType string, boyd io.Reader) (resp *Response, err error)
    func PostForm(url string, data url.Values) (resp *Response, err error)

methods:

    func (r *Response) ProtoAtLeast(major, minor int) bool

    // 获取相应中的Set-Cookie设置的cookie
    func (r *Response) Cookies() []*Cookie

## ResponseWriter

用于构造http回复.

    type ResponseWriter interface {
        Header() Header
        WriteHeader(int)
        Write([]byte) (int, error)
    }

***

# net/mail

***

# net/smtp

***

# net/rpc

function:

    // 在DefaultServer注册并公布rcvr方法.
    func Register(rcvr interface{}) error

    // 接收连接，将每个连接交给DefaultServer服务.会阻塞.
    func Accept(lis net.Listener)

    // 在单个连接执行DefaultServer,会阻塞.
    func ServceConn(conn io.ReadWriteCloser)

    func HandleHTTP()

## Call

代表一个执行中或执行完毕的会话．

    type Call struct {
        ServiceMethod string
        Args interface{}
        Reply interface{}
        Error error
        Done chan *Call
    }

## Client

rpc客户端

    type client struct {}

function:

    func NewClient(conn io.ReadWriteCloser) *Client

    func Dial(network, address string) (*Client, error)

    func DialHTTP(network, address string) (*Client, error)

method:

    // 调用指定的方法，等待返回，将结果写入reply.
    func (client *Client) Call(serviceMethod string, args interface{}, reply interface{}) error

    func (client *Client) Go(serviceMethod string, args interface{}, reply interface{}, done chan *Call) *Call

    func (client *Client) Close() error

***

# net/textproto

***

# net/url

    scheme://[userinfo@]host/path[?query][#fragment]

## URL

    type URL struct {
        Scheme string
        Opaque string
        User *Userinfo
        Host string // host or host:port
        Path string
        RawQuery string
        Fragment string
    }

function:

    func Parse(rawurl string) (url *URL, err error)
    func ParseRequestURI(rawurl string) (url *URL, err error)

methods:

## Userinfo

## VAlues

***

