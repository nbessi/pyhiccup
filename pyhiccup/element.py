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
import sys

if sys.version_info < (3, 0): # pragma: no cover
    from urllib import quote
else: # pragma: no cover
    from urllib.parse import quote


def _protect_url(url):
    splited_url = url.split('://', 1)
    if len(splited_url) == 1:
        return quote(url)
    else:
        return "%s://%s" % (splited_url[0], quote(splited_url[1]))


def javascipt_include(*args):
    """Generate elements to include js script

    It generates many `script` tags `<script type.../>

    :param args: sources URLs of script to be included
    :type args: list

    :return: a list representing script tag with URL
    :rtype: list
    """
    tag_list = []
    # we can yield but it is harder to debugg
    for js_url in args:
        tag_list.append(
            ['script',
             {'type': 'text/javascript',
              'src': _protect_url(js_url)}]
        )
    return tag_list


def javascript_with_content(script):
    """Generate element to insert js script

    It generates a `script` tag `<script type...><![CDATA[script]]></script>`

    :param script: script to be interted
    :type script: str

    :return: a list representing script tag with content
    :rtype: list
    """
    tag_list = ['script',
                {'type': 'text/javascript'},
                "<![CDATA[\n %s \n]]>" % script]
    return tag_list


def css_include(*args):
    """Generate elements to include js script

    It generates many `link` tags `<link type="text/css".../>

    :param args:  sources URLs of script to be included
    :type args: list

    :return: a list representing script tag with URL
    :rtype: list
    """
    tag_list = []
    # we can yield but it is harder to debugg
    for css_url in args:
        tag_list.append(
            ['link',
             {'type': 'text/css',
              'href': _protect_url(css_url)}]
        )
    return tag_list


def link_to(url, content):
    """Generate an URL element
    It generates a `a` tag with content `<a href="url">content</a>`

    :param url: destination URL
    :type url: str

    :return: a list representing `a` link tag
    :rtype: list
    """
    tag_list = ['a',
                {'href': _protect_url(url)},
                content]
    return tag_list


def image(source_url, alt=None, height=None, width=None):
    """Generate an image element
    It generates a `image` from URL <img src="url" alt=.../>

    :param url: image source URL
    :type url: str

    :param alt: alternate text
    :type alt: str

    :param height: height of image
    :param height: str or numeric

    :param width: width of image
    :param width: str or numeric

    :return: a list representing an `img` tag
    :rtype: list
    """
    attrs = {'src': _protect_url(source_url)}
    if alt:
        attrs['alt'] = alt
    if height:
        attrs['height'] = height
    if width:
        attrs['width'] = width
    tag_list = ['img', attrs]
    return tag_list
