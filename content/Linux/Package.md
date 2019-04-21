Title: Package
Date: 2016-06-07 16:57:45
Tags: Linux, dpkg, yum, zypper



# DPKG

debian的包管理机制。

## dpkg

dpkg的本地前端工具。

deb - Debian binary package format

dpkg - package manager for Debian

    dpkg
    dpkg -X  ./xxx.deb  xxx  # 将deb包解压到xxx目录
    dpkg -e  ./xxx.deb  xxx/DEBIAN # 将control信息解压
    dpkg -l | grep pkg # 查看安装的包

dpkg-reconfigure - reconfigure an already installed package

    dpkg-reconfigure

dpkg-deb - Debian package archive (.deb) manipulation tool

    # 创建debian包
    dpkg-deb -b|--build <directory> [<deb>]

    # <directory> 结构, DEBIAN/control　是必需的
    |- debian_root
       |- DEBIAN
          |- preinst/preinstallation # 解压deb包之前执行
          |- prerm/preremove
          |- control
          |- postinst/postinstallation # 解压完成之后执行，通常用来配置
          |- postrm/postremove
          |- copyright
          |- changelog
          |- conffiles
       |- etc
          |- init.d
             |- <service>
          |- logrotate.d
             |- <service>
       |- user/local/...
       |- opt/...

    # control文件
    Package
    Version
    Description
    Section: utils/net/mail/text/x11/...
    Priority: required/standard/optional/extra/...
    Essential: yes/no
    Architecture: i386/amd64/...
    Source:
    Depends:    # 运行该process需要的依萊, 只能安装之前安装好，或者用gdebi安装
    Pre-Depends:
    Recommends:
    Suggests:
    ...
    最后一行需要空行

    # 查看包信息
    dpkg-deb -I XXX.deb

dpkg-query - a tool to query the dpkg database

    dpkg-query

## gdebi - Simple tool to install deb files

dpkg的本地前端工具。

使用gdebi安装deb包会自动解决依赖问题:

安装gdebi:

    $ sudo apt-get install gdebi-core
    $ sudo apt-get install gdebi-gtk
    $ sudo aptitude install gdebi-core # install gdebi itself
    $ sudo aptitude install gdebi-gtk # install gdebi GUI

使用gdebi:

    sudo gdebi XXX.deb # install package

## apt - command-line interface

dpkg的远程前端工具。

apt - command-line interface

    $ apt install package

apt-get - APT package handling utility -- command-line interface

    $ sudo apt-get option command package

    # command:
    install
    remove
    purge
    download
    source
    update

    # install
    # 可以通过apt-cache madison查看version
    apt-get install <package>=<version>

    # option:
    -d, --download-only
    --print-uris
    -y,--yes,--assume-yes    # 交互时确认
    -f,--force-yes
    --reinstall
    --allow-unauthenticated
    --allow-downgrades (>= ubuntu1604)

    # 打印在当前环境安装该包需要的所有以来的下载连接信息
    apt-get --print-uris install package

aptitude - high-level interface to the package manager

    $ sudo aptitude install package

apt-cache - query the APT cache

    $ apt-cache showpkg <pkg>
    $ apt-cache showsrc <pkg>
    $ apt-cache search <pkg>
    $ apt-cache madison <pkg> # 查看当前源可以安装的版本
    $ apt-cache policy <pkg>

    # 查看哪些包依赖该包
    $ apt-cache rdepends <pkg>
    # 查看该包依赖哪些包
    $ apt-cache depends <pkg>
    # 查看依赖，　以及依赖的依赖
    $ apt-cache --recurse depends <pkg>

# install

***

# RPM

redhat的包管理机制。

## rpm

rpm的本地前端工具。

rpm -

rpmbuild -

## yum

rpm的远程前端工具。

yum -

***

# zypper

suse的包管理机制。

***

# Alien

> alien is a program that converts between Red Hat rpm, Debian deb, Stampede slp, Slackware tgz, and Solaris pkg file formats.

# gbp

通过git来管理deb或rpm包．

<https://github.com/agx/git-buildpackage>

    $sudo -E pip install gbp

# fpm

通过fpm来创建deb/rpm包

<https://github.com/jordansissel/fpm>

***

# patch
