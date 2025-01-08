import unittest
from parentnode import ParentNode 
from leafnode import LeafNode 


class TestParentNode(unittest.TestCase):
    def test_to_html_simple(self):
        node = ParentNode( "p",
         [
             LeafNode("b", "Bold text"),
             LeafNode(None, "Normal text"),
             LeafNode("i", "italic text"),
             LeafNode(None, "Normal text"),
         ],
        )

        node.to_html()
        self.assertEqual("a", "a")



