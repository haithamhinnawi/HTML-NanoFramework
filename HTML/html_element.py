"""
This module defines the HTMLElement class for creating and manipulating HTML elements.
"""
from typing import Union

class HTMLElemnet:
    """
    This class represents an HTML element for creating and manipulating HTML content.

    You can use this class to create HTML elements, append child elements, render them to
    HTML strings, and search for elements based on attributes or tag names.

    Attributes:
        name (str): The name of the HTML element.
        value (Union[str, HTMLElement, list]): The value of the HTML element.
        attrs (dict): The attributes of the HTML element.

    Methods:
        append(parent: HTMLElement, element: HTMLElement): 
            Appends a child element to the current HTML element.
        render(depth: int = 0) -> str: Renders the HTML element and its children.
        find_elements_by_attrs(attr_name: str, attr_value: str): Finds elements by attributes.
        find_elements_by_tag_name(tag_name: str): Finds elements by tag name.
        render_file(file_path: str): Renders the HTML element to an HTML file.
        check_id(self, element: 'HTMLElemnet'): Checks if the element id exists in the tree
    """

    tag_names = {"html", "head", "title", "meta", "link", "style", "script", "body", "div", "abbr",
                 "p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "img", "ul", "ol", "li", "table",
                 "tr", "th", "td", "form", "input", "button", "textarea", "select", "label",
                 "iframe", "video", "audio", "canvas", "svg", "hr", "br", "span", "strong", "em"}

    def __init__(self, name: str, value: Union[str, 'HTMLElemnet', list] = None,
         attrs: dict[str, str] = None):
        self.elements_id = set()
        if not isinstance(name, str):
            raise TypeError("Element name must be a string")
        if not isinstance(value, (str, HTMLElemnet, list)) and value is not None:
            raise TypeError("Element value must be a string or an HtmlElement or a list")
        if not isinstance(attrs, dict) and attrs is not None:
            raise TypeError("Element attributes must be a dictionary")
        if name not in HTMLElemnet.tag_names:
            raise NameError('Invalid tag name for HTML element')
        if attrs is not None:
            if 'id' in attrs:
                self.elements_id.add(attrs['id'])
        self.name = name
        self.attrs = attrs
        self.children = []
        self.parent = None
        if value is not None:
            HTMLElemnet.append(self, value)

    @classmethod
    def append(cls, parent: 'HTMLElemnet', element: Union[str, 'HTMLElemnet', list]):
        '''
        append(parent: HTMLElement, element: HTMLElement): 
        Appends a child element to the current HTML element.
        '''
        if not isinstance(element, (HTMLElemnet, str, list)):
            raise TypeError("The appended element must be an HTMLElemnet or a string or a list")
        if isinstance(element, HTMLElemnet):
            HTMLElemnet.check_id(parent, element)
            element.parent = parent
            parent.children.append(element)
        elif isinstance(element, list):
            for item in element:
                if isinstance(item, HTMLElemnet):
                    HTMLElemnet.check_id(parent, item)
                    item.parent = parent
                parent.children.append(item)
        else:
            parent.children.append(element)

    @classmethod
    def render(cls, parent: 'HTMLElemnet', depth: int = 0) -> str:
        '''
        render(parent, depth: int = 0) -> str: Renders the HTML element and its children.
        '''
        result = ''
        space = '   '
        spaces = space * depth
        if isinstance(parent, HTMLElemnet):
            result = f'{spaces}<{parent.name}'
            if parent.attrs is not None:
                for key, val in parent.attrs.items():
                    result += f' {key}="{val}"'
            result += '>'
            for child in parent.children:
                if child != '':
                    result += '\n' + HTMLElemnet.render(child, depth+1)
            result += f'\n{spaces}</{parent.name}>'
        elif isinstance(parent, str):
            if parent != '':
                result += f'{spaces}{parent}'
        return result

    def find_elements(self, parent: 'HTMLElemnet', name: str, attr_value: str):
        '''
        find_elements(name: str, attr_value: str): This is the generic method to find elements,
        this function finds elements with their tag name or with attributes,
        if the user enter one string then the search will be on tag name,
        and if its two then it will be on attribute name and value.
        '''
        elements: list = []
        if(attr_value is not None) and parent.attrs is not None:
            if name in parent.attrs:
                if parent.attrs[name] == attr_value:
                    elements.append(parent)
        else:
            if parent.name == name:
                elements.append(parent)
        if len(parent.children) > 0:
            for child in parent.children:
                if not isinstance(child, str):
                    elements.extend(HTMLElemnet.find_elements(self, child, name, attr_value))
        return elements

    @classmethod
    def find_elements_by_attrs(cls, parent: 'HTMLElemnet', attr_name: str, attr_value: str = None):
        '''
        We will use this method to find elements with specific attribute value
        using the generic function find elements.
        '''
        return HTMLElemnet.find_elements(cls, parent, attr_name, attr_value)

    @classmethod
    def find_elements_by_tag_name(cls, parent: 'HTMLElemnet', tag_name: str):
        '''
        This function to find elements with their tag name, also in this
        function we will use the generic function find elements to get the result
        '''
        return HTMLElemnet.find_elements(cls, parent, tag_name, None)

    @classmethod
    def render_file(cls, parent, file_path: str):
        '''
        render_file(file_path: str): Renders the HTML element to an HTML file.
        '''
        with open(file_path, "w", encoding="utf-8") as file:
            file.write('<!DOCTYPE html>\n')
            file.write(HTMLElemnet.render(parent))

    def check_id(self, element: 'HTMLElemnet'):
        '''
        check_id(self, element: 'HTMLElemnet'): Checks if the element id exists in the tree
        '''
        if self.parent is not None:
            self.parent.check_id(element)
        check_intersection = self.elements_id.intersection(element.elements_id)
        if check_intersection:
            raise NameError(f"Element with id '{check_intersection}' already exists")
        self.elements_id.update(element.elements_id)
