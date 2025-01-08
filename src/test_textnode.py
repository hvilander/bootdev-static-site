import unittest
from textnode import TextNode, TextType

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


        


    if __name__ == "__main__":
        unittet.main()
