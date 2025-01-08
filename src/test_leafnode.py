import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_props_p_tag(self):
        ln = LeafNode("p", "This is a paragraph of text.")
        exp = "<p>This is a paragraph of text.</p>"

        self.assertEqual(ln.to_html(), exp)

    def test_props_a_tag(self):
        ln = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        exp = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(ln.to_html(), exp)
