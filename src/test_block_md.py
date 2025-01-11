import unittest
from htmlnode import HTMLNode
from block_md import *


class TestBlockMD(unittest.TestCase):
    def test_markdown_to_blocks(self):
        document = "# Heading \n This is a paragraph \n * bullet 1 \n * bullet 2 \n"
        expected = ["# Heading", "This is a paragraph", "* bullet 1", "* bullet 2"]

        actual = markdown_to_blocks(document) 

        self.assertEqual(expected, actual)


