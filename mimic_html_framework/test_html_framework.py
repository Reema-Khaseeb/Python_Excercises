"""Test positive and negative cases for HTMLElement class methods"""
import pytest

from .html_framework import HTMLElement
from .html_framework import TagNameError
from .html_framework import SameIdException


@pytest.fixture
def html_tree():
    """ Create and Return HTML Tree

    Returns:
        class: Root of HTML tree
    """
    root = HTMLElement('div', {"id":"div1", "class": "div_class"})
    div1 = HTMLElement('div', {"id":"div651", "title": "div2", "class": "div_class"})
    HTMLElement.append(root, div1)
    p_2 = HTMLElement('p', {"id":"pp_id", 'class': "div_class"})
    HTMLElement.append(p_2, 'Hi')
    HTMLElement.append(div1, p_2)
    a_elem = HTMLElement('a', {"href": "https://google.com", "id": "a_id", "target":"_blank" })
    HTMLElement.append(root, a_elem)
    a_child_img = HTMLElement('img', {"id":"img_id", "border":0,
    "alt":"Google", "src":"images02.jpg", "width":100, "height":100})
    HTMLElement.append(a_elem, a_child_img)
    print(root, type(root))
    return root


@pytest.fixture
def list_elems():
    """Returns a list of initiated html elements

    Returns:
        list: list of initiated elements
    """
    elem1 = HTMLElement('div', {'class': "div_class"}, 'Hi')
    elem2 = HTMLElement('p', {'class': "div_class"}, 'Hi')
    elem3_a = HTMLElement('a', {"href": "https://google.com", "id": "a_id", "target":"_blank" })
    return [elem1, elem2, elem3_a]


@pytest.mark.parametrize('expected_tag_name, expected_attrs, expected_val', [
    ('div', {'class': "div_class"}, 'Hi'),
    ('div', {'class': "div2_class"}, HTMLElement('div', {'class': "div_class"}, 'Hi')),
    ('div', {'class': "div2_class"}, pytest.lazy_fixture('list_elems'))
    ])
def test_initializer(expected_tag_name, expected_attrs, expected_val):
    """Test constructor functionality that its properties' values should be
    equal to the expected passed arguments

    Args:
        expected_tag_name (str): HTML tag name
        expected_attrs (dict): HTML element attributes
        expected_val (HTMLElement | str): HTML element values
    """
    elem = HTMLElement(expected_tag_name, expected_attrs, expected_val)
    assert elem.tag_name == expected_tag_name
    assert elem.attrs == expected_attrs
    if isinstance(expected_val, list):
        assert elem.value == expected_val
    else:
        assert elem.value == [expected_val]


@pytest.fixture
def expected_str():
    """Fixture function that returns a string to be compared with
    the rendered string from rendering methods

    Returns:
        str: expected rendered string from rendering methods
    """
    return """<!DOCTYPE html>
<div id='div1' class='div_class'>
    <div id='div651' title='div2' class='div_class'>
        <p id='pp_id' class='div_class'>Hi</p>
    </div>

    <a href='https://google.com' id='a_id' target='_blank'>
        <img id='img_id' border=0 alt='Google' src='images02.jpg' width=100 height=100></img>
    </a>
</div>
"""


def test_render(html_tree, expected_str):
    """ Test rendering HTML tree syntax as the expected string

    Args:
        html_tree (class): Root of HTML tree
        expected_str (str): expected html syntax text that should be rendered
    """
    assert HTMLElement.render(html_tree) == expected_str


def test_render_html_file(html_tree, expected_str):
    """Test render_html_file() method that should output html syntax text as expected

    Args:
        html_tree (class): Root of HTML tree
        expected_str (str): expected html syntax text that should be rendered
    """
    print(expected_str)
    HTMLElement.render_html_file(html_tree, 'render.html')
    with open("render.html", "r", encoding = 'utf-8') as file:
        assert file.read() == expected_str


