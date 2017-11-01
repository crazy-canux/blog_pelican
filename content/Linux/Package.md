Title: Package
Date: 2016-06-07 16:57:45
Tags: Linux, dpkg, yum, zypper



# DPKG

debian的包管理机制。

## dpkg

dpkg的本地前端工具。

deb - Debian binary package format
dpkg - package manager for Debian
dpkg-reconfigure - reconfigure an already installed package
dpkg-deb - Debian package archive (.deb) manipulation tool
dpkg-query - a tool to query the dpkg database

    dpkg --help

## gdebi - Simple tool to install deb files

dpkg的本地前端工具。

安装gdebi:

    $ sudo apt-get install gdebi-core
    $ sudo apt-get install gdebi-gtk
    $ sudo aptitude install gdebi-core # install gdebi itself
    $ sudo aptitude install gdebi-gtk # install gdebi GUI

使用gdebi安装deb包会自动解决依赖问题:

    sudo gdebi XXX.deb # install package

## apt - command-line interface

dpkg的远程前端工具。

apt - command-line interface

    $ apt install package

apt-get - APT package handling utility -- command-line interface

    $ sudo apt-get install package

aptitude - high-level interface to the package manager

    $ sudo aptitude install package

***

# RPM

redhat的包管理机制。

## rpm

rpm的本地前端工具。

rpm -

rpmbuild -

## yum

rpm的远程前端工具。

***

# zypper

suse的包管理机制。

***

# Alien

> alien is a program that converts between Red Hat rpm, Debian deb, Stampede slp, Slackware tgz, and Solaris pkg file formats.

# gbp

通过git来管理debian或rpm包．

<https://github.com/agx/git-buildpackage>

    $sudo -E pip install gbp
