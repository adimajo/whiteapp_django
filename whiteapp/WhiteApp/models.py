"""
Django models
"""
# -*- coding: utf-8 -*-
# ================================================= Import des packages ================================================
# Gestion des données
from uuid import uuid4

from django import forms
# Package Django
from django.db import models
from django.forms import ModelForm

# ============================= Definition des variables ===============================================================

creation_date_name = "Creation date"
updated_at_name = "Last update"


# ============================= Definition des fonctions ===============================================================
def _generate_unique_uri():
    return str(uuid4()).replace("-", "")[:15]


def upper_firt_letter(word):
    try:
        return " ".join([x[:1].upper() + x[1:].lower() for x in word.split(" ")])
    except AttributeError:
        return word


def clean_siren(siren: str):
    try:
        siren = int(siren)
    except ValueError:
        siren = ""
    return ("0" * 9 + str(siren))[-9:]


def arg_is_yes(x):
    return x in ["True", True, "true", 1, "Oui", "oui", "O", "y", "YES", "yes", "Yes"]


# ============================= Definition des classes =================================================================
class DateInput(forms.DateInput):
    input_type = 'date'


class WhiteApp(models.Model):
    created_at = models.DateTimeField(creation_date_name, auto_now_add=True)
    updated_at = models.DateTimeField(updated_at_name, auto_now=True)
    uri = models.CharField(default=_generate_unique_uri, max_length=15, primary_key=True)
    nom_projet = models.CharField("Nom du projet", max_length=200)

    layout = {"Informations générales": ["nom_projet"]}

    @property
    def nb_notations(self):
        return self.evts.all().count()

    def to_dict(self, with_comments=False, with_events=False, **kwargs):
        """
        Turns itself into a dict (easily readable)
        :return:
        :rtype: dict
        """
        result = {v: self.__getattribute__(v) for k, variables in self.layout.items() for v in variables
                  if v not in ["promoteur"]}
        if with_comments:
            result["comments"] = [commentaire.to_dict() for commentaire in self.comments.all()]
        if with_events:
            result["evts"] = [evt.to_Accueil_view() for evt in self.evts.all()]
        result.update({"uri": self.uri,
                       "nb_notations": self.nb_notations,
                       "promoteur__uri": self.promoteur.uri, "statut": self.statut,
                       "promoteur__nom_promoteur": self.promoteur.nom_promoteur})

        result.update(kwargs)
        return result

    def to_Accueil_view(self, **kwargs):
        """
        Fonction utilisée pour exporter les données relatives à un projet (utilisée par les views)
        :return:
        :rtype: dict
        """
        result = self.to_dict(with_events=True, with_comments=True, **kwargs)
        return result

    def __str__(self):
        return "{} - ({})".format(self.nom_projet, self.uri)

    def save(self, addok=True, *args, **kwargs):
        self.nom_projet = upper_firt_letter(self.nom_projet)
        super(WhiteApp, self).save(*args, **kwargs)


class WhiteAppForm(ModelForm):
    class Meta:
        model = WhiteApp
        exclude = ["created_at", "updated_at"]

    layout = WhiteApp.layout
