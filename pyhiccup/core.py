# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
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
import logging
from itertools import chain

from .page import DOC_TYPES

_logger = logging.getLogger('pyhiccup.convert')

TREE_TYPE = (list, tuple)


def format_attributes(attributes):
    """Transform dict to XMl/HTMl attributes

    {'class': 'a-class', 'data-sel': 'a-sel'}
    returns ``class="a-class" data-sel="a-sel"``

    :param attributes: dict of XML/HMTL attributes to transform
                       to string
    :type attributes: dict

    :return: a list of attributes eg. ``class="a-class" data-sel="a-sel"``
    :rtype: basestring

    """
    output = []
    for item in attributes.items():
        output.append('%s=\"%s\"' % item)
    return " %s" % ' '.join(output)


def self_closing(btype):
    """Predicate that determine if tag is self closing

    :param btype: name of tag eg. `div`
    :type btype: str, unicode

    :return: True if tag is self closing else False
    :rtype: bool

    """
    return False


def convert_tree(node):
    """Transform a list describing HTML leaf to a list of HTML string

    ready to be joined

    :param args: leaf list describing HTML
    :type args: list, tuple

    :return: a list of string
    :rtype: list

    """
    btype = node[0]
    rest = node[1:]
    attrs = ''
    inner_trees = []
    inner_element = ''
    for element in rest:
        if isinstance(element, TREE_TYPE):
            if isinstance(element[0], TREE_TYPE):
                inner_trees.extend(element)
            else:
                inner_trees.append(element)
        elif isinstance(element, dict):
            attrs = format_attributes(element)
        else:
            inner_element = element
    if self_closing(btype):
        if inner_trees or inner_element:
            raise ValueError('%s can not have inner values' % btype)
        yield '<%s/>' % btype
    else:
        yield '<%s%s>' % (
            btype,
            attrs,
        )
        if inner_element:
            yield inner_element
        if inner_trees:
            for ext in inner_trees:
                for x in convert_tree(ext):
                    yield x
        yield '</%s>' % btype


def html5(value):
    """Transform a list describing HTML/XML to raw HTML/XML

    :param args: list of list describing HTML
    :type args: list, tuple

    :return: HTML string representation
    :rtype: str, unicode

    """
    value = ['html', value]
    converted = chain(
        [DOC_TYPES['html5']],
        convert_tree(value)
    )
    _logger.debug(
        list(chain([DOC_TYPES['html5']],
                   convert_tree(value)))
    )
    return ''.join(converted)
