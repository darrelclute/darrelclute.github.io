#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
from datetime import date

# Plugin settings, do not alter path without altering build script
PLUGIN_PATHS = ['../../pelican-plugins']
# Uncomment the following line to enable plugins, add or subtract as desired
PLUGINS = [
    'series',
    'interlinks',
    'summary',
    'neighbors',
    'gravatar',
    'readtime',
    'sitemap',
    'footer_insert',
]

# General Settings
SITEURL = u'//localhost:8080'
SITENAME = u'Darrel Clute'
FEEDURL = SITEURL
AUTHOR = u'Darrel Clute'
AUTHOR_EMAIL = 'darrel@darrelclute.net'
SITESUBTITLE = u'Ramblings from yet another IT Professional'
TIMEZONE = u'America/Detroit'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = u'%A, %B %d, %Y'
COPYDATE = 2005
CURDATE = date.today().year
DIRECT_TEMPLATES = (u'index', u'archives', u'categories')
ARTICLE_URL = u'{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = u'{date:%Y}/{date:%m}/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = u'{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = u'{date:%Y}/index.html'
TAG_URL = ''
TAG_SAVE_AS = ''
TAGS_URL = ''
TAGS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
CATEGORY_URL = u'category/{slug}/'
CATEGORY_SAVE_AS = u'category/{slug}/index.html'
ARCHIVES_SAVE_AS = u'archives/index.html'
CATEGORIES_SAVE_AS = u'category/index.html'
SUMMARY_USE_FIRST_PARAGRAPH = True
ARTICLE_EXCLUDES = ('pages', 'drafts', 'static')
THEME = '../dcnet-green-penguin'
THEME_STATIC_DIR = ''

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'),
)

STATIC_PATHS = [
    'static/resume.pdf',
    'static/pgp-key.txt',
    'static/pgp-transition-statement.txt',
    'static/robots.txt',
    'static/keybase.txt',
    'static/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'static/resume.pdf': {'path': 'pdf/darrelclute3-resume.pdf'},
    'static/pgp-key.txt': {'path': 'pgp-key.txt'},
    'static/pgp-transition-statement.txt': {'path': 'pgp-transition-statement.txt'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/keybase.txt': {'path': 'keybase.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}

SITEMAP = {
    'format': 'xml',
}

# Feed Settings
FEED_ALL_ATOM = u'feeds/index.xml'
CATEGORY_FEED_ATOM = u'feeds/%s/index.xml'
TRANSLATION_FEED_ATOM = None

# Social Links
GITHUB_USERNAME = u'darrelclute'
GITHUB_URL = u'https://github.com/darrelclute'
GITORIOUS_USERNAME = u'darrelclute'
TWITTER_USERNAME = u'darrelclute'
LINKEDIN_USERNAME = u'darrelclute'
GOOGLE_PLUS_USERNAME = u'DarrelClute'

# Presentation
DEFAULT_PAGINATION = 5
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
HIDE_CATEGORIES_FROM_MENU = False
DEFAULT_METADATA = (('location', 'Homer MI'),)
USER_LOGO_URL = u'https://www.gravatar.com/avatar/2c83f7fbc77af26448eb5da73997515c.png'

DELETE_OUTPUT_DIRECTORY = False

AUTHOR_SUMMARY = 'I am an IT Infrastructure Architect, with a focus on bridging business needs together with data center usage. I bring a cross functional focus on Network, Security, Virtulization, and UNIX Systems Engineering, trying to bridge the gaps between the disciplines. I am a strong proponent of automation and orchestration, with a focus on using the same toolsets across disciplines. I also advocate for Open Source software use in the enterprise as well as for by individuals.'

INTERLINKS = {
    'dcnet': 'https://www.darrelclute.net/'
}
