[![Build Status](https://travis-ci.org/nbessi/pyhiccup.svg?branch=master)](https://travis-ci.org/nbessi/pyhiccup)
[![Coverage Status](https://coveralls.io/repos/nbessi/pyhiccup/badge.png)](https://coveralls.io/r/nbessi/pyhiccup)

pyhiccup pre-alpha
==================

!! Under heavy development do not use in production !!

Python version of https://github.com/weavejester/hiccup


Pyhiccup is a library for representing HTML in Python. It uses list or tuple
to represent elements, and dict to represent an element's attributes.
Supported Python versions are:

 - 2.6
 - 2.7

Other Python 2.x version might also be supported.

Install
-------
TODO

Syntax
------

Here is a basic example of pyhiccup syntax:

```python
>>> from pyhiccup.core import html
>>> data = [
            'html',
            ['div',
             {'class': 'a-class', 'data-y': '23'},
             ['span', 'my-text',
              ['ul', [['li', str(x)] for x in ['coffe', 'milk', 'sugar']]]]],
        ]
>>> html(data)
>>>"<html><div data-y=\"23\" class=\"a-class\"><span>my-text<ul><li>coffe</li><li>milk</li><li>sugar</li></ul></span></div></html>"
```
