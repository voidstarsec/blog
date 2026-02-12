AUTHOR = 'VoidStar Security'
SITENAME = 'VoidStar Security Blog'
SITEURL = 'https://voidstarsec.com/blog/'
PLUGIN_PATHS = ['/home/wrongbaud/projects/vss/blog-resources/pelican-plugins']
PLUGINS = ['i18n_subsites','pelican_just_table','tag_cloud']
JINJA_ENVIRONMENT = {
            'extensions': ['jinja2.ext.i18n'],
            }

PATH = 'content'
TIMEZONE = 'America/Boise'
DEFAULT_LANG = 'en'
TAG_CLOUD_MAX_ITEMS=10
SIDEBAR_ON_LEFT=True
ARTICLE_URL='{slug}'
# Blogroll
LINKS = (('VoidStar Security Website', 'https://voidstarsec.com/'),
         ('VoidStar Security Training', 'https://www.voidstarsec.training/'),
        ('Build a Hardware Hacking Lab', 'https://www.voidstarsec.wiki/'),
         ('Free Ghidra Course', 'https://hackaday.io/course/172292-introduction-to-reverse-engineering-with-ghidra'),
         ('Wrongbauds Blog (fun intro hacks)', 'https://www.wrongbaud.github.io/'),)

# Social widget
SOCIAL = ( ('VSS website','https://voidstarsec.com'),
          ('twitter', 'https://twitter.com/voidstarsec'),
          ('linkedin', 'https://www.linkedin.com/in/voidstarsec'),
          ('github', 'https://github.com/voidstarsec'),)

#SITELOGO = './logo.png'
#SITELOGO_SIZE=70
DISPLAY_BREADCRUMBS=True
DEFAULT_PAGINATION=10
DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_CATEGORIES_ON_SIDEBAR=True
DISPLAY_ARTICLE_INFO_ON_INDEX=True
SHOW_ARTICLE_AUTHOR=True
SHOW_ARTICLE_CATEGORY=True
# journal lumen spacelab
BOOTSTRAP_THEME='flatly'