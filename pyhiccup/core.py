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
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU General Public License 3
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Mutual recursive parser

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
    output.insert(0, " ")
    return ' '.join(output)


def self_closing(btype):
    """Predicate that determine if tag is self closing

    :param btype: name of tag eg. `div`
    :type btype: str, unicode

    :return: True if tag is self closing else False
    :rtype: bool

    """
    return False


def convert_tree(*args):
    """Transform a list describing HTML/XML to raw HTML/XML list

    It is uses a mutual recursion to walk tree and transform

    :param args: list of list describing HTML
    :type args: list, tuple

    :return: a list of string
    :rtype: list

    """
    accu = []
    for x in args:
        if isinstance(x, TREE_TYPE):
            if isinstance(x[0], TREE_TYPE):
                accu.extend(convert_tree(*x))
            else:
                accu.extend(convert_leaf(*x))
        else:
            accu.extend(convert_leaf(*x))
    return accu


def convert_leaf(*args):
    """Transform a list describing HTML/XML leaf raw HTML/XML lsit

    It is uses a mutual recursion to walk tree and transform leaf

    :param args: leaf list describing HTML
    :type args: list, tuple

    :return: a list of string
    :rtype: list

    """
    accu = ["<"]
    btype = args[0]
    accu.append(btype)
    rest = args[1:]
    inner_trees = []
    inner_element = None
    for element in rest:
        if isinstance(element, TREE_TYPE):
            inner_trees.append(element)
        elif isinstance(element, dict):
            accu.append(format_attributes(element))
        else:
            inner_element = element
    if self_closing(btype):
        accu.append("/>")
        if inner_trees or inner_element:
            raise ValueError('%s can not have inner values' % btype)
    else:
        accu.append(">")
        if inner_element:
            accu.append(inner_element)
        if inner_trees:
            accu.extend(convert_tree(*inner_trees))
        accu.append("</%s>\n" % btype)
    return accu


def html(value):
    """Transform a list describing HTML/XML to raw HTML/XML

    :param args: list of list describing HTML
    :type args: list, tuple

    :return: HTML/XML string representation
    :rtype: str, unicode

    """
    res = convert_tree(value)
    return ''.join(res)
