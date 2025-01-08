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
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expected, node.to_html() )


    def test_to_html_more_complex(self):
        node = ParentNode("div", [
            ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
             ], ),
            LeafNode("a", "link", {"href": "url://test.co", "target": "_blank"}),
            ParentNode("p", [ LeafNode(None, "2nd Normal text") ])
            ])

        expected = '<div><p><b>Bold text</b>Normal text</p><a href="url://test.co" target="_blank">link</a><p>2nd Normal text</p></div>'
        self.assertEqual(expected, node.to_html())



