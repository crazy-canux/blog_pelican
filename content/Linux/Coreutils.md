Title: Shell Coreutils
Date: 2016-03-31 21:51:25
Tags: Linux, Shell, Coreutils, Bash, Zsh, Fish



# Linux的外部命令

Linux外部命令的项目是coreutils。

外部命令在coreutils目录中

查看外部命令所在目录：

    echo $PATH

外部命令在下列目录中：

    ~/bin # 用户自定义

    /sbin

    /bin

    /usr/sbin

    /usr/bin

    /usr/local/sbin

    /usr/local/bin

    /usr/games

    /usr/local/games

查看外部命令手册的在线手册：

    man [command]
    info [command]

自定义外部命令：

添加\$PATH变量，然后放到该目录。

***

# 系统管理

    # 查看cpu/mem/swap/system信息
    vmstat

    # 查看进程消耗的cpu/mem/swap/system等系统信息
    top
    top -H  # 查看线程
    %cpu = cputime/realtime * 100%
    cpu_usage = %cpu/cpu-number
    %mem = RES/physicalMem * 100%

    htop
    $ sudo apt-get install htop

    uname # 打印linux系统信息
    $ uname -a
    cat /etc/issue
    cat /proc/version

    uptime

    lsb_release # 查看发行版本信息
    $ lsb_release -a

    getconf # 查询系统配置的变量，LONG_BIT表示系统位数

    lscpu # 显示cpu架构的信息
    cat /proc/cpuinfo # 查看cpu信息
    cat /proc/cpuinfo | grep "processor" | wc -l # 逻辑cpu总数
    cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l # 物理cpu个数
    cat /proc/cpuinfo | grep "cpu cores" | uniq # 物理cpu核数
    cat /proc/cpuinfo | grep -e "cpu cores"  -e "siblings" | sort | uniq # 和cpu cores一样说明没有启用超线程.
    processor: 逻辑cpu总数=物理cpu个数*物理cpu核数（非超线程），  物理cpu个数*物理cpu核数*2（超线程cpu).
    physical id :物理cpu个数(每个socket/插槽可以放一个物理cpu).
    cpu cores: 物理cpu有几个核(如果是超线程技术的cpu,每个核可以运行两个线程，或者说每个核对应两个逻辑cpu）。
    siblings： 每个物理cpu单个核心上的逻辑cpu个数

    free # 显示空闲和使用的系统内存
    cat /proc/meminfo # 查看内存信息

    clear

    ps
    # 格式化输出，逗号后面不能有空格
    ps -eo/-Ao %cpu/pcpu,%mem/pmem,stat,start/start_time/lstart,pid,ppid,cmd/args/command
    ps --ppid 1 -o pid,command | grep -v grep | grep daemon # 获取多进程程序主进程的pid

    pstree -a

    pkill
    pkill -f <pattern> # 杀死args匹配的进程

    pgrep -P pid

    # 内核也有一个kill命令
    kill

    killall
    killall -e <deamon> # 杀死匹配的守护进程.

crontab:

    $ sudo apt-get install cron
    # /etc/crontab 设置了环境变量
    crontab
    crontab -l # 列出
    crontab -e # 编辑
    crontab -u <user> file # 导入配置/etc/cron.d/my-cron-file

editor:

    # 修改默认编辑器nano
    select-editor

时区管理

    timedatectl list-timezones # 查看所有时区
    sudo timedatectl set-timezone Asia/Shanghai # 设置时区
    ls -l /etc/localtime # 应该是一个链接

# Linux管理

    lsmod 查看已加载的模块    # /proc/modules
    modprobe -c 查看已编译可加载的内核模块
    modprobe <name> 加载模块 # /etc/modules
    modprobe -r <name> 删除模块
    rmmod <name> 删除模块

# 用户和权限管理

    id
    id -u 打印当前用户uid(root uid=0)

chmod:

    # 当文件的owner的x位置为s,表示设置了SUID, 仅对二进制可执行文件有效.
    # 如果执行者对该文件有可执行权限，那么执行者在执行该文件期间，就拥有了该文件的owner的权限.
    -rwsr-xr-x file
    chmod u+s <file> # 加SUID
    chmod 4777 <file>

    -rwxr-sr-x file/dir
    chmod g+s <file>/<dir> # 加SGID
    chmod 2777 <dir>

    drwxrwxrwt dir
    chmod o+t <dir> # 加SBIT
    chmod 1777 <dir>

    chown
    chgrp
    chattr

useradd:

    useradd
    useradd -r -m -G sudo -s /bin/bash <user>

    userdel

    usermod

    users # 查看当前登陆的用户

    groupadd
    groupdel
    groupmod

    groups # 查看指定用户所属的组，默认当前用户的组

    gpasswd

    chpasswd
    echo "username:password" | chpasswd # 修改username的密码

    passwd

# 文件和目录管理

    mkdir
    tree
    cat
    col
    colrm
    comm
    csplit
    ed
    ex
    fmt
    fold
    join
    look
    mtype
    pico
    sort
    tr
    expr
    uniq
    wc

    cksum
    cmp
    diff
    diffstat
    file
    cut
    less
    more
    locate
    lsattr
    mattrib
    mdel
    mdir
    mktemp
    mmove
    mren
    mtools
    mtoolstest
    mv
    od
    paste
    patch
    rcp
    rm
    split

    touch
    umask
    which
    cp
    whereis
    mcopy
    mshowfat
    lprm
    lpr
    lpq
    rev
    toilet
    aafire
    xeyes
    pv
    yes
    cal
    factor

tee

    main > 2>&1 log1.log | tee log2.log # 同时重定向到两个文件
    main 2>&1 | tee ${LOG} # 同时将stdout和stderr输出到终端和日志文件.
    $ echo "content" | sudo tee filename # 写入到root权限的文件

lsof查看打开的文件资源:

    lsof #
    lsof -i # 查看
    sudo lsof -i :port # 查看端口是否被使用

readlink:

    readlink 获取符号连接信息
    sudo readlink /proc/1/exe

ln:

    ln TARGET LINK_NAME # 创建文件的硬链接,目录不能创建硬链接
    -s, --symbolic
    ln -s TARGET LINK_NAME # 创建文件或目录的软链接

dirname:

    dirname
    dirname $0   # 获取当前文件所在目录的相对路径, 也就是.
    $(cd $(dirname $0) && pwd)    # 获取当前文件所在目录的绝对路径

rsync:

    rsync
    rsync [OPTION]... SRC [SRC]... DEST
    rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
    rsync [OPTION]... [USER@]HOST:SRC [DEST]
    rsync -rtvzuOPH --delete
    -e "ssh -o StrictHostKeyChecking=no"
    -v verbose
    -a archive == -rlptgoD
    -u --update # 跳过目的地址上modification time更新的文件
    --inplace
    --append
    --append-verify
    -r --recursive
    -z --compress
    --progress
    --partial
    -P == --partial --progress
    --devices
    --specials
    -D == --devices --specials
    -H --hard-links  preserve hard-link
    -l --links  copy symlinks as symlinks 保留软链接
    -L          copy symlinks to dest 复制原始文件
    --delete  从dest删除src没有的文件
    -h --human-readable
    -g --group  preserve group
    -o --owner  preserve owner
    -p --perms  preserve permissions
    -t --times  preserve modification times
    -O, --omit-dir-times    忽略目录的modification times.
    --exclude 排除文件

计算文件空间使用:

    du
    $ du -sh

四个用到正则表达式的重要命令：

    sed
    awk
    grep/ack/ag
    find

# 压缩备份

tar(.tar)

    tar
    -c, --create   # 创建归档
    -u, --update    # 更新归档文件
    -x, --extract, --get    # 提取归档

    compression options:
    -j, --bzip2
    -J, --xz
    -z, --gzip, --gunzip, --ungzip
    -Z, --compress, --uncompress

    device selection and switching:
    -f, --file=ARCHIVE

    informative output:
    -v, --verbose

gzip(.gz)

    gzip
    gunzip
    tar zxvf file.tar.gz
    tar zcvf file.tar.gz dir

bzip2(.bz2)

    bzip2
    bunzip2
    tar jxvf file.tar.bz2
    tar jcvf file.tar.bz2 dir

compress(.z)

    compress
    uncompress
    tar Zxvf file.tar.z

xz(.xz)

    xz
    unxz
    tar Jxvf file.tar.xz

zip(.zip)

    zip
    unzip

7z(.7z)

    $ sudo apt-get install p7zip
    p7zip

