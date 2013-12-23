#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
from datetime import date

# General Settings
SITEURL = u'http://www.darrelclute.net:8000'
SITENAME = u'Darrel Clute'
FEEDURL = SITEURL
AUTHOR = u'Darrel Clute'
TAGLINE = u'Ramblings from yet another IT Professional'
TIMEZONE = u'America/Denver'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = u'%A, %B %d, %Y'
COPYDATE = 2005
CURDATE = date.today().year
DIRECT_TEMPLATES = (u'index', u'archives', u'categories')
ARTICLE_URL = u'{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = u'{date:%Y}/{date:%m}/{slug}.html'
MONTH_ARCHIVE_SAVE_AS = u'{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = u'{date:%Y}/index.html'
TAG_URL = None
TAG_SAVE_AS = None
TAGS_URL = None
TAGS_SAVE_AS = None
AUTHOR_URL = None
AUTHOR_SAVE_AS = None
AUTHORS_URL = None
AUTHORS_SAVE_AS = None
ARCHIVES_SAVE_AS = u'archive.html'
SUMMARY_MAX_LENGTH = None
ARTICLE_EXCLUDES = ('pages', 'drafts')
THEME_STATIC_DIR = ''

# Feed Settings
FEED_ALL_ATOM = u'feeds/posts.xml'
CATEGORY_FEED_ATOM = u'feeds/%s.xml'
TRANSLATION_FEED_ATOM = None

# Social Links
GITHUB_USERNAME = u'darrelclute'
GITHUB_URL = u'https://github.com/darrelclute'
GITORIOUS_USERNAME = u'darrelclute'
TWITTER_USERNAME = u'darrelclute'
LINKEDIN_USERNAME = u'darrelclute'
GOOGLE_PLUS_USERNAME = u'DarrelClute'

# Presentation
THEME = u'dcnet-theme'
DEFAULT_PAGINATION = 5
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
HIDE_CATEGORIES_FROM_MENU = False
DEFAULT_METADATA = (('location', 'Elizabeth CO'),)
USER_LOGO_URL = u'http://www.gravatar.com/avatar/2c83f7fbc77af26448eb5da73997515c.png'

DELETE_OUTPUT_DIRECTORY = True
DISQUS_SITENAME = "darrelclute"
#GOOGLE_ANALYTICS = ""

AUTHOR_SUMMARY = "Darrel is an IT Infrastructure Architect focusing on Network and UNIX Systems Engineering.  The majority of Darrel's career has focused on Cisco for networking and numerous Linux distributions for systems, but has varied expertise outside of these technologies."
