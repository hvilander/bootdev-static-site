import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_display(self):
        htmlNode = HTMLNode("tag", "my value")
        expected = " HTMLNode(tag, my value, None, None)"
        strn = f" {htmlNode}"

        self.assertEqual(strn, expected)

    def test_eq(self):
        n1 = HTMLNode("tag", "my value")
        n2 = HTMLNode("tag", "my value")
        self.assertEqual(n1, n2)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank"
        }
        n = HTMLNode("tag", "my value", None, props)
        # note the leading space!!
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(n.props_to_html(), expected)
