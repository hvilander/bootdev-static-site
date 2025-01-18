import unittest
from htmlnode import HTMLNode
from file import *


class TestFile(unittest.TestCase):
 def test_extract_title_single_header(self):
        document = "# Heading \n\n This is a paragraph \n\n * bullet 1 \n * bullet 2 \n"
        expected = "Heading"
        actual = extract_title(document) 
        self.assertEqual(expected, actual)

 def test_extract_title_double_header(self):
        document = "# Heading \n\n # second \n\n This is a paragraph \n\n * bullet 1 \n * bullet 2 \n"
        expected = "Heading"
        actual = extract_title(document) 
        self.assertEqual(expected, actual)


 def test_extract_title_no_header(self):
        document = "NO Heading \n\n  second \n\n This is a paragraph \n\n * bullet 1 \n * bullet 2 \n"
        with self.assertRaises(ValueError):
            extract_title(document) 




