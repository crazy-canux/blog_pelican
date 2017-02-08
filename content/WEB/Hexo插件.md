---
layout: post
title: Hexo插件
comments: true
date: 2016-04-06 21:58:31
updated:
tags:
- nodejs
- npm
- hexo
- plugin
categories:
- Web
- Blog
permalink:
---

# 安装hexo插件

[plugins](https://hexo.io/plugins/)

    sudo npm install <plugin-name> --save

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

    npm install hexo-generator-sitemap --save

>\## sitemap

>        sitemap:

>            path: sitemap.xml

<https://github.com/hexojs/hexo-generator-sitemap>

# RSS

    npm install hexo-generator-feed --save

>\## feed

>        feed:

>          type: atom

>          path: atom.xml

>          limit: 20

>          hub:

<https://github.com/hexojs/hexo-generator-feed>

# SEO优化

    npm install hexo-generator-seo-friendly-sitemap --save

>        sitemap:

>            path: sitemap.xml

<https://github.com/ludoviclefevre/hexo-generator-seo-friendly-sitemap>

