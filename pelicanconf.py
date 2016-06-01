#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Yergler'
SITENAME = u'Read Ya!'
SITEDOMAIN = ''
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DEFAULT_DATE_FORMAT = "%A, %B %-d, %Y"

DIRECT_TEMPLATES = (
    'tags',
    'categories',
    'archives',
)

DEFAULT_CATEGORY = 'letters'

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TEMPLATE_PAGES = {
    'signup.html': 'index.html',
    'CNAME': 'CNAME',
}

THEME = 'themes/readya'

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'markdown.extensions.smarty',
]
