#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
from datetime import date

# Plugin settings, do not alter path without altering build script
# PLUGIN_PATHS = ['~/repos/pelican-plugins']
# Uncomment the following line to enable plugins, add or subtract as desired
# PLUGINS = ['series', 'interlinks', 'summary', 'neighbors']

# General Settings
SITEURL = u'https://www.darrelclute.net'
SITENAME = u'Darrel Clute'
FEEDURL = None
AUTHOR = u'Darrel Clute'
TAGLINE = u''
TIMEZONE = u'America/Detroit'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = u'%A, %B %d, %Y'
COPYDATE = 2005
CURDATE = date.today().year
DIRECT_TEMPLATES = (u'index', u'archives', u'categories')
ARTICLE_URL = None
ARTICLE_SAVE_AS = None
MONTH_ARCHIVE_SAVE_AS = None
YEAR_ARCHIVE_SAVE_AS = None
TAG_URL = ''
TAG_SAVE_AS = ''
TAGS_URL = ''
TAGS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
CATEGORY_URL = None
CATEGORY_SAVE_AS = None
ARCHIVES_SAVE_AS = None
CATEGORIES_SAVE_AS = None
SUMMARY_MAX_LENGTH = None
ARTICLE_EXCLUDES = ('pages', 'drafts', 'static')
THEME_STATIC_DIR = ''

STATIC_PATHS = [
    'static/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Feed Settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
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
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_CATEGORIES_FROM_MENU = False
DEFAULT_METADATA = (('location', 'Homer MI'),)
USER_LOGO_URL = u'https://www.gravatar.com/avatar/2c83f7fbc77af26448eb5da73997515c.png'

DELETE_OUTPUT_DIRECTORY = False

AUTHOR_SUMMARY = "Darrel is an IT Infrastructure Architect focusing on Network and UNIX Systems Engineering.  The majority of Darrel's career has focused on Cisco for networking and numerous Linux distributions for systems, but has varied expertise outside of these technologies."
