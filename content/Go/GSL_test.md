Title: GSL_test
Date: 2018-01-01 10:49:21
Tags: Go, testing



# testing

go的测试由go test命令和testing包组成．

测试程序命名：

    XXX_test.go

测试程序结构：

    import "testing"

    func TestXXX(t *testing.T) {}
    func BenchmarkXXX(b *testing.B) {}

go test会运行所有这种命名的函数，t.Error或t.Fail表示该函数测试失败．

## constants

## variables

## functions

## T

管理测试状态并支持格式化测试的日志．

struct:

    type T struct {}

methods:

    // 将当前测试标识为失败，但继续执行该文件剩下的测试
    func (c *T) Fail()

    // 将当前测试标识为失败，并停止执行该测试, 继续执行下一个测试文件.
    func (c *T) FailNow()

    // 用于报告测试函数是否失败
    func (c *T) Failed() bool

    func (c *T) Fatal(args ...interface{})
    func (c *T) Fatalf(format string, args ...interface{})

    func (c *T) Error(args ...interface{})
    func (c *T) Errorf(format string, args ...interface{})

    func (c *T) Log(args ...interface{})
    func (c *T) Logf(format string, args ...interface{})

    func (c *T) Skip(args ...interface{})
    func (c *T) SkipNow()
    func (c *T) Skipf(format string, args ...interface{})
    func (c *T) Skipped() bool

## B

管理基准测试的计时行为，并指示应该迭代的运行测试多少次.

struct:

    type B struct {
        N int
    }

methods:

    func (c *B) Fail()
    func (c *B) FailNow()
    func (c *B) Failed() bool

    func (c *B) Error(args ...interface{})
    func (c *B) Errorf(format string, args ...interface{})

    func (c *B) Fatal(args ...interface{})
    func (c *B) Fatalf(format string, args ...interface{})

    func (c *B) Log(args ...interface{})
    func (c *B) Logf(format string, args ...interface{})

    func (c *B) Skip(args ...interface{})
    func (c *B) SkipNow()
    func (c *B) Skipf(format string, args ...interface{})
    func (c *B) Skipped() bool

***

# testing/iotest

***

# testing/quick
