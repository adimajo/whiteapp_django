"""
admin tools for Django app
"""
# -*- coding: utf-8 -*-
# ============================ Import statements============================================
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from DjangoSite.utils import layout_to_fieldset
from WhiteApp.models import WhiteApp, WhiteAppForm

classAdmin = ImportExportModelAdmin


class WhiteAppResource(resources.ModelResource):
    class Meta:
        model = WhiteApp


@admin.register(WhiteApp)
class WhiteAppAdmin(classAdmin):
    fieldsets = layout_to_fieldset(WhiteApp.layout)
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('uri', "nom_projet")
    list_filter = ["nom_projet"]
    sortable_by = ["nom_projet"]
    form = WhiteAppForm
    resource_class = WhiteAppResource
