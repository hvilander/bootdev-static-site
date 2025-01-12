import unittest
from htmlnode import HTMLNode
from block_md import *


class TestBlockMD(unittest.TestCase):
    def test_markdown_to_blocks(self):
        document = "# Heading \n\n This is a paragraph \n\n * bullet 1 \n * bullet 2 \n"
        expected = ["# Heading", "This is a paragraph", "* bullet 1 \n * bullet 2"]

        actual = markdown_to_blocks(document) 

        self.assertEqual(expected, actual)


    def test_block_to_block_type_heading(self):
        block = "# heading"
        expected = BlockType.HEADING
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_code(self):
        block = "```\ncode\n```\n"
        expected = BlockType.CODE
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)


    def test_block_to_block_type_quote(self):
        block = "> line one \n >line two"
        expected = BlockType.QUOTE
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_unordered(self):
        block = "- line one \n * line two"
        expected = BlockType.UL
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)


    def test_block_to_block_type_ordered(self):
        block = "1. line one \n 2. line two"
        expected = BlockType.OL
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)


    def test_md_to_html_simple(self):
        document = "# heading\n\n a paragraph"
        expected = HTMLNode("div", None, [HTMLNode("h1", "heading"), HTMLNode("p", "a paragraph")])
        actual = markdown_to_html_node(document)

        self.assertEqual(expected, actual)

    def test_md_to_html_code(self):
        document = "```\nsome \n code\n```\n\n and a paragraph\n"
        expected_children = [
            HTMLNode("pre", None, [
                HTMLNode("code", "\nsome \n code\n")
            ]),
            HTMLNode("p", "and a paragraph")
        ]

        expected = HTMLNode("div", None, expected_children)
        actual = markdown_to_html_node(document)
        string_expected = f"{expected}"
        string_actual = f"{actual}"
        self.assertEqual(string_expected, string_actual)


    def test_md_to_html_ul(self):
        document = "- one\n- two\n\np after ul"
        expected_children = [
            HTMLNode("ul", None, [
                HTMLNode("li", "one"),
                HTMLNode("li", "two"), 
            ]),
            HTMLNode("p", "p after ul")
        ]

        expected = HTMLNode("div", None, expected_children)
        actual = markdown_to_html_node(document)
        string_expected = f"{expected}"
        string_actual = f"{actual}"
        self.assertEqual(string_expected, string_actual)



    def test_md_to_html_ul_alt(self):
        document = "* one\n* two\n\np after ul"
        expected_children = [
            HTMLNode("ul", None, [
                HTMLNode("li", "one"),
                HTMLNode("li", "two"), 
            ]),
            HTMLNode("p", "p after ul")
        ]

        expected = HTMLNode("div", None, expected_children)
        actual = markdown_to_html_node(document)
        string_expected = f"{expected}"
        string_actual = f"{actual}"
        self.assertEqual(string_expected, string_actual)





    def est_md_to_html_node(self):
        document = "# heading 1\n- ul one\n* ul two\n> start\n> mid\n> end of quote\n```code\nblock\n```\n\n\n1. ol one\n2. ol2\na paragraph\n\n## heading 2\n\n"

        expected_children = [
            HTMLNode("h1", "heading 1"),
            HTMLNode("ul", None, [HTMLNode("li", "ul one"), HTMLNode("li", "ul two")]),
            HTMLNode("blockquote", "start\nmid\nend\n"),
            HTMLNode("pre", None, HTMLNode("code", "code\nblock")),
            HTMLNode("ol", None, [HTMLNode("li", "1. ol one"), HTMLNode("li", "n2. ol2")]),
            HTMLNode("p", "a paragraph"),
            HTMLNode("h2", "heading 2"),
        ]

        expected = HTMLNode("div", None, expected_children)
        actual = markdown_to_html_node(document)
        self.assertEqual(len(expected.children), len(actual.children))
        self.assertEqual(expected, actual)
