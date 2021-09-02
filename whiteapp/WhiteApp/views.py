# -*- coding: utf-8 -*-
# ================================================= Import des packages ================================================
import codecs
import os
import re
import sys

import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from pip._internal.operations.freeze import freeze
from markupsafe import Markup
from logger_mig import MyPrinter


logger = MyPrinter()

# ============================= Definition des classes  ================================================================
class Accueil(TemplateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    template_name = "Accueil.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class AccueilVue(TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        logger.info("POST : IN : request : {}".format(request))

        result = {"messages": []}

        request_dict = request.POST.dict()

        if "init" in request_dict:
            result['user'] = None

        with codecs.open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__init__.py"), 'r') as fp:
            version_file = fp.read()

        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        cell = {  # for row hover use <tr> instead of <td>
            'selector': 'td',
            'props': [('background-color', '#ffffb3'),
                      ('color', 'black')]
        }
        cell_hover = {  # for row hover use <tr> instead of <td>
            'selector': 'td:hover',
            'props': [('background-color', '#ffffb3'),
                      ('color', 'red')]
        }
        index_names = {
            'selector': '.index_name',
            'props': 'font-style: italic; color: darkgrey; font-weight:normal;'
        }
        headers = {
            'selector': 'th:not(.index_name)',
            'props': 'background-color: #000066; color: white;'
        }

        result['python_version'] = sys.version
        if version_match:
            result['package_version'] = version_match.group(1)
        else:
            "Unknown"
        result['requirements'] = Markup(pd.DataFrame(list(
            map(lambda x: x.split('=='), freeze(local_only=True))
        ), columns=['package', 'version']).style.set_table_styles([cell, cell_hover, index_names, headers]).hide_index().to_html())

        result["messages"].append({
            "msg": "Succès",
            "type": "alert-success"})

        logger.info("POST : OUT : request : {}".format(result))

        return JsonResponse(result, status=202)
