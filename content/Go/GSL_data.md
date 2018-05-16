Title: GSL_data
Date: 2018-01-01 10:49:21
Tags: Go, GSL, time, container, archive, compress



# time

## constants

const:

    const (
        ANSIC       = "Mon Jan _2 15:04:05 2006"
        UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
        RFC3339     = "2006-01-02T15:04:05Z07:00"
        ...
    )

## functions

    // 阻塞go程d代表的时间段
    func Sleep(d Duration)

    func After(d Duration) <- chan Time

    func Tick(d Duration) <- chan Time

## Time

代表一个纳秒精度的时间点.

零值是January 1, year 1, 00:00:00.000000000 UTC.

struct:

    type  Time struct {}

functions:

    // 格式化一个时间, eg:　2009-11-10 15:00:00 -0800 PST
    func Date(year int, month Month, day, hour, min, sec, nsec int, loc *Location) Time

    // 返回当前本地时间, eg: 2018-03-18 12:16:55.842029 +0800 CST m=+0.001962301
    func Now() Time

    func Parse(layout, value s tring) (Time, error)

    func ParseInLocation(layout, value string, loc *Location) (Time, error)

    func Unix(sec int64, nsec int64) Time

methods:

    // 返回T的地点和时区信息
    func (t Time) Location() *Location

    // 返回t的时区规范名和相对于UTC的偏移量
    func (t Time) Zone() (name string, offset int)

    func (t Time) IsZero() bool

    func (t Time) Local() Time

    func (t Time) UTC() Time

    func (t Time) In(loc *Location) Time

    func (t Time) Unix() int64

    func (t Time) UnixNano() int64

    // 比较两个时间
    func (t Time) Equal(u Time) bool

    // t > u 返回true
    func (t Time) Before(u Time) bool

    // t < u 返回true
    func (t Time) After(u Time) bool

    // 返回t的年月日.
    func (t Time) Date() (year int, month Month, day int)

    // 返回t对应的时分秒
    func (t Time) Clock() (hour, min, sec int)

    // 返回t对应的年
    func (t Time) Year() int

    // 返回t对应的月
    func (t Time) Month() Month

    func (t Time) ISOWeek() (year, week int)

    // 返回t对应的当年的第几天
    func (t Time) YearDay() int

    // 返回t对应的当月的第几天
    func (t Time) Day() int

    // 返回t对应的星期几
    func (t Time) Weekday() Weekday

    // 返回t对应的第几小时
    func (t Time) Hour() int

    // 返回t对应的分钟
    func (t Time) Minute() int

    // 返回t对应的秒
    func (t Time) Second() int

    // 返回t对应的纳秒偏移量
    func (t Time) Nanosecond() int

    func (t Time) Add(d Duration) Time

    func (t Time) AddDate(years int, months int, days int) Time

    func (t Time) Sub(u Time) Duration

    func (t Time) Round(d duration) Time

    func (t Time) Truncate(d Duration) Time

    func (t Time) Format(layout string) string

    func (t Time) String(layout string) string

## Weekday

    type Weekday int

    const (
        Sunday Weekday = iota
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday
    )

methods:

    // 返回d对应的英文名
    func (d Weekday) String() string

## Month

    type Month int

    const (
        January Month = 1 + iota
        February
        March
        April
        May
        June
        July
        August
        September
        October
        November
        December
    )

methods:

    // 返回m对应的英文名
    func (m Month) String() string

## Location

struct:

    type Location struct {}

functions:

    // 返回使用给定名字创建的Location
    // name == "" 或　name == "UTC", 返回UTC
    // name == "Local", fanhui1Local
    // 其它时间数据库的值
    func LoadLocation(name string) (*Location, error)

    // 使用给定的名称和偏移量创建一个Location
    func FixedZone(name string, offset int) *Location

methods:

    // 返回对时区信息的描述
    func (l *Location) String() string

## Duration

## Timer

## Ticker

***

# container/heap

***

# container/list

***

# container/ring


***

# compress/bzip2

***

# compress/flate

***

# compress/gzip

***

# compress/lzw

***

# compress/zlib

***

# archive

***