def test_find_elems_by_attr(html_tree):
    """Test find_elements_by_attr() method functionality that should
    return all elements with the same passed attribute key and value

    Args:
        html_tree (class): Root of HTML tree
    """
    elements_with_same_attr = HTMLElement.find_elements_by_attr(html_tree, 'class', 'div_class')
    assert len(elements_with_same_attr) == 3
    assert [elem.elem_id for elem in elements_with_same_attr] == ['div1', 'div651', 'pp_id']


def test_find_elem_by_id(html_tree):
    """Test find_elements_by_id() method functionality that should
    return one element with the passed id value

    Args:
        html_tree (class): Root of HTML tree
    """
    elements_with_same_attr = HTMLElement.find_elements_by_id(html_tree, 'div1')
    assert len(elements_with_same_attr) == 1
    assert [elem.elem_id for elem in elements_with_same_attr] == ['div1']


def test_find_elems_by_tag_name(html_tree):
    """Test find_elements_by_tag_name() method functionality
    that should return all elements with the same passed tag name

    Args:
        html_tree (class): Root of HTML tree
    """
    elements_with_same_tag_name = HTMLElement.find_elements_by_tag_name(html_tree, 'div')
    assert len(elements_with_same_tag_name) == 2
    assert [elem.elem_id for elem in elements_with_same_tag_name] == ['div1', 'div651']


def test_append(html_tree):
    """Test append() functionality, that the appended value should be included in HTML tree

    Args:
        html_tree (class): Root of HTML tree
    """
    new_element = HTMLElement('span', {'class': 'span_class'})
    html_tree.append(html_tree, new_element)
    assert new_element in html_tree.value


def test_invalid_tag_name():
    """Negative test case, HTMLElement constructor should raise TagNameError custom exception
       when trying to initiate html element with invalid tag name
    """
    with pytest.raises(TagNameError) as custom_exception:
        HTMLElement('ss', {'class': "div_class"})
    assert str(custom_exception.value) == \
        'Tag name ss is not valid, please specify a valid tag name'


def test_same_id_initialize_elem(html_tree):
    """Negative test case, HTMLElement constructor should raise SameIdException custom exception
       when trying to initiate html element with a value that have same id
    """
    with pytest.raises(SameIdException) as custom_exception:
        HTMLElement('span', {'id': 'div1', 'class': "div_class"}, html_tree)
    assert str(custom_exception.value) == \
        "Shouldn't have same id value div1 for more than one element"


def test_same_id_exception_append(html_tree):
    """Negative test case for append() method that should raise SameIdException custom exception
       when trying to append html element with a value that have same id
    """
    with pytest.raises(SameIdException) as custom_exception:
        new_elem = HTMLElement('span', {'id': 'div1', 'class': "div_class"})
        HTMLElement.append(html_tree, new_elem)
    assert str(custom_exception.value) == \
    "Shouldn't have same id value div1 for more than one element"


@pytest.mark.parametrize('tree_html, attr_key, attr_val', [
    (html_tree, 'class', 3.5),
    (html_tree, 'style', "color:red;")])
def test_find_elements_by_attr_not_exist(tree_html, attr_key, attr_val):
    """Negative test case for find_elements_by_attr() method.
    It should return True(The negation of an empty list) when passing
    attrs that either its key or value or both don't exist

    Args:
        tree_html (class): Root of HTML tree
        attr_key (str): attribute key
        attr_val (str | number): attribute value
    """
    elem = HTMLElement.find_elements_by_attr(tree_html, attr_key, attr_val)
    assert not elem


def test_find_elements_by_tag_not_exist(html_tree):
    """Negative test case for find_elements_by_tag_name() method. It should
    return True(The negation of an empty list) when passing a tag name that doesn't exist

    Args:
        html_tree (root): Root of HTML tree
    """
    elements_with_same_tag_name = HTMLElement.find_elements_by_tag_name(html_tree, 'input')
    assert not elements_with_same_tag_name
