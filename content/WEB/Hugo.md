Title: Hugo
Date: 2013-04-01 12:49:49
Tags: Hugo



# Hugo

go开发的静态站点生成器.

<https://github.com/gohugoio/hugo>

<https://gohugo.io/>

# 搭建博客

创建环境:

    # linux
    $ sudo apt-get install hugo
    # windows
    PATH:   C:\Hugo\bin

创建hugo项目:

    $ hugo new site blog

生成下列文件和目录:

    config.toml
    archetypes
    content    # md 文件
    data
    layouts
    static
    themes
    bytes

***

# Theme

<https://github.com/gohugoio/hugoThemes>

下载所有主题:

    cd blog
    git clone --depth 1 --recursive https://github.com/gohugoio/hugoThemes.git themes

下载单个主题：

    cd themes
    git clone url

在pelicanconf.py添加主题：

    THEME = 'bootstrap2'

***

# 创建页面

    ## content/about.md
    $ hugo new about.md

# 创建文章

    ## content/page/first.md
    $ hugo new post/first.md

***

 # 本地测试

     $ hugo server --theme=hyde --buildDrafts
     $ firefox http://localhost:1313

***

# 部署到github

先在github创建repo.

    $ hugo --theme=<theme> --baseUrl="https://<user>.github.io/"

push到github:

    $ cd public
    $ git init
    $ git remote add origin https://github.com/<user>/<user>.github.io.git
    $ git add -A
    $ git commit -m "first push."
    $ git push -u origin master
