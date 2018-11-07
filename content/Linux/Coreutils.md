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

    free # 显示空闲和使用的系统内存
    cat /proc/meminfo # 查看内存信息

    clear

    ps
    # 格式化输出，逗号后面不能有空格
    ps -eo/-Ao %cpu/pcpu,%mem/pmem,start/start_time/lstart,pid,ppid,cmd/args/command

    pstree -a

    pkill
    pkill -ef <pattern> # 杀死args匹配的进程

    pgrep -P pid

    # 内核也有一个kill命令
    kill

    killall

    # /etc/crontab 设置了环境变量
    crontab
    crontab -l
    crontab -e

    # 修改默认编辑器nano
    select-editor

时区管理

    timedatectl list-timezones # 查看所有时区
    sudo timedatectl set-timezone Asia/Shanghai # 设置时区
    ls -l /etc/localtime # 应该是一个链接

# 用户和权限管理

    id
    id -u 打印当前用户uid(root uid=0)

    chmod
    chown
    chgrp
    chattr

    useradd
    userdel
    usermod
    users # 查看当前登陆的用户

    groupadd
    groupdel
    groupmod
    groups # 查看指定用户所属的组，默认当前用户的组

    gpasswd
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

    tee
    $command > 2>& 1 log1.log | tee log2.log # 同时重定向到两个文件
    $ echo "content" | sudo tee filename # 写入到root权限的文件

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

# 磁盘管理(设备管理)

sysstat:

    # <https://github.com/sysstat/sysstat>
    $ sudo apt-get install sysstat
    # 包括 iostat/mpstat/pidstat/tapestat/cifsiostat

iostat:

    # 查看diskio信息
    $ sudo iostat

iotop

    # 查看进程的diskio
    $ sudo apt-get install iotop
    $ sudo iotop

df计算文件系统磁盘空间使用:

    df
    $ df -h

mount/umount挂载文件系统:

    mount
    mount -t type -o option device dir
    mount -t ext4 /dev/sdb1 /var/www
    mount -t tmpfs -o size=100G tmpfs /var/www

    umount
    umount device/dir

dd转化并拷贝文件:

    dd

fsck检查并修复文件系统:

    fsck

mkfs:

    mkfs [options] [-t type fs-options] device [size]
    mkfs.ext4 /dev/sdb1

fdisk管理磁盘分区表:

    fdisk
    fdisk -l

    fdisk /dev/sda # 可以创建新的磁盘分区
    > n ...    创建新的分区
    > t (8e表示linux LVM), 修改分区类型
    > w 保存修改
    partprobe /dev/sda # 在不重启的情况下保存分区

磁盘管理:

    # 先创建linux lvm分区
    pvcreate <pv-name> # 创建物理卷PV
    pvdisplay
    vgextend <vg-name> <pv-name>  # 给物理卷创建卷组VG
    vgdisplay
    lvextend -r -l +100%FREE <lv-path> # 将物理卷上的空闲空间全部放到逻辑卷LV上
    lvdisplay

sync同步缓存写入固态存储:

    sync

设备管理:

    lspci # 列出所有PCI设备

    lsusb # 列出USB设备

    lsblk # 列出块设备

    lshw # 列出硬件

    setleds

    loadkeys

    dumpkeys

    MAKEDEV

# 网络管理

    telnet

    ping # 用于确定网络的连通性

    ifconfig # 查看TCP/IP设置

    arp # 用于确定IP地址的网卡物理地址

    route # 操作路由表的命令：

    nslookup # 查询IP地址和对应的域名

    ethtool # 查询网络设备信息

    nc/netcat # 设置路由器

netstat:

    netstat
    -a, --all, --listening # 显示所有socket, 默认只显示connected
    -l, --listening  # 显示listening
    -n, --numeric
    -p, --programs # 显示pid或程序名称
    # socket选项:
    -t, --tcp
    -u, --udp
    -w, --raw
    -x, --unix
    --ax25
    --ipx
    --netrom

    # 常用
    netstat -anp    # 查看哪些端口是打开的．
    sudo netstat -anp | grep port # 查看端口是否被使用
    sudo netstat -tulnp # 查看tcp&udp端口是否被监听

iftop:

    # <http://www.ex-parrot.com/~pdw/iftop/>
    $ sudo apt-get install iftop
    $ sudo iftop

tcpdump:

    tcpdump

wget:

    wget [option] [URL]

    -a, --append-output=FILE 输出重定向到日志
    -o, --output-file=FILE
    -q, --quiet    不输出
    -b, --background

    -t, --tries=NUMBER    超时重连次数, 0表示不限制, 默认20
    -nc, --no-clobber    不覆盖原有文件
    -N, --timestamping   只下载比本地新的文件
    -c, --continue    断点续传
    -T, --timeout=SECONDS    超时时间, 默认900s
    -w, --wait=SECONDS    重连之间的等待时间
    -O, --output-document=FILE, 重命名下载文件

    -nH, --no-host-directories 不创建站点的根目录
    -x, --force-directories    创建和服务器一样的结构下载
    -P, --directory-prefix=PREFIX  指定下载的目录

    -R,  --reject=LIST 排除下载的文件
    -r, --recursive  迭代下载
    -np, --no-parent 不下载父目录的内容

    # 同步目录
    wget -Nc -r -np -nH --cut-dirs=3 -R "index.*, *.js, *.css, *.html, *.jpg, *.png, *.gif" -P /path/to/source/ http://host/path/to/dest/

curl:

    curl

iptables:

    iptables

misc:

    # 在Network里面研究的几个常用命令
    ftp(参考network-ftp)
    snmp(参考network-snmp)
    ssh/scp/sftp(参考network-ssh)

***
