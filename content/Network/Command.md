Title: Network Command
Date: 2019-03-31 21:51:25
Tags: Network, Linux, Windows



# telnet

    telnet

# nc/netcat

    nc -z IP PORT # 查看指定tcp://ip:port是否监听
    nc -zu IP PORT # 查看udp://ip:port是否监听

# ping

    $ sudo apt-get install iputils-ping
    ping # 用于确定网络的连通性

# ifconfig

    $ sudo apt-get install net-tools
    ifconfig # 查看up的interface
    ifconfig -a  # 查看所有的interface
    ifconfig <bridge>/<interface> up/down

# brctl

    $ sudo apt-get install bridge-utils
    brctl show
    brctl addbr <bridge> # 添加bridge
    brctl delbr <bridge> # 删除bridge
    brctl addif <bridge> <interface> # 绑定interface到bridge
    brctl delif <bridge> <interface> # 删除bridge上的interface

# ip

    ip link

# route

    route # 操作路由表的命令：

# arp

    arp # 用于确定IP地址的网卡物理地址

# nslookup

    nslookup # 查询IP地址和对应的域名

# ethtool

    ethtool # 查询网络设备信息

# netstat

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

# iftop

查看网络流量

    # <http://www.ex-parrot.com/~pdw/iftop/>
    $ sudo apt-get install iftop
    $ sudo iftop

# tcpdump

    tcpdump

    tcpdump udp port <port> 抓udp 在port端口的包
    tcpdump -i <interface> host <ip>

# wget

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

