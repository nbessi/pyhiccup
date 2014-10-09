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
from ..element import (link_to, javascript_with_content, javascipt_include,
                       css_include, image)
from ..core import _convert_tree
from .common import CommonTest


class ElementTest(CommonTest):

    def test_javascript_include(self):
        """Test js inclusion helper"""
        data = javascipt_include("jquery-1.11.1.min.js")
        awaited = '<script src="jquery-1.11.1.min.js" type="text/javascript"/>'
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_javascript_include_remote(self):
        """Test js inclusion helper using remote URL"""
        url = "http://an-url/jquery.mobile.min.css"
        data = javascipt_include(url)
        awaited = ('<script src="http://an-url/jquery.mobile.min.css" type="text/javascript"/>')
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_javascript_include_mutlipe(self):
        """Test js include helper using many URL"""
        url = "http://an-url/jquery.mobile.min.css"
        data = javascipt_include(url, "jquery-1.11.1.min.js")
        awaited = ('<script src="http://an-url/jquery.mobile.min.css" type="text/javascript"/>'
                   '<script src="jquery-1.11.1.min.js" type="text/javascript"/>')
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_javascript_with_content(self):
        """Test javascript with content helper"""
        data = javascript_with_content("alert('Hello, World!')")
        awaited = ("<script type=\"text/javascript\">"
                   "<![CDATA[ alert('Hello, World!') ]]>"
                   "</script>")
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_link_to(self):
        """Test URL helper"""
        data = link_to('http://github.com/~pyhiccup', 'pyhiccup')
        awaited = '<a href="http://github.com/%7Epyhiccup">pyhiccup</a>'
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_css_include_multiple(self):
        """Test CSS helper"""
        data = css_include('http://homer.com/css', 'local.css')
        awaited = ('<link href="http://homer.com/css" type="text/css"/>'
                   '<link href="local.css" type="text/css"/>')

        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_image(self):
        """Test image helper"""
        data = image('http://homer.com/tho.jpg')
        awaited = ('<img src="http://homer.com/tho.jpg"/>')
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_image_with_aprams(self):
        """Test image helper"""
        data = image('http://homer.com/tho.jpg',
                     alt='donut',
                     height='20px',
                     width='10px')
        awaited = ('<img alt="donut" height="20px" '
                   'src="http://homer.com/tho.jpg" '
                   'width="10px"/>')
        conv = ''.join(_convert_tree(data))
        self.assertEquals(awaited, self.normalize_result(conv))
