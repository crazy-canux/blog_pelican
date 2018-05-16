Title: GSL_sytem
Date: 2018-01-01 10:49:21
Tags: Go, GSL, os, syscall, log, flag, bufio, io, fmt



# os

提供了操作系统的不依赖平台的接口

    import "os"

## constants

    const (
        O_RDONLY int = syscall.O_RDONLY
        O_WRONLY int = syscall.O_WRONLY
        O_RDWR int = syscall.O_RDWR
        O_CREATE int = syscall.O_CREATE
        O_TRUNC int = syscall.O_TRUNC
        ...
    )

    const (
        SEEK_SET int = 0
        SEEK_CUR int = 1
        SEEK_END int = 2
    )

    const (
        // 操作系统指定的路径分隔符
        PathSeperator = '/'
        // 操作系统指定的表分隔符
        PathListSeparator = ':'
    )

    // 操作系统空设备的名字
    const DevNull = "/dev/null"

## variables

    var (
        ErrInvalid = errors.New("invalid argument")
        ...
    )

    // 指向标准输入／输出／错误的文件描述符
    var (
        Stdin = NewFile(uintptr(syscall.Stdin), "/dev/stdin")
        Stdout = NewFile(uintptr(syscall.Stdout), "/dev/stdout")
        Stderr = NewFile(uintptr(syscall.Stderr), "/dev/stderr")
    )

    // 保存了命令行参数，第一个是程序名
    var Args []string

## functions

    // 返回内核提供的主机名
    func Hostname() (name string, err error)

    // 当前程序以给出的状态码退出，defer不会执行
    func Exit(code int)

    // 返回key=value格式的环境变量的字符串的切片拷贝
    func Environ() []string

## Signal

interface:

    type Signal interface {
        String() string
        Signal()
    }

variable:

    var (
        Interrupt Signal = syscall.SIGINT
        Kill Signal = syscall.SIGKILL
    )

## FileMode

代表文件模式和权限位．

    type FileMode uint32

constant:

    const (
        ModeDir    FileMode = 1 << (32 - 1 - iota) // d: 目录
        ...
        ModeType = ModeDir | ModeSymlink | ModeNamePipe | ModeSocket | ModeDevice
        ModePerm FileMode = 0777
    )

methods:

    func (m FileMode) IsDir() bool

## FileInfo

## File

表示一个打开的文件对象

struct:

    type File struct {}

functions:

    // 采用flag=os.O_RDWR和perm=0666模式创建一个名为name的文件, 返回读写文件句柄
    // 文件已存在就截断
    func Create(name string) (file *File, err error)

    // 打开指定文件，返回只读文件句柄, flag=os.O_RDONLY
    func Open(name string) (file *File, err error)

    // 指定flag和perm创建／打开文件
    func OpenFile(name string, flag int, perm FileMode) (file *File, err error)

    // 使用给定的文件描述服和名称创建一个文件.
    func NewFile(fd uintptr, name string) *File

    // 返回一对关联的文件对象
    func Pipe() (r *File, w *File, err error)

methods:

    // 从文件f中最多读取len(b)字节数据写入b, 返回读取的字节数
    // 返回0, io.EOF, 表示读取0个字节,文件终止．
    func (f *File) Read(b []byte) (n int, err error)

    // 向文件f写入len(b)字节数据b，返回写入字节数
    func (f *File) Write(b []byte) (n int, err error)

    func (f *File) WriteString(s string) (ret int, err error)

    func (f *File) Close() error

## Process

保存一个被StarProcess创建的进程的信息

struct:

    type Process struct {
        Pid int
    }

functions:

    // 启动一个新进程
    func StartProcess(name string, argv []string, attr *ProcAttr) (*Process, error)

    // 查找一个运行中的进程
    func FindProcess(pid int) (p *Process, err error)

methods:

    // 向进程发送信号
    func (p *Process) Signal(sig Signal) error

    // 阻塞直到进程退出
    func (p *Process) Wait() (*ProcessState, error)

    // 让进程立刻退出
    func (p *Process) Kill() error

    // 释放进程绑定的资源
    func (p *Process) Release() error

