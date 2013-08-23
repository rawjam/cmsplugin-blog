from django.utils.translation import get_language, ugettext_lazy as _
from django.conf import settings

def module_exists(str):
    try:
        __import__(str)
    except ImportError:
        return False
    return True

def is_multilingual():
    return 'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware' in settings.MIDDLEWARE_CLASSES

def get_lang_name(lang):
    return _(dict(settings.LANGUAGES)[lang])

def add_current_root(url):
    #if is_multilingual() and not has_lang_prefix(url):
    if is_multilingual() and module_exists('cms.middleware.multilingual') and not has_lang_prefix(url):
        from cms.middleware.multilingual import has_lang_prefix
        new_root = "/%s" % get_language()
        url = new_root + url
    return url