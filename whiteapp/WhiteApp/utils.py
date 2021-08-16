"""
Common utility functions
"""
import base64
import io
import urllib


# ======================================================================================================================
def diff_month(d1, d2):
    d1, d2 = min(d1, d2), max(d1, d2)
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def apply_filter(df, row_filter, name_filter=None):
    string_separator = "#==========================================================================="

    avt = len(df)
    result = df[row_filter]
    apr = len(result)
    msg = "{}\nApply filter: {}\n\tTaille avant : {}\n\tTaille apres : {}\n\tdelta : {}".format(string_separator,
                                                                                                name_filter,
                                                                                                avt,
                                                                                                apr,
                                                                                                abs(avt - apr))
    print(msg)
    return result


def to_html_string(fig):
    """
    convertit une figure en un texte compatible HTML

    :param fig: Figure a transformer
    :type fig: figure (matplotlib)

    :rtype: string
    """
    imgdata = io.BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)
    return "data:image/png;base64," + urllib.parse.quote(base64.b64encode(imgdata.getbuffer()))
