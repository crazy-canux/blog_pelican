Title: GSL_database
Date: 2018-01-01 10:49:21
Tags: Go, GSL, database



# database/sql

使用该包，必须提供一个数据库驱动

<https://github.com/golang/go/wiki/SQLDrivers>

mssql driver:

<https://github.com/denisenkom/go-mssqldb>

mysql driver:

<https://github.com/go-sql-driver/mysql>

postgresql driver:

<https://github.com/lib/pq>

<https://github.com/jackc/pgx>

## variables

    // QueryRow 没有返回row时，调用返回值的Scan方法会返回该变量
    var ErrNoRows = errors.New("sql: no rows in result set")

## functions

    // 注册并命名一个数据库，在Open中使用该命名启用该驱动
    // 如果注册同一名称两次或者driver参数为nil, 会导致panic.
    Register(name string, driver driver.Driver)

## DB

DB是一个数据库句柄，代表一个具有零到多个底层连接的连接池．

可以安全的被多个go程同时使用．

struct:

    type DB struct {}

functions:

    // 验证数据库驱动和参数
    // driverName: mssql, mysql, postgres
    // mssql dataSourceName: "server=%s;port=%d;database=%s;user id=%s;password=%s"
    // mysql dataSourceName: "user:password@tcp(server:port)/database"
    Open(driverName, dataSourceName string) (*DB, error)

methods:

    // 返回数据库下层驱动
    func (db *DB) Driver() driver.Driver

    // 检查连接是否有效
    func (db *DB) Ping() error

    // 关闭数据库，释放资源
    func (db *DB) Close() error

    // 设置与数据库建立连接的最大数目
    func (db *DB) SetMaxOpenConns(n int)

    // 设置连接池中的最大闲置连接数
    func (db *DB) SetMaxIdleConns(n int)

    // 执行命令但是不返回执行结果,一般用于(insert/update/delete)
    func (db *DB) Exec(query string, args ...interface{}) (Result, error)

    // 执行命令返回多行结果（一般用于select)
    func (db *DB) Query(query string, args ...interface{}) (*Rows, error)

    // 执行命令最多返回一行结果
    func (db *DB) QueryRow(query string, args ...interface{}) *Row

    // 创建一个准备好的状态用于之后的命令
    func (db *DB) Prepare(query string) (*Stmt, error)

    // 开始一个事务
    func (db *DB) Begin() (*Tx, error)

## Stmt

stmt是准备好的状态，可以安全的被多个go程同时使用．

struct:

    type Stmt struct {}

methods:

    func (s *Stmt) Exec(args ...interface{}) (Result, error)

    func (s *Stmt) Query(args ...interface{}) (*Rows, error)

    func (s *Stmt) QueryRow(args ...interface{}) *Row

    func (s *Stmt) Close() error

## Tx

Tx表示一个进行中的数据库事务．

一次事务必须以对Commit或Rollback的调用结束．

事务结束后，所有的操作都会失败并返回ErrTxDone.

struct:

    type Tx struct {}

methods:

    func (tx *Tx) Exec(query string, args ...interface{}) (Result, error)

    func (tx *Tx) Query(query string, args ...interface{}) (*Rows, error)

    func (tx *Tx) QueryRow(query string, args ...interface{}) *Row

    func (tx *Tx) Prepare(query string) (*Stmt, error)

    // 使用已存在的状态生成一个特定的状态．
    func (tx *Tx) Stmt(stmt *Stmt) *Stmt

    // 提交事务
    func (tx *Tx) Commit() error

    // 回滚事务
    func (tx *Tx) Rollback() error

## Scanner

interface:

    type Scanner interface {
        Scan(src interface{}) error
    }

## Result

Exec方法返回Result.

    type Result interface {
        LastInsertId() (int64, error)
        RowsAffected() (int64, error)
    }

## Row

QueryRow方法返回Row, 表示单行查询结果．

struct:

    type Row struct {}

methods:

    // 将该行查询结果各列分别保存进dest参数指定的值中．
    // 如果匹配多行，只取第一行，如果没有匹配行，返回ErrNoRows.
    func (r *Row) Scan(dest ...interface{}) error

## Rows

Query方法返回Rows, 表示查询的结果集，它的游标指向第０行，使用Next方法遍历该结果集．

struct:

    type Rows struct {}

methods:

    // 返回列名
    func (rs *Rows) Columns() ([]string, error)

    // 将当前行的各列结果填充进dest
    func (rs *Rows) Scan(dest ...interface{}) error

    // 准备用于Scan的下一行结果，每次调用Scan都要先调用Next
    func (rs *Rows) Next() bool

    func (rs *Rows) Close() error

    func (rs *Rows) Err() error

***

# database/sql/driver
