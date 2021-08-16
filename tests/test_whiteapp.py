import sys
import django
import os
sys.path.append("whiteapp")

if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'whiteapp.DjangoSite.settings'


def test_whiteapp():
    django.setup()
    from whiteapp.WhiteApp import urls, utils
    from whiteapp import manage
    from whiteapp.DjangoSite import Singleton, urls, wsgi
