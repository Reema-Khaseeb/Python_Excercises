''' This module implement html framework that initiate, append, render, and find elements '''
class TagNameError(Exception):
    """ Create custom exception

    Args:
        Exception (class): Base Exception class

    Returns:
        str: Exception message
    """
    valid_tag_names = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'strong', 'abbr', 'a', 'big',
                    'b', 'html', 'head', 'body', 'form', 'input', 'em', 'dd', 'dl', 'dt', 'i',
                    'li', 'ol', 'marquee', 'strike', 'table', 'th', 'td', 'tr', 'tt', 'u', 'title',
                    '!--', 'address', 'article', 'aside', 'audio', 'bdi', 'bdo', 'blockquote',
                    'button', 'canvas', 'caption', 'cite', 'code', 'colgroup', 'text', 'data',
                    'datalist', 'del', 'details', 'dfn', 'dialog', 'div', 'em', 'embed', 'fieldset',
                    'figure',  'figcaption', 'footer', 'header', 'i', 'iframe', 'ins', 'kbd',
                    'legend', 'label', 'main', 'map', 'mark', 'meter', 'nav', 'noscript', 'object',
                    'optgroup', 'option', 'output', 'picture', 'pre', 'progress', 'q', 'rp', 'rt',
                    'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'span', 'style',
                    'sub', 'summary', 'sup', 'svg', 'tbody', 'template', 'textarea', 'tfoot',
                    'thead', 'time', 'ul', 'var', 'video', 'wbr', '!DOCTYPE', 'br', 'embed', 'hr',
                    'img', 'link', 'input', 'menu', 'area', 'source', 'base', 'col', 'meta',
                    'param', 'track']

    def __init__(self, tag_name, *args):
        """ Construct attributes for the TagNameError object

        Args:
            tag_name (str): HTML tag name
            args (tuple): The tuple of arguments given to the exception constructor
        """
        # Call the base class constructor with the parameters it needs
        super().__init__(args)
        self.tag_name = tag_name

    def __str__(self):
        """ Return Exception message

        Returns:
            str: Exception message
        """
        return f'Tag name {self.tag_name} is not valid, please specify a valid tag name'

class SameIdException(Exception):
    """ Create custom exception

    Args:
        Exception (class): Base Exception class
    """
    pass

class HTMLElement:
    """ A class to act as HTML framework that initiate, append, render, and find elements """
    def __init__(self, tag_name, attrs=None, val=None):
        """ Construct all the necessary attributes for the HTMLElement object

        Args:
            tag_name (str): HTML tag name
            attrs (dict, optional): HTML element attributes. Defaults to None.
            val (HTMLElement | str | list): HTML element values. Defaults to None.

        Raises:
            TagNameError: Raise custom exception when having invalid tag name
        """
        if tag_name not in TagNameError.valid_tag_names:
            raise TagNameError(tag_name)
        self.tag_name = tag_name
        self.attrs = attrs or {}
        self.value = []
        self.elem_id = attrs.get('id', None)

        self.handle_element_value(self, val)

    @classmethod
    def append(cls, element, val):
        """Append val to the given element

        Args:
            element (HTMLElement): HTML element to append to
            val (str | HTMLElement | list): HTML element value to be appended

        Raises:
            SameIdException: Raise custom exception when having elements with the same id value
        """
        cls.handle_element_value(element, val)

    @classmethod
    def handle_element_value(cls, element, val):
        """Handle appending a value(or values) to the given element
        considering value data type and custom exceptions

        Args:
            element (HTMLElement): HTML element to append to
            val (str | HTMLElement | list): HTML element value to be appended

        Raises:
            SameIdException: Raise custom exception when having elements with the same id value
        """
        if not isinstance(val, list):
            val = [val] if val else []
        for appended_elem in val:
            if isinstance(appended_elem, str):
                continue
            if list_elems_with_id:= cls.find_elements_by_id(appended_elem, element.elem_id):
                if list_elems_with_id:
                    raise SameIdException(
                        f"Shouldn't have same id value {element.elem_id} for more than one element")

        if isinstance(val, list):
            element.value.extend(val)
        else:
            element.value = val

    @classmethod
    def render(cls, element, level=0):
        """ Traverse the given element to create HTML DOM syntax

        Args:
            element (HTMLElement | str | list): HTML element to start traverse from
            level (int, optional): HTML Element level in tree. Defaults to 0.

        Returns:
            str: HTML syntax tree
        """
        if not element:
            return None

        indentation = ' '*4*level
        html = ''
        if level == 0:
            html += "<!DOCTYPE html>\n"
        html += f'{indentation}<{element.tag_name}'

        if element.attrs:
            html +=''.join(f" {key}='{val}'"
                    if isinstance(val, str) else f" {key}={val}"
                        for key, val in element.attrs.items())

        html+= '>'
        for child in element.value:
            html+= f'{child}' if isinstance(child, str) else f'\n{cls.render(child, level+1)}'
        if len(element.value) >= 1 and isinstance(element.value[0], cls):
            html += f'{indentation}</{element.tag_name}>\n'
        else:
            html += f'</{element.tag_name}>\n'

        if level == 0:
            print(html)
        return html

    @classmethod
    def render_html_file(cls, element, file_name):
        """ Render HTML syntax created into an html file

        Args:
            element (HTMLElement)
        """
        try:
            with open(file_name, 'w', encoding = 'utf-8') as file:
                file.write(cls.render(element))

        except (FileNotFoundError, IOError) as error:
            print(f"{type(error)}: {error}")

    @classmethod
    def find_elements_by_attr(cls, elem, attr_key, attr_val):
        """ Returns all html elements having the same attribute value for a specific key attribute

        Args:
            elem (HTMLElement): HTML element
            attr_key (str): attribute key
            attr_val (str | number): attribute value

        Raises:
            SameIdException: Raise custom exception when having elements with the same id value

        Returns:
            list: list of HTML elements
        """
        if not isinstance(elem, HTMLElement):
            return []
        list_elem = []
        if (attr_key, attr_val) in elem.attrs.items():
            list_elem.append(elem)

        for child in elem.value:
            if not isinstance(child, str):
                list_elem.extend(cls.find_elements_by_attr(child, attr_key, attr_val))
        return list_elem

    @classmethod
    def find_elements_by_id(cls, elem, id_val):
        """ Returns all html elements having id attribute

        Args:
            elem (HTMLElement): HTML element
            id_val (str): id attribute value

        Returns:
            list: list of HTML elements
        """
        return cls.find_elements_by_attr(elem, 'id', id_val)

    @classmethod
    def find_elements_by_tag_name(cls, element, name):
        """ Return HTML elements having the same tag name

        Args:
            element (HTMLElement): HTML element
            name (string): HTML element tag name

        Returns:
            list: list of HTML elements
        """
        list_elem = []
        if name == element.tag_name:
            list_elem.append(element)

        for child in element.value:
            if not isinstance(child, str):
                list_elem.extend(cls.find_elements_by_tag_name(child, name))
        return list_elem
