from pathlib import Path
import json

SITENAME = 'IEEE SaTML 2026'
SITEURL = "https://dev.satml.org/"

CONFERENCE_NAME = "4th IEEE Conference on Secure and Trustworthy Machine Learning"
CONFERENCE_LOCATION = "Technical University of Munich, Germany"
CONFERENCE_DATE = "March 23–25, 2026"

CHAIRS = json.loads(Path('data/chairs.json').read_text())
STEERING_COMMITTEE = json.loads(Path('data/steering.json').read_text())
PROGRAM_COMMITTEE = json.loads(Path('data/pc.json').read_text())

PAST_EDITIONS = json.loads(Path('data/past-editions.json').read_text())

PAPERS = json.loads(Path('data/papers.json').read_text())

SOCIAL = {
    "mail" : "contact@satml.org",
    "bluesky" : "https://bsky.app/profile/satml.org",
}

PATH = "content"
THEME = 'theme'

TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE = 'fs'

DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['', 'hidden']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

THEME_STATIC_DIR = ''

INDEX_SAVE_AS = ''

# Disable everything blog related
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATH = ['articles']

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
