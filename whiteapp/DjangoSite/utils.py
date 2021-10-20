"""
Common utility functions
"""


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
