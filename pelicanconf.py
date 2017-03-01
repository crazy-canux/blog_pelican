#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

################
## Basic setting
################

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
#DOCUTILS_SETTINGS = {}
DELETE_OUTPUT_DIRECTORY = True
#OUTPUT_RETENTION = []
#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#JINJA_FILTERS = {}
#LOG_FILTER = []
READERS = {'html': None,}
#IGNORE_FILES = ['.#*']
#MARKDOWN = {}
OUTPUT_PATH = 'output/'
PATH = 'content/'
#PAGE_PATHS = ['pages']
#PAGE_EXCLUDES = []
#ARTICLE_PATHS = ['']
#ARTICLE_EXCLUDES = []
#OUTPUT_SOURCES = False
#OUTPUT_SOURCES_EXTENSION = '.text'
SITENAME = u"Canux's Blog"
SITEURL = 'http://www.canuxcheng.com'
STATIC_PATHS = ['images', 'extra']
#STATIC_EXCLUDES = []
#STATIC_EXCLUDE_SOURCES = True
#TYPOGRIFY = False
#TYPOGRIFY_IGNORE_TAGS = []
#SUMMARY_MAX_LENGTH = 50
#WITH_FUTURE_DATES = True
#INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
#PYGMENTS_RST_OPTIONS = []
#SLUGIFY_SOURCE = 'title'
#CACHE_CONTENT = False
#CONTENT_CACHING_LAYER = 'reader'
#CACHE_PATH = 'cache'
#GZIP_CACHE = True
#CHECK_MODIFIED_METHOD = 'mtime'
#LOAD_CONTENT_CACHE = False
#WRITE_SELECTED = []
#FORMATTED_FIELDS = ['summary']

################
## URL setting
################

RELATIVE_URLS = True
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
#ARTICLE_LANG_URL = '{slug}-{lang}.html'
#ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
#DRAFT_URL = 'drafts/{slug}.html'
#DRAFT_SAVE_AS = 'drafts/{slug}.html'
#DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
#DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
#PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
#PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
#AUTHOR_URL = 'author/{slug}.html'
#AUTHOR_SAVE_AS = 'author/{slug}.html'
#YEAR_ARCHIVE_SAVE_AS = ''
#MONTH_ARCHIVE_SAVE_AS = ''
#DAY_ARCHIVE_SAVE_AS = ''
#SLUG_SUBSTITUTIONS = ()
#AUTHOR_SUBSTITUTIONS = ()
#CATEGORY_SUBSTITUTIONS = ()
#TAG_SUBSTITUTIONS = ()
#ARCHIVES_SAVE_AS = 'archives.html'
#YEAR_ARCHIVE_SAVE_AS = ''
#MONTH_ARCHIVE_SAVE_AS = ''
#DAY_ARCHIVE_SAVE_AS = ''
#AUTHORS_SAVE_AS = 'authors.html'
CATEGORIES_SAVE_AS = 'category/categories.html'
TAGS_SAVE_AS = 'tag/tags.html'
#INDEX_SAVE_AS = 'index.html'

################
## Time&Date setting
################

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_FORMATS = {'zh_CN': '%Y-%m-%d %H:%M:%S',}
LOCALE = ('en_US.utf8',)

################
## Template setting
################

#TEMPLATE_PAGES = None
#DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
#PAGINATED_DIRECT_TEMPLATES = ['index']
#EXTRA_TEMPLATES_PATHS = []

################
## Metadata setting
################

AUTHOR = u'Canux CHENG'
#DEFAULT_METADATA = {}
FILENAME_METADATA = '(?P<slug>.*)'
#PATH_METADATA = ''
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

################
## Feed setting
################

FEED_DOMAIN = SITEURL

#FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
#TAG_FEED_RSS = None
#RSS_FEED_SUMMARY_ONLY = True

#FEED_ATOM = 'feeds/atom.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
#TAG_FEED_ATOM = None

FEED_MAX_ITEMS = 20

################
## Pagination setting
################

#DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
#PAGINATION_PATTERNS

################
## Translations setting
################

DEFAULT_LANG = u'en'
#TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
#TRANSLATION_FEED_RSS = None

################
## Ordering content setting
################

#NEWEST_FIRST_ARCHIVES = True
#REVERSE_CATEGORY_ORDER = False
#ARTICLE_ORDER_BY = 'reversed-date'
#PAGE_ORDER_BY = 'basename'

################
## Theme setting
################

THEME = 'pelican-theme-canux'
HEADER = 'extra/header.png'
SITEICON = 'extra/siteicon.ico'

#THEME_STATIC_DIR = 'theme'
#THEME_STATIC_PATHS = ['static']
#CSS_FILE = 'main.css'
SITESUBTITLE = 'DevOps & Cloud Computing'
#DISQUS_SITENAME
GITHUB_URL = 'https://github.com/crazy-canux'
#GOOGLE_ANALYTICS
#GA_COOKIE_DOMAIN
#GOSQUARED_SITENAME
#PIWIK_URL
#PIWIK_SSL_URL
#PIWIK_SITE_ID
#TWITTER_USERNAME
#LINKS_WIDGET_NAME
#SOCIAL_WIDGET_NAME

MENUITEMS = (('Category', 'categories.html'),
             ('Tags', 'tags.html'))

LINKS = (('Python', 'https://www.python.org/'),
         ('Django', 'https://www.djangoproject.com/'),
         ('Jinja', 'http://jinja.pocoo.org/'),
         ('OpenJDK', 'http://openjdk.java.net/'))

SOCIAL = (('github', 'https://github.com/crazy-canux'),
          ('linkedin', 'http://www.linkedin.com/profile/preview?locale=zh_CN&trk=prof-0-sb-preview-primary-button'),
          ('stackoverflow', 'http://stackoverflow.com/users/4344009/canux'),
          ('rss', 'http://canuxcheng.com/feeds/all.rss.xml'),
          ('mail', 'mailto:canuxcheng@gmail.com'))

################
## Plugin setting
################

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'feed_summary', 'tag_cloud']

# sitemap
SITEMAP = {
    "format":"xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# feed_summary
FEED_USE_SUMMARY = True

# tag_cloud
TAG_CLOUD_MAX_ITEMS = 50

# i18n_subsites
