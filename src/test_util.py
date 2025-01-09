import unittest
from util import *
from textnode import TextNode, TextType


class TestUtil(unittest.TestCase):
    def test_basic_middle(self):
        strn ="This is text with a **bolded phrase** in the middle" 
        input = TextNode(strn, TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]


        act_lst = split_nodes_delim([input], '**', None)
        self.assertEqual(len(act_lst), len(expected))

        for i in range(0, len(expected)):
            exp = expected[i]
            act = act_lst[i]
            self.assertEqual(act, exp)

    def test_basic_start(self):
        strn ="**This is text with a bolded phrase** at the start" 
        input = TextNode(strn, TextType.TEXT)
        expected = [
            TextNode("This is text with a bolded phrase", TextType.BOLD),
            TextNode(" at the start", TextType.TEXT)
        ]

        act_lst = split_nodes_delim([input], '**', TextType.TEXT)
        self.assertEqual(len(act_lst), len(expected))

        for i in range(0, len(expected)):
            exp = expected[i]
            act = act_lst[i]
            self.assertEqual(act, exp)
 
    def test_basic_end(self):
        strn ="This is text with a bolded phrase **at the end**" 
        input = TextNode(strn, TextType.TEXT)
        expected = [
            TextNode("This is text with a bolded phrase ", TextType.TEXT),
            TextNode("at the end", TextType.BOLD),
        ]

        act_lst = split_nodes_delim([input], '**', None)
        self.assertEqual(len(act_lst), len(expected))

        for i in range(0, len(expected)):
            exp = expected[i]
            act = act_lst[i]
            self.assertEqual(act, exp)
 
    def test_basic_code(self):
        strn ="This is text with a `code block`" 
        input = TextNode(strn, TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]

        act_lst = split_nodes_delim([input], '`', None)
        self.assertEqual(len(act_lst), len(expected))

        for i in range(0, len(expected)):
            exp = expected[i]
            act = act_lst[i]
            self.assertEqual(act, exp)
 
    def test_basic_italic(self):
        strn ="This is text with an *italic*" 
        input = TextNode(strn, TextType.TEXT)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]

        act_lst = split_nodes_delim([input], '*', None)
        self.assertEqual(len(act_lst), len(expected))

        for i in range(0, len(expected)):
            exp = expected[i]
            act = act_lst[i]
            self.assertEqual(act, exp)
                                             
                                            
                      

    def test_unmatched(self):
        strn ="This is text with a **bolded phrase unmatched" 
        input = TextNode(strn, TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delim([input], "**", TextType.TEXT)


