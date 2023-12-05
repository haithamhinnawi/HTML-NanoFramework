This class represents an HTML element for creating and manipulating HTML content.
You can use this class to create HTML elements, append child elements, render them to HTML strings, 
and search for elements based on attributes or tag names.
Attributes:
    name (str): The name of the HTML element -tag name-.
    value (Union[str, HTMLElement, list]): The value of the HTML element, it could be a string or an html element or a list of elements
    attrs (dict): The attributes of the HTML element e.g: id.
    there are also a list of children to implement the tree of elements, and the parent for every element.
Methods:
    append(parent: HTMLElement, element: HTMLElement): Appends a child element to the current HTML element, 
        first it checks if the id is one of the attributes and checks that id if it exists in the tree before, add it if not and raise an exception if it exist.
    render(depth: int = 0) -> str: Renders the HTML element and its children on the terminal, it uses recursion to print every element in the tree.
    find_elements_by_attrs(attr_name: str, attr_value: str): Finds elements by attributes and return them if any exist.
    find_elements_by_tag_name(tag_name: str): Finds elements by tag name and return them if any exist.
    render_file(file_path: str): Renders the HTML element to an HTML file.
    check_id(self, element: 'HTMLElemnet'): Checks if the element id exists in the tree and raise an exception if exist, it goes to the root first and start checking the list of childrens id,
    if it exist he will raise an exception, if not he will ad the id for all parents children list of ids