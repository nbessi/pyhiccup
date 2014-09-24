import re
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from ..core import html

CLEAN_REGEX = re.compile('[\t\r\n]')


class basic_html(unittest.TestCase):

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

    def test_minimal_conversion(self):
        data = data = [
            'html',
            ['div',
             {'class': 'a-class', 'data-y': '23'},
             ['span', 'my-text',
              ['ul', [['li', str(x)] for x in ['coffe', 'milk', 'sugar']]]]],
        ]

        awaited = ('<html><div  data-y=\"23\" class=\"a-class\">'
                   '<span>my-text<ul><li>coffe</li><li>milk</li>'
                   '<li>sugar</li></ul></span></div></html>')
        conv = html(data)
        self.assertEquals(awaited, self.normalize_result(conv))