## ProcessState

保管Wait函数报告的某个已退出进程的信息．

struct:

    type ProcessState struct {}

methods:

    // 返回一个已退出的进程的id
    func (p *ProcessState) Pid() int

    // 报告进程是否已退出
    func (p *ProcessState) Exited() bool

    // 报告进程是否成功退出
    func (p *ProcessState) Success() bool

    // 返回已退出进程及其子进程耗费的系统cpu时间
    func (p *ProcessState) SystemTime() time.Duration

    // 返回已退出进程及其子进程耗费的用户cpu时间
    func (p *ProcessState) UserTime() time.Duration

    func (p *ProcessState) Sys() interface{}

    func (p *ProcessState) SysUsage() interface{}

    func (p *ProcessState) String() string

## ProcAttr

保存被StratProcess启动的新进程的属性

struct:

    type ProcAttr struct {
        Dir string
        Env []string
        Files []*File
        Sys *syscall.SysProcAttr
    }

***

# os/exec

执行外部命令，包装了os.StartProcess函数，提供更高级的接口.

## variable

    var ErrNotFound = errors.New("executable file not found in $PATH")

## functions

    // 在环境变量指定的目录中搜索可执行文件file
    func LookPath(file string) (string, error)

## Cmd

表示一个准备执行或执行中的外部命令

struct:

    type Cmd struct {
        Path string
        Args []string
        Env []string
        Dir string
        stdin io.Reader
        Stdout io.Writer
        Stderr io.Writer
        ExtraFiles []*os.File
        SysProcAttr *syscall.SysProcAttr
        Process *os.Process
        ProcessState *os.ProcessState
    }

functions:

    // 返回*Cmd
    func Command(name string, arg ***string) *Cmd

methods:

    // 同步：执行命令，并阻塞直到完成
    func (c *Cmd) Run() error

    // 异步：开始执行命令，不阻塞直接返回，
    func (c *Cmd) Start() error
    // 阻塞通过Start执行的命令直到完成，设置状态码并释放资源．
    func (c *Cmd) Wait() error

    func (c *Cmd) StdinPipe() (io.WriteCloser, error)
    func (c *Cmd) StdoutPipe() (io.ReadCloser, error)
    func (c *Cmd) StderrPipe() (io.ReadCloser, error)

    // 执行命令并返回stdout的切片
    func (c *Cmd) Output() ([]byte, error)
    // 执行命令并返回stdout和stderr合并后的切片
    func (c *Cmd) CombinedOutput() ([]byte, error)

***

# os/signal

***

# os/user

***

# syscall

提供了操作系统级别的调用．

    import "syscall"

## constants

    const (
        AF_ALG    = 0x26
        ...
    )

    // 定义异常
    const (
        E2BIG    = Errno(0x70)
        ...
    )

    // 定义信号
    const (
        SIGABRT    = Signal(0x6)
        ...
    )

    const (
        SYS_READ    = 0
        ...
    )

    const (
        SizeofSockaddrInet4    = 0x10
        ...
    )

    const (
        IFA_UNSPEC    = 0x0
        ...
    )

    const (
        SizeofSockFilter    = 0x8
        ...
    )

    const (
        VINTR    = 0x0
        ...
    )

    const ImplementsGetwd = true

    const PathMax = 0x1000

    const SizeofInotifyEvent = 0x10

## variables

    var (
        Stdin = 0
        Stdout = 1
        Stderr = 2
    )

    var ForkLock sync.RWMutex

    var SocketDisableIPv6 bool

## others

参考文档

***

# io

提供了对IO原语的基本接口

    import "io"

## variables

    // 放无法获取更多输入时Read方法返回os.EOF
    var EOF = errors.New("EOF")

## functions

    func TeeReader(r Reader, w Writer) Reader

    func MultiReader(readers ...Reader) Reader

    func MultiWriter(writers ...Writer) Writer

    // 将src数据拷贝到dst, 直到EOF或出错，返回拷贝的字节数
    func Copy(dst Writer, src Reader) (written int64, err error)

    // 类似Copy，不过只拷贝n个字节.
    func CopyN(dst Writer, src Reader, n int64) (written int64, err error)

    func ReadAtLeast(r Reader, buf []byte, min int) (n int, err error)

    func ReadFull(r Reader, buf []byte) (n int, err error)

    func WriteString(w Writer, s string) (n int, err error)

