Title: DevOps
Date: 2016-04-15 09:41:39
Tags: DevOps, Development, Operations, QA



# DevOps

DevOps包括ChatOps, 敏捷开发，持续集成,持续交付,持续发布/部署，QA(自动化测试），智能监控和日志管理等内容．

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

# CD

Continuous Delivery.

持续交付包括：

* 将通过测试的代码部署到Staging.

# Continuous Release/Deploy

持续部署/发布包括：

* 将通过评审的交付代码部署到Production.

***

# CI/CD的工具

持续集成和部署

## Jenkins

## travis CI

<https://travis-ci.org/>

travis CI是基于github的CI工具, 部署代码然后运行测试代码.

在github项目添加.travis.yml文件：

    language: python
    python:
      - "2.7"
    install:
      - pip install -r requirements.txt
      - pip install coveralls
    script:
      - coverage run --source=pymonitoringplugins setup.py test
    after_success:
      - coveralls

## circleci

<https://circleci.com/>

***

# coverage的工具

统计单元测试的覆盖率

## coveralls

<https://coveralls.io/>

## codecov

<https://codecov.io/>

***

# stackstorm

StackStorm is a platform for integration and automation across services and tools, taking actions in response to events.

For DevOps and ChatOps.

<https://github.com/StackStorm/st2>

# Drone

Drone is a Continuous Delivery platform built on Docker, written in Go

<https://github.com/drone/drone>

# sentry

Sentry is a cross-platform crash reporting and aggregation platform.

<https://github.com/getsentry/sentry>

<https://github.com/getsentry/raven-python>

<https://github.com/getsentry/raven-java>

# supervisor

Supervisor process control system for UNIX/Linux.

<https://github.com/Supervisor/supervisor>

    $pip install supervisor

***

# redmine

ruby开发的项目管理工具,集成bug和wiki工具．

***

# dokuwiki

php开发的wiki管理工具

***

# Atlassian

Jira for Porject Management.

Bitbucket for Source code management.

Bamboo for CI/CD.

***

# bugzilla

perl开发的bug追踪系统．

***

# errbot

python开发的ChatOps工具．

<https://github.com/errbotio/errbot>

***

# zulip

团队聊天工具介绍

<https://github.com/zulip/zulip>
