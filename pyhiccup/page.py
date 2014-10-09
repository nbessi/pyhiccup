# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License 3
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from __future__ import unicode_literals

DOC_TYPES = {
    'html4': "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\" "
             "\"http://www.w3.org/TR/html4/strict.dtd\">\n",

    'xhtml-strict': "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 ""Strict//EN\" "
                    "\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n",

    'xhtml-transitional': "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" "
                          "\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n",

    'html5': "<!DOCTYPE html>\n",
}

DEFAULT_XMLNS = 'http://www.w3.org/1999/xhtml'
XMl_DECLARATION = '<?xml version="1.0" encoding="UTF-8"?>'


def get_doc_type(doc_type):
    """Return a DOCTYPE declaration

    :param doc_type: doc type string must be in ``page.DOC_TYPES``
    :type doc_type: str
    :return: DOCTYPE declaration
    :rtype: str

    """
    if doc_type not in DOC_TYPES:
        raise ValueError(
            'Invalid DOCTYPE %s available values are %s' %
            (doc_type, DOC_TYPES.keys())
        )
    return DOC_TYPES[doc_type]


def get_html_enclosing_tag(etype, **kwargs):
    """Generate html tag list representation

    :param etype: html doc type `html5, html4, xhtml-strict,
                  xhtml-transitional`
    :type etype: str
    :param kwargs: dict of attribute for HTML tag will override defaults
    :type kwargs: dict

    :return: html tag list representation ['html', {'xmlns': ...}]
    :rtype: dict
    """
    attrs = {}
    if etype in DOC_TYPES:
        attrs['lang'] = 'en'
        attrs['dir'] = 'rtl'
        attrs['xml:lang'] = 'en'
    if 'xhtml' in etype:
        attrs[u'xmlns'] = DEFAULT_XMLNS
    attrs.update(kwargs)
    return ['html', attrs]


def get_xml_enclosing_tag(etype, **kwargs):
    """Generate XML root tag list representation

    :param etype: root tag name
    :type etype: str
    :param kwargs: dict of attribute for root tag
    :type kwargs: dict

    :return: root xml tag list representation ['atag', {'attr': ...}]
    :rtype: dict
    """
    return [etype, kwargs]