## Reader

用于包装基本的读取方法

os.File 和 bufio.Reader都是io.Reader接口

interface:

    type Reader interface {
        Read(p []byte) (n int, err error)
    }

## Writer

用于包装基本的写入方法

os.File 和 bufio.Writer都是io.Writer接口

interface:

    type Writer interface {
        Write(p []byte) (n int, err error)
    }

## Closer

用于包装基本的关闭方法

interface:

    type Closer interface {
        Close() error
    }

## Seeker

用于包装基本的移位方法

interface:

    type Seeker interface {
        Seek(offset int64, whence int) (int64, error)
    }

***

# io/ioutil

实现一些增强的IO接口功能

## variables

    // 一个io.Writer接口，对它所有Write调用都会无实际操作成功返回.
    var Discard io.Writer = devNull(0)

## functions

    func NopCloser(r io.Reader) io.ReadCloser

    func ReadAll(r io.Reader) ([]byte, error)

    // 从filename指定的文件读取数据并返回, 成功返回文件内容和nil
    func ReadFile(filename string) ([]byte, error)

    // 向filename指定文件写入数据，如果文件存在先清空文件，如果不存在创建文件.
    func WriteFile(filename string, data []byte, perm os.FileMode) error

    func ReadDir(dirname string) ([]os.FileInfo, error)

    func TempDir(dir, prefix string) (name string, err error)

    func TempFile(dir, prefix string) (f *os.File, err error)

***

# bufio

bufio实现了有缓冲的IO

## constants

    const (
        // 用于缓冲一个token
        MaxScanTokenSize = 64 * 1024
    )

## variables

    // 会被Scanner返回的错误
    var (
        ErrInvalidUnreadByte = errors.New("bufio: invalid use of UnreadByte")
        ...
    )

## functions

    func ScanBytes(data []byte, atEOF bool) (advance int, token []byte, err error)

    func ScanRunes(data []byte, atEOF bool) (advance int, token []byte, err error)

    func ScanWords(data []byte, atEOF bool) (advance int, token []byte, err error)

    // 将每一行文本去掉末尾的换行标记，然后作为一个token返回
    func ScanLines (data []byte, atEOF bool) (advance int, token []byte, err error)

## Reader

给io.Reader接口对象附加缓冲

struct:

    type Reader struct {}

functions:

    func NewReader(rd io.Reader) *Reader

    func NewReaderSize(rd io.Reader, size int) *Reader

methods:

    func (b *Reader) Read(p []byte) (n int, err error)
    // 读取直到第一次遇到delim字节，返回一个包含已读取数据和delim字节的字符串
    // 当且仅当返回的切片不以delim结尾时，返回非nil错误
    func (b *Reader) ReadString(delim byte) (line string, err error)
    func (b *Reader) ReadBytes(delim byte) (line []byte, err error)
    func (b *Reader) ReadSlice(delim byte) (line []byte, err error)
    func (b *Reader) ReadLine() (line []byte, isPrefix bool, err error)

    func (b *Reader) ReadByte() (c byte, err error)
    func (b *Reader) ReadRune() (r rune, size int, err error)

## Writer

给io.Writer接口对象提供缓冲

struct:

    type Writer struct {}

functions:

    func NewWriter(w io.Writer) *Writer

    func NewWriterSize(w io.Writer, size int) *Writer

methods:

    func (b *Writer) Write(p []byte) (nn int, err error)
    func (b *Writer) WriteString(s string) (int, error)
    func (b *Writer) WriteByte(c byte) error
    func (b *Writer) WriteRune(r rune) (size int, err error)

    func (b *Writer) Flush() error

## ReadWriter

struct:

    type ReadWriter struct {
        *Reader
        *Writer
    }

functions:

    func NewReadWriter(r *Reader, w *Writer) *ReadWriter

## Scanner

提供了方便的读取数据接口

