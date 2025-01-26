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


    def test_generate_page(self):
        from_path = "content/index.md"
        dest_path = "public/index.html"
        template_path = "./template.html"

        generate_page(from_path, template_path, dest_path)


    def test_recursive(self):
        content_dir_path = "content"
        dest_path = "public"
        template_path = "./template.html"


        generate_pages_recursive(content_dir_path, template_path, dest_path)


    


