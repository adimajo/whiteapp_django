import sys
import django
import os
sys.path.append("whiteapp")

if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'whiteapp.DjangoSite.settings'


def test_whiteapp():
    django.setup()
    from whiteapp.WhiteApp import apps, urls, views
    from whiteapp.WhiteApp.management.commands import ensure_superuser
    from whiteapp import manage
    from whiteapp.DjangoSite import Singleton, urls, wsgi

    class Handler(metaclass=Singleton.Singleton):
        pass

    toto = Handler()
    tata = Handler()


def test_whiteapp_test_db():
    os.environ['TEST_DB'] = "True"
    django.setup()
    from whiteapp.WhiteApp import apps, urls, views
    from whiteapp.WhiteApp.management.commands import ensure_superuser
    from whiteapp import manage


def test_layout():
    from whiteapp.DjangoSite.utils import layout_to_fieldset
    layout_to_fieldset({'toto': [1, 2, 3],
                        'tata': [1, 2, 3],
                        'tutu': [1, 2, 3]})


def test_django():

    from django.test import TestCase
    import sys
    sys.path.append("whiteapp")
    from WhiteApp.models import WhiteApp

    django.setup()

    class WhiteAppTestCase(TestCase):
        def setUp(self):
            WhiteApp.objects.create(nom_projet="lion")
            lion = WhiteApp.objects.get(nom_projet="lion")
            assert lion.exemple_propriete == "lion"
            lion.to_dict()
            lion.to_Accueil_view()