struct:

    type Scanner struct {}

functions:

    // 创建并返回一个从r读取数据的Scanner，默认分割函数是ScanLines
    func NewScanner(r io.Reader) *Scanner

methods:

    // 设置s的分割函数
    func (s *Scanner) Split(split SplitFunc)

    // 获取当前位置的token, 并让Scanner的扫描位置移动到下一个token.
    func (s *Scanner) Scan() bool

    // 返回最近一次Scan调用生成的token.
    func (s *Scanner) Bytes() []byte

    // 创建一个字符串保存Bytes返回的token,并返回
    func (s *Scanner) Text() string

    // 返回Scanner遇到的第一个非EOF错误
    func (s *Scanner) Err() error

## SplitFunc

    type SplitFunc func(data []byte, atEOF bool) (advance int, token []byte, err error)

***

# fmt

实现了类似于C的printf/scanf的格式化IO.

    import "fmt"

通用占位符:

    %v    相应值的默认格式
    %+v   同时打印结构体的字段名
    %#v   相应值的go语法表示
    %T    相应值的类型的go语法表示
    %%    字面上的百分号

布尔类型：

    %t    true/false

整数类型：

    %b    二进制表示
    %c    相应的unicode码点所表示的字符
    %d    十进制表示
    %o    八进制表示
    %q    单引号包围的字符字面值
    %x    十六进制(字母小写)
    %X    十六进制(字母大写)
    %U    unicode格式

浮点数类型：

    %b    无小数部分的，指数为二的幂的科学计数法．
    %e    科学计数法
    %E    科学计数法
    %f    有小数点，而无指数
    %g    根据情况选择%e 或 %f
    %G    根据情况选择E% 或 %f

    %[宽度]Type
    %.[精度]Type
    %[宽度].[精度]Type

字符串与字节切片：

    %s    字符串或切片的字节
    %q    双引号包围的字符串
    %x    十六进制(小写字母)
    %X    十六进制(大写字母)

指针：

    %p    十六进制表示(0x)

## functions

    // 返回一个包含该格式化字符串的错误
    func Errorf(format string, a ...interface{}) error

    // 写入到STDOUT, 返回写入字节数
    // 默认格式化
    func Print(a ...interface{}) (n int, err error)
    // 默认格式化，自动结尾添加换行符
    func Println(a ...interface{}) (n int, err error)
    // 指定格式化
    func Printf(format string, a ...interface{}) (n int, err error)

    // 写入到w, 返回写入字节数
    // w: os.File bufio.Writer
    func Fprint(w io.Writer, a ...interface{}) (n int, err error)
    func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
    func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)

    // 返回该字符串
    func Sprint(a ...interface{}) string
    func Sprintln(a ...interface{}) string
    func Sprintf(format string, a ...interface{}) string

    // 从STDIN扫描文本存入a,返回成功扫描的个数
    // 换行视为空白，获取len(a)个条目才停止扫描
    func Scan(a ...interface{}) (n int, err error)
    // 换行才停止扫描
    func Scanln(a ...interface{}) (n int, err error)
    // 根据空格分割的条目格式化写入指定参数a
    func Scanf(format string, a ...interface{}) (n int, err error)

    // 从r扫描文本存入a, 返回成功扫描的条目
    // r: os.File bufio.Reader
    func Fscan(r io.Reader, a ...interface{}) (n int, err error)
    func Fscanln(r io.Reader, a ...interface{}) (n int, err error)
    func Fscanf(r io.Reader, format string, a ...interface{}) (n int, err error)

    // 从字符串str扫描文本存入a,  返回扫描成功的条目
    func Sscan(str string, a ...interface{}) (n int, err error)
    func Sscanln(str string, a ...interface{}) (n int, err error)
    func Sscanf(str string, format string, a ...interface{}) (n int, err error)

## Stringer

interface:

    type Stringer initerface {
        String() string
    }

## GoStringer

interface:

    type GoStringer interface {
        GoString() string
    }

## State

interface:

    type State interface {
        Write(b []byte) (ret int, err error)
        Width() (wid int, ok bool)
        Precision() (prec int, ok bool)
        Flag(c int) bool
    }

