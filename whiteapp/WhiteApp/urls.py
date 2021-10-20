# -*- coding: utf-8 -*-
# ================================================= Import des packages ================================================
from django.urls import path

from . import views

# ============================= Definition des variables ===============================================================
app_name = 'WhiteApp'
urlpatterns = [
    path('Accueil', views.Accueil.as_view(), name="Accueil"),
    path('AccueilVue', views.AccueilVue.as_view(), name="AccueilVue")
]
