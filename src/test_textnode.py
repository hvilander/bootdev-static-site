import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node1 = TextNode("this is a text node with a URL", TextType.CODE, "http://www.123.com")
        node2 = TextNode("this is a text node with a URL", TextType.CODE, "http://www.123.com")
        self.assertEqual(node1, node2)


    def test_to_string(self):
        expected = "TextNode(test node, link text, http://testURL.net)"
        node = TextNode("test node", TextType.LINK, "http://testURL.net")
        self.assertEqual(f"{node}", expected)

    def test_not_equal(self):
        node1 = TextNode("this is a text node with a URL", TextType.CODE, "http://www.123.com")
        node2 = TextNode("different text", TextType.CODE, "http://www.123.com")
        self.assertNotEqual(node1, node2)


    def test_to_leaf_node_text(self):
        t_node = TextNode("plain text", TextType.NORMAL)
        expect = HTMLNode(None, "plain text")
        self.assertEqual(expect, t_node.to_html_node())

    def test_to_leaf_node_bold(self):
        t_node = TextNode("bold text", TextType.BOLD)
        expect = HTMLNode("b", "bold text")
        self.assertEqual(expect, t_node.to_html_node())

    def test_to_leaf_node_italic(self):
        t_node = TextNode("italic text", TextType.ITALIC)
        expect = HTMLNode("i", "italic text")
        self.assertEqual(expect, t_node.to_html_node())


    def test_to_leaf_node_code(self):
        t_node = TextNode("code text", TextType.CODE)
        expect = HTMLNode("code", "code text")
        self.assertEqual(expect, t_node.to_html_node())


    def test_to_leaf_node_image(self):
        t_node = TextNode("alt_text", TextType.IMAGE, "img:/url")
        expect = HTMLNode("img", "", None, {"src": "img:/url", "alt": "alt_text"})
        self.assertEqual(expect, t_node.to_html_node())

    def test_to_leaf_node_link(self):
        t_node = TextNode("my_link", TextType.LINK, "url:/link" )
        expect = HTMLNode("a", "my_link", None, {"href": "url:/link"})
        self.assertEqual(expect, t_node.to_html_node())


        


    if __name__ == "__main__":
        unittet.main()