## Formatter

interface:

    type Formatter interface {
        Format(f State, c rune)
    }

## ScanState

interface:

    type ScanState interface {
        ReadRune() (r rune, size int, err error)
        UnreadRune() error
        SkipSpace()
        Token(skipSpace bool, f func(rune) bool) (token []byte, err error)
        Width() (wid int, ok bool)
        Read(buf []byte) (n int, err error)
    }

## Scanner

interface:

    type Scanner interface {
        Scan(state ScanState, verb rune) error
    }

***

# unsafe

***

# log

实现了简单的日志服务.

## Constants

    const (
        Ldate        = 1 << iota     // 日期
        Ltime              // 时间
        Lmicroseconds      // 微秒
        Llongfile          // 绝对文件名和行好 /path/to/file.go:13
        Lshortfile         // 文件名和行好, 覆盖上面字段 file.go:13
        LstdFlags    = Ldate | Ltime      // 标准logger的初始值
    )

## functions


## Logger

struct:

    type Logger struct {}

function:

    // 创建一个Logger.
    func New(out io.Writer, prefix string, flag int) *Logger

methods:

    func (l *Logger) Flags() int

***

# flag

实现了命令行参数解析

## variables

    var CommandLine = NewFlagSet(os.Args[0], ExitOnError)

    //
    var ErrHelp = errors.New("flag: help requested")

    //
    var Usage = func() {
        fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
        PrintDefaults()
    }

## functions

    // 返回已被设置的flag数量
    func NFlag() int

    // 返回已注册flag的结构体指针
    func Lookup(name string) *Flag

    // 返回解析flag之后参数个数
    func NArg() int
    // 返回解析之后非flag参数个数
    func Args() []string
    // 返回解析之后的第i个参数, i=0 就是第一个参数，而不是程序名称
    func Arg(i int) string

    // 向Stderr写入所有注册好的flag的默认值
    func PrintDefaults()

    // 从os.Args[1:] 中解析注册的flag.
    func Parse()
    // 返回是否Parse是否被调用过
    func Parsed() bool

    // 按照字典顺序遍历flag，并对每个flag调用fn, 只针对解析时设置了的flag
    func Visit(fn func(*Flag))
    // 按照字典顺序遍历flag,　并对每个flag调用fn, 针对所有flag.
    func VisitAll(fn func(*Flag))

    // 用指定的名称，默认值，帮助信息注册一个bool类型的flag
    // 返回一个保存了该flag的值的指针
    func Bool(name string, value bool, usage string) *bool
    // 用指定的名称，默认值，帮助信息注册一个bool类型的flag
    // 将flag值保存到指针p指向的变量
    func BoolVar(p *bool, name string, value bool, usage string)

    func Int
    func IntVar
    func Int64
    func Int64Var

    func Uint
    func UintVar
    func Uint64
    func Uint64Var

    func Float64
    func Float64Var

    func String
    func StringVar

    // time.Duration类型
    func Duration
    func DurationVar

    // 用指定的名字，帮助信息，注册一个flag，类型由value决定
    func Var(value Value, name string, usage string)
    // 设置已注册的flag的值
    func Set(name, value string) error

## ErrorHandling

定义如何处理flag解析错误

    type ErrorHandling int

    const (
        ContinueOnError ErrorHandling = iota
        ExitOnError
        PanicOnError
    )

## Flag

定义一个flag

struct:

    type Flag struct {
        Name     string
        Usage    string
        Value    Value
        DefValue string
    }

## FlagSet

代表一个已注册flag集合.

FlagSet零值没有名字，默认采用ContinueOnError.

struct:

    type FlagSet struct {
        Usage func()
    }

functions:

    // 创建一个新的FlagSet叫name，采用errorHandling为错误处理策略
    func NewFlagSet(name string, errorHandling ErrorHandling) *FlagSet

methods:

    // 设置f的名字和错误处理策略.
    func (f *FlagSet) Init(name string, errorHandling ErrorHandling)

## Value

用于将动态值保存在flag里.

interface:

    type Value interface {
        String() string
        Set(string) error
    }

## Getter

***
