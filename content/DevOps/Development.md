Title: Development
Date: 2016-04-15 09:41:39
Tags: DevOps, Development



# Development

开发相关的工具

传统的软件开发采用的是瀑布式开发流程．

现代的软件开发采用的是敏捷开发流程(Agile development).

***

# 怎样选择Licenses

<http://choosealicense.com/licenses/>

![pic](/images/license.jpeg)

***

# semver

语义化版本．

<http://semver.org/lang/zh-CN/>

<https://github.com/mojombo/semver>

    主版本号.次版本号.修订号
    Major.Minor.Patch

    Major: 做了不兼容的API修改
    Minor: 做了向下兼容的功能性新增
    Patch: 做了向下兼容的问题修正

***

# 文档阅读工具

## zeal

## dash

***

# cookiecutter

一个快速建立工程模板的命令行工具．

<https://github.com/audreyr/cookiecutter>

<https://github.com/audreyr/cookiecutter-pypackage>

    $sudo -E pip install cookiecutter
    # 创建python项目
    $cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
    # 创建django格式的python项目
    $cookiecutter https://github.com/pydanny/cookiecutter-django
    # 创建openstack格式的python项目
    $cookiecutter https://git.openstack.org/openstack-dev/cookiecutter.git
    $cookiecutter https://github.com/openstack-dev/cookiecutter.git

***

# bumpversion

版本管理工具

<https://github.com/peritus/bumpversion>

    $sudo -E pip install bumpversion
    # put config in setup.cfg
    [bumpversion]
    current_version = 1.2.0
    files = pymonitoringplugins/__init__.py
    $bumpversion major/minor/patch --commit # commit新版本

***
