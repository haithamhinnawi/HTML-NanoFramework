"""
This module is to make a test cases for the main module,
checks the functionality if it works fine or not using pytest
"""

import pytest
from partial_elements import Div, HTML, Head, Body, P, Title
from html_element import HTMLElemnet
import pydoc

@pytest.fixture
def html_element():
    """
    This is a fixture to define the element tree that will be used in most of the tests
    """
    title = Title('My Website', {'id': 'container'})
    head = Head(title)
    p1 = P('This is a paragraph')
    p2 = P('Paragraph', {'id': 'unique-id'})
    div = Div([p1, p2], {'id': 'Container'})
    body = Body(div)
    html = HTML([head, body])
    return html

@pytest.fixture
def render_value():
    """
    This is a fixture refers to the expected result from the render method
    we use it in two tests
    """
    return '''<html>
   <head>
      <title id="container">
         My Website
      </title>
   </head>
   <body>
      <div id="Container">
         <p>
            This is a paragraph
         </p>
         <p id="unique-id">
            Paragraph
         </p>
      </div>
   </body>
</html>'''

def test_element_creation(html_element):
    """
    This method is the test for the creation of the element
    """
    assert html_element.name == 'html'
    assert html_element.attrs is None
    assert len(html_element.children) == 2

def test_element_creation_invalid_name():
    """
    Test the negative case of creation an element using wrong tag name
    """
    with pytest.raises(NameError):
        HTMLElemnet("tag")

def test_element_append(html_element):
    """
    In this method we test the appending method if it work right or not
    """
    # ====== append an element =====
    p = P('New Paragraph')
    HTMLElemnet.append(html_element, p)
    assert len(html_element.children) == 3
    assert html_element.children[2].name == 'p'
    # ====== append a string =======
    HTMLElemnet.append(html_element, "This is string appending")
    assert html_element.children[3] == 'This is string appending'


def test_element_append_repeated_id(html_element):
    '''
    Test the negative case of append an element in case of same id
    '''
    with pytest.raises(NameError):
        div1 = Div(attrs = {'id': 'container'})
        HTMLElemnet.append(html_element, div1)

def test_find_by_attr(html_element):
    '''
    Test the method of finding elements by any attribute
    '''
    result = HTMLElemnet.find_elements_by_attrs(html_element, 'id', 'Container')
    assert result[0].name == 'div'


def test_find_by_attr_not_exist(html_element):
    '''
    This is to test the negative case of find by attr method
    '''
    result = HTMLElemnet.find_elements_by_attrs(html_element, 'id', 'Contain')
    assert len(result) == 0

def test_find_by_tag_name(html_element):
    '''
    Test the method of finding elements by tag name
    '''
    result = HTMLElemnet.find_elements_by_tag_name(html_element, 'p')
    assert len(result) == 2

def test_find_by_tag_name_not_exist(html_element):
    '''
    This is to test the negative case of find by tag name method
    '''
    result = HTMLElemnet.find_elements_by_tag_name(html_element, 'span')
    assert len(result) == 0

def test_render(render_value, html_element):
    '''
    Test the render method
    '''
    assert HTMLElemnet.render(html_element) == render_value

def test_render_file(render_value, html_element):
    '''
    Test render file method
    '''
    HTMLElemnet.render_file(html_element, 'index.html')
    with open("index.html", "r", encoding="utf-8") as file:
        result = file.read()
    assert result == ('<!DOCTYPE html>\n' + render_value)
