pyhiccup pre-alpha
==================

!! Under heavy development do not use in production !!

Python version of https://github.com/weavejester/hiccup


Pyhiccup is a library for representing HTML in python. It uses list or tuple
to represent elements, and dict to represent an element's attributes.

Install
-------

TODO

Syntax
------

Here is a basic example of Hiccup syntax:

```python
>>> from pyhiccup.core import html
>>> data = ['html',
             ['div',
              {'class': 'a_class', 'data-y': 23},
              ['span',
               'blabla',
               ['ul',
                [['li', str(x)] for x in xrange(20)]]]],
             ['ul',
              [['li', str(x)] for x in xrange(20)]]]
>>> html(data)
>>>"<html><div  data-y=\"23\" class=\"a_class\"><span>blabla<ul><li>0</li>
<li>1</li>
<li>2</li>
<li>3</li>
<li>4</li>
<li>5</li>
<li>6</li>
<li>7</li>
<li>8</li>
<li>9</li>
<li>10</li>
<li>11</li>
<li>12</li>
<li>13</li>
<li>14</li>
<li>15</li>
<li>16</li>
<li>17</li>
<li>18</li>
<li>19</li>
</ul>
</span>
</div>
<ul><li>0</li>
<li>1</li>
<li>2</li>
<li>3</li>
<li>4</li>
<li>5</li>
<li>6</li>
<li>7</li>
<li>8</li>
<li>9</li>
<li>10</li>
<li>11</li>
<li>12</li>
<li>13</li>
<li>14</li>
<li>15</li>
<li>16</li>
<li>17</li>
<li>18</li>
<li>19</li>
</ul>
</html>"
```
