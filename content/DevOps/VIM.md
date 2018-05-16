Title: VIM
Date: 2016-04-02 21:11:26
Tags: Vi, Vim



# vim

<http://www.vim.org>

<https://github.com/vim/vim>

类似编辑器:

* emacs
* Atom(github的开源跨平台编辑器，支持插件。)
* VSCode(微软的开源跨平台的编辑器，支持插件。)

# Vim安装和配置

查看vim版本和编译信息：

    vim --version

安装vim：

    $ sudo apt-get install vim
    $ yum install vim

源码安装vim：

    $ sudo apt-get build-dep vim
    $ cd vim/src

    $ ./configure \
    --with-features=huge \
    --with-compiledby="Canux" \
    --enable-multibyte \
    --enable-gui=gtk2 \
    --enable-gpm \
    --prefix=/usr \
    --enable-cscope \
    --enable-fontset \
    --enable-xim \
    --enable-fail-if-missing \
    --enable-mzschemeinterp \
    --enable-perlinterp \
    --enable-luainterp \
    --enable-tclinterp\
    --enable-rubyinterp \
    --enable-pythoninterp \
    --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \
    --enable-python3interp \
    --with-python3-config-dir=/usr/lib/python3.4/config-3.4m-x86_64-linux-gnu

    $ make VIMRUNTIMEDIR=/usr/share/vim/vim74
    $ sudo make install

***

# Vim相关项目

## neovim

<https://github.com/neovim/neovim>

vim的升级版，修复了vim的bug，同时集成了许多插件。

## spacevim

<https://github.com/SpaceVim/SpaceVim>

更高效的vim.

## sp13

分布式vim。

<https://github.com/spf13/spf13-vim>

## vim-galore

<https://github.com/mhinz/vim-galore>

vim的知识库．

## vimrc

vim的终极配置．

<https://github.com/amix/vimrc>

***

# vim常见用法和特殊用法

vim的三种模式：

    v    # 视觉模式
    i    # 插入模式
    esc  # 普通模式

常用命令:

    :    # 进入命令行
    :help # 查看帮助
    :q
    :q!
    :qa
    :w
    :n1, n2 w
    :wq
    :x

    # 常用设置
    :set mouse=a # enable mouse
    :set list    # 查看tab键
    :set nolist
    :set nu
    :set nonu
    :! [shell-command]   # 可以运行外部命令

    # 替换
    :s/old/new    # 替换第一个
    :ns/old/new/g    # 替换行n
    :n1,n2s/old/new/g    # 替换n1-n2之间的全部
    :%s/old/new/g    # 替换整个文件
    :%s/old/new/gc    # 替换整个文件，弹出提示
    :%/^/inseart/g    # 行首插入
    :%/$/inseart/g    # 行尾插入

    # 删除
    :g/pattern/d    # 删除匹配的行
    :n1,n2g/pattern/d    # 删除n1-n2中匹配的行
    :v/pattern/d    # 删除不匹配的行
    :n1,n2d    # 删除n1-n2行
    :%s/^\s\+//g    # 删除行首空格
    :%s/\s\+$//g    # 删除行尾空格
    :1,$d    # 删除所有行，包括行号
    :%s/^.*$//g    # 清空内容，保留行号

常用快捷键：

    # 左右跳转快捷键
    n h    # left
    n l    # right
    0      # 跳转到一行的首字母
    ^      # 跳转到一行的非空首字母
    n $    # 跳转一行的结尾

    # 上下跳转快捷键
    n k    # up
    n j    # down
    n G  # 跳转到行号n, 默认最后一行
    n gg # 同上，默认第一行

    # 文本移动(向前就是向右，向后就是向左)
    n w     # 向前移动n个单词
    n W     # 向前移动n个空格分割的单词
    n e     # 跳转到最后第n个单词
    n E     # 跳转到以空格分割的最后地n个单词
    n b     # 向后n个单词
    n B     # 向后n个单词，以空格分割

    # 模式匹配
    N  /{pattern}[/[offset]]<CR> # 向后查找N个匹配
    N  ?{pattern}[?[offset]]<CR> # 向前查找N个匹配
    N n # 向后查看
    N N # 向前查看

    # 大小写转换
    ~    # 单个字符相互转换
    U    # 转换成大些
    u    # 转换成小写
    g~~    # 转换当前行大小写
    :%s/./\U&/g    # 全文改成大些

特殊字符处理：

    # 查看特殊字符，字符编码和二合字母
    :digraphs
    :h digraph-table
    # 直接使用字符编码,插入模式下输入
    <ctrl-v> + <dec>
    # 使用二合字母，插入模式下输入
    <ctrl-k> + <digraph>

***

# vim-plugins-manager

vim的插件管理器

## pathogen

<https://github.com/tpope/vim-pathogen>

vim的本地管理插件。

## vundle

<https://github.com/VundleVim/Vundle.vim>

vim的在线管理插件。

## vim-plug

<https://github.com/junegunn/vim-plug>

vundle的迷你版。

## dein

dein已经取代neobundle, 可以用于vim和neovim。

旧版本：

<https://github.com/Shougo/neobundle.vim>

新版本：

<https://github.com/Shougo/dein.vim>

***

# vim-plugins

vim常用的插件

## YCM

## syntastic

***

# 常用情景

vim内部使用sudo保存:

    :w !sudo tee %
