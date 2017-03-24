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

    sudo apt-get install vim
    yum install vim

源码安装vim：

    sudo apt-get build-dep vim
    cd vim/src

    ./configure \
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

    make VIMRUNTIMEDIR=/usr/share/vim/vim74
    sudo make install

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

# vim用法

行首/行尾插入字符串：

    :%/^/inseart/g
    :%/$/inseart/g

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

# pathogen

<https://github.com/tpope/vim-pathogen>

vim的本地管理插件。

# vundle

<https://github.com/VundleVim/Vundle.vim>

vim的在线管理插件。

# vim-plug

<https://github.com/junegunn/vim-plug>

vundle的迷你版。

# dein

dein已经取代neobundle, 可以用于vim和neovim。

旧版本：

<https://github.com/Shougo/neobundle.vim>

新版本：

<https://github.com/Shougo/dein.vim>

***

# vim-plugins

vim常用的插件

# YCM

# syntastic

