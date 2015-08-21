#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Florian Gesser'
SITENAME = u'GSoC Blog C-PAC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

MARKUP = ('md', 'ipynb')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('C-PAC Configurable Pipeline for the Analysis of Connectomes', 'http://fcp-indi.github.io/'),)

# Social widget
SOCIAL =(('twitter', 'http://twitter.com/flrgsr'),
         ('github', 'http://github.com/flrgsr'),)		

(('You can add links in your config file', '#'),
          ('Another social link', '#'),)

TWITTER_USERNAME = "flrgsr"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['liquid_tags.notebook', 'pelican-ipynb']

# For iPython Notebook
# EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')


#THEME = "pelican-themes/built-texts"
THEME = "pelican-themes/flex"

# SITEURL = "http://fgesser.io"
DISQUS_SITENAME = "fgesserio"