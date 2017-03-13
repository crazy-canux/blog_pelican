Title: Hexo
date: 2016-03-22 12:59:10
tags: Hexo



# Hexo

## 什么是hexo

>Hexo是用nodejs开发的快速、简洁且高效的博客框架，
>Hexo 使用Markdown（或其他渲染引擎）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。

hexo有大量的插件和主题。

[plugins](https://hexo.io/plugins/)

[themes](https://hexo.io/themes/)

## 安装hexo

需要安装依赖nodejs(包括npm)和git。

安装hexo命令行插件hexo-cli：

    $sudo npm install hexo-cli -g

## Next

>Next是一种文雅的Hexo主题。
>一个主题，三种外观，选您所好。
>通过主题中的主题（亦称Scheme），您可以方便地改变您博客的外观，同时几乎所有配置同样适用。

[原生的Next](https://github.com/iissnan/hexo-theme-next)

[作者的Next](https://github.com/crazy-canux/hexo-theme-next)

***

# 快速使用

## 初始化

初始化一个hexo的目录：

    $hexo init <folder>

## 安装依赖

进入hexo目录安装依赖：

    $cd <folder>
    $sudo npm install <package-name>

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

    $hexo g
    $hexo generate

## 启动本地服务器

    $hexo s
    $hexo server

用浏览器打开链接即可本地查看默认博客。

## 写博文

    $hexo new post <article-name>

编辑这篇文章。

## 清理生成文件和缓存

    $hexo clean

再次运行hexo g和hexo s查看。

## 安装部署插件

    $sudo npm install hexo-deployer-git --save

修改全局配置文件，参考插件的[github](https://github.com/hexojs/hexo-deployer-git)
针对github需要新建一个名字为&lt;your-github-name>.github.io的仓库。

## 部署到github

    $hexo d
    $hexo deploy

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

    $hexo clean
    $hexo g
    $hexo d

github访问http://<your-github-name>.github.io即可。

coding访问http://<your-coding-name>.coding.me/<your-coding-name>

绑定自己的域名：
1. 在域名供应商购买域名后添加解析，记录类型A或者CNAME，主机类型@或者www，记录值可以是http://<your-github-name>.github.io或者通过ping获取的ip地址。
2. 在<your-blog>/source/新建文件CNAME，添加你购买的域名<your-domain>.com。
3. 正常部署到github。
4. 访问http://<your-doamin>.com即可。

***

# 安装hexo插件

[plugins](https://hexo.io/plugins/)

    $sudo npm install <plugin-name> --save

# 配置hexo插件

全局配置文件是&lt;folder>/_config.yml

>>\# Extensions

>\## Plugins: https://hexo.io/plugins/

>\## Themes: https://hexo.io/themes/

>        theme: next

>        Plugins:

>        - hexo-deployer-git

>\# Extend plugins

>\## deploy

>        deploy:

>        type: git
>
>        repo: git@github.com:<your-github-name>/<your-github-name>.github.io.git

>        branch: master

>        message:

# 站点地图

    $npm install hexo-generator-sitemap --save

>\## sitemap

>        sitemap:

>            path: sitemap.xml

<https://github.com/hexojs/hexo-generator-sitemap>

# RSS

    $npm install hexo-generator-feed --save

>\## feed

>        feed:

>          type: atom

>          path: atom.xml

>          limit: 20

>          hub:

<https://github.com/hexojs/hexo-generator-feed>

# SEO优化

    $npm install hexo-generator-seo-friendly-sitemap --save

>        sitemap:

>            path: sitemap.xml

<https://github.com/ludoviclefevre/hexo-generator-seo-friendly-sitemap>

***

# Next

以hexo主题next为例

中文文档：

<http://theme-next.iissnan.com/>

英文文档：

<https://github.com/iissnan/hexo-theme-next/blob/master/README.en.md>

# 主题配置文件

主题配置文件在：

&lt;folder>/themes/next/_config.yml

# 主题配置

>\# ---------------------------------------------------------------

>\# 站点信息设置

>\# ---------------------------------------------------------------

>\# 将制作好的favicon图标放到/source里面。

>     favicon: /favicon.ico

>\# SEO优化的关键字。

>     keywords: "Canux, CHENG, blog"

>\# 指定站点的起始日期。

>     since: 2013

>\# ---------------------------------------------------------------

>\# 菜单设置

>\# ---------------------------------------------------------------

>\# 顶部菜单栏

>     menu:

>       home: /

>       about: /about

>       categories: /categories

>       tags: /tags

>       archives: /archives

>       #commonweal: /404.html

>\# 菜单栏图标,使用fontawsome

>     menu_icons:

>       enable: true

>       home: home

>       about: user

>       categories: th

>       tags: tags

>       archives: archive

>       #commonweal: heartbeat

>\# ---------------------------------------------------------------

>\# 主题方案设计: Must | Mist | Pisces

>\# ---------------------------------------------------------------

>     scheme: Muse

>\# ---------------------------------------------------------------

>\# 捐赠设置

>\# ---------------------------------------------------------------

>     reward_comment: 您的支持是我创作的动力!

>     wechatpay: /images/myimages/wechatpay.jpg

>     alipay: /images/myimages/alipay.jpg

>\# ---------------------------------------------------------------

>\# 侧边栏设置

>\# ---------------------------------------------------------------

>\# 社交信息

>     social:

>       GitHub: https://github.com/crazy-canux

>       Stackoverflow: http://stackoverflow.com/

>       LinkedIn: http://www.linkedin.com/profile/preview?locale=zh_CN&trk=prof-0-sb-preview-primary-button

>       E-mail: mailto:canuxcheng@gmail.com

>\# 社交信息图标，使用fontawsome。

>     social_icons:

>       enable: true

>       GitHub: github

>       LinkedIn: linkedin

>       Stackoverflow: stack-overflow

>       E-mail: envelope

>\# 友情链接

>     links_title: Links

>     links:

>       CSDN: http://bbs.csdn.net/home

>       51CTO: http://bbs.51cto.com/

>       ChinaUnix: http://bbs.chinaunix.net/

>       ITPUB: http://www.itpub.net/forum.php

>\# 侧边栏图像

>     avatar: /images/myimages/avatar.jpg

>\# TOC(table of contents)设置

>     toc:

>       enable: true

>       number: true

>\#  设置 4.0 International 许可证: by | by-nc | by-nc-nd | by-nc-sa | by-nd | by-sa | zero

>     creative_commons: zero

>\# 侧边栏位置: left | right

>     sidebar:

>       position: left

>\# 侧边栏显示方式： post | always | hide | remove

>     display: post

>\# ---------------------------------------------------------------

>\# 其它设置

>\# ---------------------------------------------------------------

>\# 使用Custom Logo.

>     custom_logo:

>       enabled: false

>       image:

>\# 代码高亮主题: normal | night | night eighties | night blue | night bright

>     highlight_theme: night eighties

>\# 自动滚动页面

>     scroll_to_more: true

>\# 自动摘录

>     auto_excerpt:

>       enable: true

>       length: 150

>\# 使用Lato font

>     use_font_lato: true

>\# ---------------------------------------------------------------

>\# 第三方插件: 一般都需要去插件的官网注册使用。

>\# ---------------------------------------------------------------

>\# MathJax Support

>     mathjax: true

>

>\# Google Analytics - US

>     #google_analytics:

>\# Facebook sdk Analytics - US

>     facebook_sdk:

>       enable: false

>       app_id: #<app_id>

>       fb_admin: #<user_id>

>       like_button: #true

>       webmaster: #true

>\# CNZZ Analytics - CN

>     cnzz_siteid: ******

>\# leancloud Analytics - CN

>     leancloud_visitors:

>       enable: false

>       app_id: #<app_id>

>       app_key: #<app_key>

>\# Baidu Analytics

>     #baidu_analytics: ******

>\# Tencent Analytics

>     #tencent_analytics: ******

>

>\# Disqus - US

>     #disqus_shortname: ******

>\# Duoshuo - CN

>     duoshuo_shortname: ******

>\# Make duoshuo show UA

>     duoshuo_info:

>       ua_enable: true

>       admin_enable: false

>       user_id:

>       #admin_nickname: ROOT

>\# Make duoshuo show hot artical

>     duoshuo_hotartical: true

>

>\# AddThis - US

>     #add_this_id:

>\# JiaThis - CN

>     jiathis: true

>\# Baidu Share

>     #baidushare: true

>\# Duoshuo Share

>     #duoshuo_share: true

>

>\# Swiftype - US

>     swiftype_key: ******

>\# Tinysou - CN

>     #tinysou_Key

>\#! ---------------------------------------------------------------

>\#! 谨慎编辑的主题信息

>\#! ---------------------------------------------------------------

>\# 侧边栏移动插件 Motion

>     use_motion: true

>\# 图片弹出插件 Fancybox

>     fancybox: true

>\# Static files

>     vendors: vendors

>     css: css

>     js: js

>     images: images

>\# Theme version

>     version: 0.5.0
