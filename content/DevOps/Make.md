Title: Make
Date: 2017-01-12 21:18:33
Tags: Make, Makefile



# Make

make的作用：
* 控制源代码的编译
* 手册页的编写
* 将应用程序安装到目标目录

make的使用规则：
* 如果工程没有编译过，需要编译所有源文件和链接所有目标文件．
* 如果工程里某几个目标文件被修改，只需要编译修改的源文件，并链接所有目标文件．
* 如果头文件被修改，只需要编译引用了被修改的头文件的源文件，并链接所有目标文件．

makefile文件查找顺序：
* 当前目录找makefile
* 当前目录找Makefile
* 当前目录找GNUmakefile

# make命令

make命令会执行当前目录的makefile/Makefile/GNUmakefile文件．

    make [options] [target] ...
    -f FILE, --file=FILE, --makefile=FILE    # 指定makefile文件
    -n, --just-print, --dry-run, --recon # 只打印，不执行
    -k, --keep-going　# 忽略错误继续执行

    make
    make all
    make install
    make clean

make的工作顺序：
* 读入所有makefile文件
* 读入include的其它makefile文件
* 初始化变量
* 推导隐晦规则，分析所有规则
* 为所有目标文件创建依赖关系链
* 根据依赖关系决定哪些目标需要重新生成
* 执行生成的命令

# makefile语法

make命令执行makefile文件时，会比较target和prerequisites的时间戳，如果后者比前者新，或者前者不存在，就会执行command,否则会跳过command.

其中#表示注释，\表示续行．@表示该命令的执行不会打印到stdout,-表示忽略错误继续执行．

makefile中的command必须以tab开头，target和prerequisites有多个时用空格分开．

    # comment
    target...: prerequisites...
        command
        command1 too \
        long
        @command2
        -command3
        ...

makefile变量赋值:

    var=val
    var := val  覆盖之前的值
    var ?= val  如果没有被赋值过，就赋值
    var += val  添加一个值

通过命令定义变量：

    var := $(shell <command>)
    为了区分makefile变量和shell命令里面的变量，用$$var表示shell变量
    var := $(shell cat file | awk '/.*/{print $$0}')

makefile的变量：

    定义变量：
    obj=a.o b.o c.o
    使用变量：
    $(obj)

自动化变量：

    $<    # 第一个依赖文件
    $^    # 所有的依赖文件
    $@    # 目标文件
    $*    # 不包含扩展名的目标文件名称
    $+    # 所有的依赖文件，用空格分开
    $?    # 所有时间戳比目标文件晚的依赖文件，以空格分开
    $%    # 如果目标是归档成员，则表示目标的归档成员

清空目标文件：

    clean:
        -rm elf $(obj)
    # 或者用.PHONY表示clean是一个伪目标
    .PHONY: clean
    clean:
        -rm elf $(obj)

在makefile中引用外部makefile:

    # 优先在当前目录查找，-l可以指定额外的查找路径
    -include a.makefile b.makefile ...

makefile支持的通配符：

    ~    # 用来表示$HOME环境变量
    *    # 用来表示任意长度字符串
    [...]

自动推导和隐晦规则：

伪目标：

查找路径：
