---
layout: post
title: Django之MISC
comments: true
date: 2017-01-04 01:13:36
updated:
tags:
categories:
- Python
- Django
permalink:
---

# Django的国际化和本地化

settings.py里面和国际化和本地化相关的设置:

    USE_I18N = True
    USE_L10N = True
    TIME_ZONE = 'UTC'
    USE_TZ = True

## 国际化(i18N)

由开发者完成,本地化的准备工作.

<http://www.i18nguy.com/unicode/language-identifiers.html>

    LANGUAGE_CODE = 'en-us' # default

    LANGUAGES = [
        ('en-US', _('English')),
        ('zh-CN', _('Chinese')),
    ]

## 本地化(l10N)

由翻译者完成.

***

# Django的安全

***

# Django的性能优化

***

# Django的地理框架

