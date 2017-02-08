---
layout: post
title: Hexo
comments: true
date: 2016-03-22 12:59:10
updated:
tags:
- javascript
- nodejs
- npm
- hexo
- next
categories:
- Web
- Blog
permalink:
---

# Hexo

## 什么是hexo

>Hexo是用nodejs开发的快速、简洁且高效的博客框架，
>Hexo 使用Markdown（或其他渲染引擎）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。

hexo有大量的插件和主题。

[plugins](https://hexo.io/plugins/)

[themes](https://hexo.io/themes/)

## 安装hexo

需要安装依赖nodejs和git。

安装hexo命令行插件hexo-cli：

    sudo npm install hexo-cli -g

## Next

>Next是一种文雅的Hexo主题。
>一个主题，三种外观，选您所好。
>通过主题中的主题（亦称Scheme），您可以方便地改变您博客的外观，同时几乎所有配置同样适用。

[原生的Next](https://github.com/iissnan/hexo-theme-next)

[作者的Next](https://github.com/crazy-canux/hexo-theme-next)

***

# 安装依赖

## 安装nodejs

>Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行环境。
>Node.js 使用了一个事件驱动、非阻塞式 I/O 的模型，使其轻量又高效。
>Node.js 的包管理器npm，是全球最大的开源库生态系统。

常说的javascript是前端语言，nodejs就是后端版本的javascript。

ubuntu/debian安装：

    sudo apt-get install nodejs

源码安装参考github或官网：

[node](https://github.com/nodejs/node)

## 安装npm

javascript的包管理器，npm和hexo都是javascript包。
高版本的nodejs自带npm。

ubuntu/debian安装：

    sudo apt-get install npm

源码安装参考github或官网：

[npm](https://github.com/npm/npm)


## 安装nvm或n

nvm和n都是node的版本管理器。

具体安装参考github:

[nvm](https://github.com/creationix/nvm)

[n](https://github.com/tj/n)

## 安装git

git是分布式的版本控制系统。

ubuntu/debian安装：

    sudo apt-get install git

源码按抓参考github或官网：

[git](https://github.com/git/git)

***

# 快速使用

## 初始化

初始化一个hexo的目录：

    hexo init <folder>

## 安装依赖

进入hexo目录安装依赖：

    cd <folder>
    sudo npm install

默认安装下列依赖：

    hexo
    hexo-server
    hexo-generator-index
    hexo-generator-archive
    hexo-generator-category
    hexo-generator-tag
    hexo-renderer-ejs
    hexo-renderer-marked
    hexo-renderer-stylus

## 查看文件和目录

安装完成后有下列

文件：

    _config.yml
    db.json
    package.json

目录：

    node_modules
    scaffolds
    source
    themes

## 生成静态文件

    hexo g
    hexo generate

## 启动本地服务器

    hexo s
    hexo server

用浏览器打开链接即可本地查看默认博客。

## 写博文

    hexo new post <article-name>

编辑这篇文章。

## 清理生成文件和缓存

    hexo clean

再次运行hexo g和hexo s查看。

## 安装部署插件

    sudo npm install hexo-deployer-git --save

修改全局配置文件，参考插件的[github](https://github.com/hexojs/hexo-deployer-git)
针对github需要新建一个名字为&lt;your-github-name>.github.io的仓库。

## 部署到github

    hexo d
    hexo deploy

在浏览器打开http://&lt;your-github-name>.github.io/查看博客。

***

# 配置

## 全局配置

全局配置文件是&lt;folder>/_config.yml

>>\# Hexo Configuration

>\## Docs: https://hexo.io/docs/configuration.html

>\## Source: https://github.com/hexojs/hexo/

>>\# Site

>        title:

>        subtitle:

>        description:

>        author:

>        language: zh-Hans

>        timezone: Asia/Shanghai

>>\# URL

>\## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'

>        url: http://<your-github-name>.github.io/

>        root: /

>        permalink: :year/:month/:day/:title/

>        permalink_defaults:

>>\# Directory

>        source_dir: source

>        public_dir: public

>        tag_dir: tags

>        archive_dir: archives

>        category_dir: categories

>        code_dir: downloads/code

>        i18n_dir: :lang

>        skip_render:

>>\# Writing

>        new_post_name: :title.md # File name of new posts

>        default_layout: post # post | page | draft

>        titlecase: false # Transform title into titlecase

>        external_link: true # Open external links in new tab

>        filename_case: 0

>        render_drafts: false

>        post_asset_folder: false

>        relative_link: false

>        future: true

>        highlight:

>        enable: true

>        line_number: true

>        auto_detect: true

>        tab_replace: ''

>>\# Category & Tag

>        default_category: uncategorized

>        category_map:

>        tag_map:

>>\# Date / Time format

>\## Hexo uses Moment.js to parse and display date

>\## You can customize the date format as defined in

>\## http://momentjs.com/docs/#/displaying/format/

>        date_format: YYYY-MM-DD

>        time_format: HH:mm:ss

>>\# Pagination

>\## Set per_page to 0 to disable pagination

>        per_page: 10

>        pagination_dir: page

>>\# Extensions

>\## Plugins: https://hexo.io/plugins/

>\## Themes: https://hexo.io/themes/

>        theme: hexo-theme-canux

>        Plugins:

>        - hexo-deployer-git

>>\# Extend plugins

>\## deploy

>        deploy:

>          type: git

>          repo:

>             github: https://github.com/crazy-canux/crazy-canux.github.io.git,master

>             coding: https://git.coding.net/Canux/Canux.git,master

## 主题配置

hexo官方默认主题是&lt;folder>/themes/landscape。

主题配置文件是&lt;folder>/themes/landscape/_config.yml

现在将默认主题替换成自己喜欢的主题：

    cd <folder>/themes
    git clone <github-url-of-your-favourite-theme>

然后将全局配置的 theme: landscape 改为 theme: &lt;your-favourite-theme-name>

***

# 部署

部署到github和coding(gitcafe)：

    hexo clean
    hexo g
    hexo d

github访问http://<your-github-name>.github.io即可。

coding访问http://<your-coding-name>.coding.me/<your-coding-name>

绑定自己的域名：
1. 在域名供应商购买域名后添加解析，记录类型A或者CNAME，主机类型@或者www，记录值可以是http://<your-github-name>.github.io或者通过ping获取的ip地址。
2. 在<your-blog>/source/新建文件CNAME，添加你购买的域名<your-domain>.com。
3. 正常部署到github。
4. 访问http://<your-doamin>.com即可。
