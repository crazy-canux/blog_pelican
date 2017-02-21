Title: Pelican
Date: 2013-04-01 12:49:49
Tags: Pelican



# Pelican

python开发的静态站点生成器.

<http://blog.getpelican.com/>

<https://github.com/getpelican/pelican>

<http://pelican-docs-zh-cn.readthedocs.io/en/latest/getting_started.html>

<http://pelican-zh.readthedocs.io/en/latest/zh-cn/>

# 搭建博客

创建环境:

    $mkdir blog_pelican
    $cd blog_pelican
    $virtualenv .venv
    $source .venv/bin/activate
    $pip install pelican
    $pip install markdown

创建pelican项目:

    $pelican-quickstart

生成下列文件和目录:

    publishconf.py # 主配置文件
    pelicanconf.py # 发布的配置文件
    fabfile.py # fabric配置文件
    Makefile   # make配置文件
    develop_server.sh # 用于开启测试服务器
    content # 用于存放所有文章
    output # 静态生成文件

# 发布站点

pelican部署博客:

    # 将rst或md格式转换成html,默认导入到output.
    $pelican content
    $pelican content -s pelicanconf.py

    # 启动web服务器预览
    $cd output
    $python -m pelican.server
    $python2.7 -m SimpleHTTPServer
    $python3 -m http.server
    $firefox http://localhost:8000/

    # 部署站点
    # 一般publishconf.py导入pelicanconf.py即可，配置一样．
    $pelican content -s publishconf.py

fabric部署博客:

    $fab github # 一键部署到github/coding.

make部署博客:

    $make github # 一键部署到github/coding.

***

# 配置

pelicanconf.py

publishconf.py

参考pelican和hexo的配置：

<https://github.com/crazy-canux/blog_hexo>

<https://github.com/crazy-canux/blog_pelican>

***

# Theme

添加主题

    $cd blog_pelican
    $git submodule add https://github.com/getpelican/pelican-themes.git themes

安装主题：

    $cd pelican-themes
    $pelican-themes -i bootstrap2

在pelicanconf.py添加主题：

    THEME = 'bootstrap2'

***

# Plugin

添加插件：

    $cd blog_pelican
    $git submodule add https://github.com/getpelican/pelican-plugins.git plugins

***

# 部署到github

在makefile添加三个变量：

    GITHUB_BRANCH=master
    GITHUB_URL=https://github.com/crazy-canux/crazy-canux.github.io.git

修改makefile:

    github: publish
        cd $(OUTPUTDIR); git init; git remote add origin $(GITHUB_URL); git add -A; git commit -m "[$(shell date +%Y%m%d)]update"; git push -f -u origin $(GITHUB_BRANCH)

一键部署：

    $make github
