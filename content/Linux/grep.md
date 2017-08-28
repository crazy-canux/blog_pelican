Title: Shell grep
Date: 2016-04-20 13:55:36
Tags: Shell, grep, ack, ack2, ag



# grep

grep相关的命令：

    grep
    egrep == grep -E
    fgrep == grep -F
    rgrep == grep -r

grep:

    grep [OPTIONS] PATTERN [FILE/DIR...]
    grep [OPTIONS] [-e PATTERN | -f FILE] [FILE/DIR...]

options:

    # Matcher Selection
    -G, --basic-regexp grep默认只支持BRE, 只能使用基本的RE
    -E, --extended-regexp 选择ERE, 可以使用扩展的RE
    # grep -E "pattern1|pattern2" 比如支持或运算
    -F, --fixed-strings
    -P, --perl-regexp perl RE

    # Matching Control
    -e PATTERN, --regexp=PATTERN    可以指定多个pattern
    # grep -e pattern1 -e pattern2 filename 相当于或运算，满足一个就被过滤出来
    -f FILE, --file=FILE    文件的每一行就是一个pattern.
    -i, --ignore-case    忽略大小写
    -v, --invert-match   忽略含有pattern的行
    -w, --word-regexp    精确匹配一个单词
    -x, --line-regexp    精确匹配一行
    -y

    # General Output Control
    -c, --count    统计匹配到的行数
    --color[=WHEN], --colour[=WHEN]    输出匹配的pattern高亮
    -L, --files-without-match    列出没有匹配到的文件名
    -l, --files-with-matches    列出匹配到的文件的文件名
    # grep -rl pattern1 | xargs grep -r pattern2    相当于与运算，过滤同时满足两个pattern
    -m NUM, --max-count=NUM
    -o, --only-matching    只输出匹配的部分
    # grep -o pattern filename | wc -l 统计匹配的行数
    -q, --quiet, --silent    不打印查找的结果
    -s, --no-messages

    # Output Line Prefix Control
    -b, --byte-offset    打印匹配的字符数或偏移量
    -H, --with-filename
    -h, --no-filename
    --label=LABEL
    -n, --line-number    打印匹配的行的行号
    -T, --initial-tab
    -u, --unix-byte-offsets
    -Z, --null

    # Context Line Control
    -A NUM, --after-context=NUM    打印匹配到的行的后NUM行
    -B NUM, --before-context=NUM    打印匹配到的行的前NUM行j
    -C NUM, -NUM, --context=NUM    打印匹配到的行的前NUM行和后NUM行

    # File and Directory Selection
    -a, --text
    --binary-files=TYPE
    -D ACTION, --devices=ACTION
    -d ACTION, --directories=ACTION
    --exclude=GLOB    排除查找指定的文件
    --exclude-from=FILE
    --exclude-dir=DIR   排除查找指定的目录
    -I
    --include=GLOB     指定查找的文件
    -r, --recursive    递归查找
    -R, --dereference-recursive    递归查找
    # grep -nR/-nr pattern filename    阅读源码可以递归查找并打印行号

    # Other Options
    --line-buffered
    --mmap
    -U, --binary
    -z, --null-data

# ack

ack/ack2是grep的升级版

ack:

<https://github.com/beyondgrep/ack>

ack2(ack-grep):

<https://github.com/beyondgrep/ack2>

# ag

ack/ack2的升级版

<https://github.com/ggreer/the_silver_searcher>

安装：

    $sudo apt-get install silversearcher-ag
    $sudo yum install the_silver_searcher

使用：

    $man ag
