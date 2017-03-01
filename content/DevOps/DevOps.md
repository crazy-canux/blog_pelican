Title: DevOps
Date: 2016-04-15 09:41:39
Tags: DevOps, Development, Operations, QA



# DevOps

DevOps包括敏捷开发，持续集成,持续交付,持续/发布部署，智能监控和日志管理等内容．

DevOps涉及到三个部门：
* Development
* Operations
* Quality Assurance

***

# CI

Continuous Integration.

持续集成包括：
* 编译代码.
* 静态代码分析.
* 自动化测试，例如selenium.
* 代码覆盖率分析.
* 构建，例如docker.

CI工具分为:
* Self Hosted CI, 自建机房，例如Jenkins,Fabric.
* Hosted CI, SAAS.

# CD

Continuous Delivery.

持续交付包括：
* 将通过测试的代码部署到Staging.

# Continuous Release/Deploy

持续部署/发布包括：
* 将通过评审的交付代码部署到Production.

# travis CI & coveralls

<https://travis-ci.org/>

<https://coveralls.io/>

travis CI和coveralls是基于github的CI工具．

在github项目添加.travis.yml文件：

    language: python
    python:
      - "2.7"
    install:
      - pip install -r requirements.txt
      - pip install coveralls
    script:
      - ...
    after_success:
      - coveralls

***

# sentry

<https://github.com/getsentry/sentry>

# pybuilder

<https://github.com/pybuilder/pybuilder>

# stackstorm

<https://github.com/StackStorm/st2>

# supervisor

<https://github.com/Supervisor/supervisor>

***

配置批量管理工具

# puppet

# chef

# salt

# ansible

***

密码管理工具

# KeePassX

<https://www.keepassx.org/>

<https://github.com/keepassx/keepassx>

***

项目管理工具

# redmine

ruby开发的项目管理工具

***

文档管理工具

# dokuwiki

php开发的文档管理工具

***

文档阅读工具

# zeal

# dash

