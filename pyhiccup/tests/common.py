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
import re

try:
    import unittest2 as unittest
except ImportError:
    import unittest

CLEAN_REGEX = re.compile('[\t\r\n]')


class CommonTest(unittest.TestCase):

    def normalize_result(self, raw_string):
        """Remove tab, carriage and space around balise

        :param raw_string: HTML/XML to clean
        :type raw_string: basestring

        :return: normalized string
        :rtype: str

        """
        return CLEAN_REGEX.sub('', raw_string)

    def test_normalize_result(self):
        """Test normalize helper"""
        raw = u"Hello\t \nWorld"
        clean = self.normalize_result(raw)
        self.assertEqual(clean, u"Hello World")
