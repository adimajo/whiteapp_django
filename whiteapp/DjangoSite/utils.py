"""
Common utility functions
"""
# -*- coding: utf-8 -*-
# ================================================= Import des packages ================================================
# Calculs
import os

# Homemade packages
from loguru import logger


# ================================================= Macro init ================================================
# Gestion des exports Excel
def layout_to_fieldset(layout):
    fieldset = []
    idx = 0
    for k, v in layout.items():
        idx += 1
        if idx == 1:
            fieldset.append((k, {"fields": tuple(v)}))
            continue
        fieldset.append((k, {"classes": ("collapse", "open"),
                             "fields": tuple(v)}))
    return tuple(fieldset)


def arg_is_yes(x):
    return x in [True, "true", "True", "oui", "O", "Oui", "Yes", "OUI", "y", "Y", "yes"]


def create_dir(path):
    """
    Fonction used to safely create a directory
    :param path: path of the directory
    :type path: str
    :return: path
    :rtype: str
    """
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            logger.error(e)
        return path
