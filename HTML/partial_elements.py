'''
This module is to define the partial methods from the HTMLElemnet module,
to use them in the fixture defined in the test cases module
'''

from functools import partial
from html_element import HTMLElemnet

H1 = partial(HTMLElemnet, 'h1')
H2 = partial(HTMLElemnet, 'h2')
H3 = partial(HTMLElemnet, 'h3')
P = partial(HTMLElemnet, 'p')
HTML = partial(HTMLElemnet, 'html')
Head = partial(HTMLElemnet, 'head')
Title = partial(HTMLElemnet, 'title')
Body = partial(HTMLElemnet, 'body')
Div = partial(HTMLElemnet, 'div')
