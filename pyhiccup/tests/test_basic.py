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
import logging

from ..core import html, xml, _logger
from .common import CommonTest


class HTMLTest(CommonTest):

    def test_comprehension_conversion(self):
        """Test basic HTML and list comprehension"""
        data = [
            [u'div',
             {u'class': 'a-class', 'data-y': '23'},
             [u'span', 'my-text',
              [u'ul', [['li', x] for x in [u'café', u'milk', u'sugar']]]]]
        ]

        awaited = ('<!DOCTYPE html><html dir="rtl" lang="en" xml:lang="en">'
                   '<div class="a-class" data-y="23"><span>my-text'
                   '<ul><li>caf\xe9</li><li>milk</li><li>sugar</li></ul>'
                   '</span></div></html>')
        conv = html(data)
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_html5_doc_type(self):
        """Test HTML 5 DOCTYPE"""
        data = []
        awaited = '<!DOCTYPE html><html dir="rtl" lang="en" xml:lang="en"/>'
        conv = html(data, etype='html5')
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_html4_doc_type(self):
        """Test HTML 4 DOCTYPE"""
        data = []
        awaited = ('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                   '"http://www.w3.org/TR/html4/strict.dtd"><html dir="rtl" lang="en"'
                   ' xml:lang="en"/>')
        conv = html(data, etype='html4')
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_xhtml_strict_doc_type(self):
        """Test XHTML strict DOCTYPE"""
        data = []
        awaited = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
                   '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
                   '<html dir="rtl" lang="en" xml:lang="en" '
                   'xmlns="http://www.w3.org/1999/xhtml"/>')
        conv = html(data, etype='xhtml-strict')
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_xhtml_transitional_doc_type(self):
        """Test XHTML transitional DOCTYPE"""
        data = []
        awaited = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML '
                   '1.0 Transitional//EN" '
                   '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
                   '<html dir="rtl" lang="en" xml:lang="en" '
                   'xmlns="http://www.w3.org/1999/xhtml"/>')
        conv = html(data, etype='xhtml-transitional')
        self.assertEquals(awaited, self.normalize_result(conv))

    def test_wrong_type(self):
        data = []
        self.assertRaises(ValueError, html, data, 'kaboom')

    def test_debug_logging(self):
        """Ensure that debug logging will not break"""
        current_level = _logger.getEffectiveLevel()
        _logger.setLevel(logging.DEBUG)
        html([])
        _logger.setLevel(current_level)


class XMLTest(CommonTest):

    def test_minimal_xml(self):
        """Test minimal XML"""
        data = ['form-desc',
                ['field', {'name': 'a_name'}],
                ['field', {'name': 'a_other_name'}]]
        conv = xml(data, 'foo-ns', bar='an_attr')
        awaited = ('<?xml version="1.0" encoding="UTF-8"?>'
                   '<foo-ns bar="an_attr"><form-desc><field name="a_name"/>'
                   '<field name="a_other_name"/></form-desc></foo-ns>')
        self.assertEquals(awaited, self.normalize_result(conv))
