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


        act_lst = split_nodes_delim([input], '**', TextType.BOLD)
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

        act_lst = split_nodes_delim([input], '**', TextType.BOLD)
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

        act_lst = split_nodes_delim([input], '**', TextType.BOLD)
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

        act_lst = split_nodes_delim([input], '`', TextType.CODE)
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

        act_lst = split_nodes_delim([input], '*', TextType.ITALIC)
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



    def test_link_regex(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        act = extract_md_links(text)

        self.assertEqual(act, expected)

    def test_img_regex(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected =  [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        act = extract_md_images(text)

        self.assertEqual(act, expected)


    def test_split_notes_links_zero(self):
        nodes = [TextNode("No links here", TextType.TEXT)]
        expected = [TextNode("No links here", TextType.TEXT)]

        self.assertEqual(expected, split_nodes_link(nodes))

    def test_split_notes_links_a_link(self):
        nodes = [TextNode("one links [here](http://to.url)", TextType.TEXT)]
        expected = [
            TextNode("one links ", TextType.TEXT),
            TextNode("here", TextType.LINK, "http://to.url")
        ]

        self.assertEqual(expected, split_nodes_link(nodes))


    def test_split_notes_links_two_links(self):
        nodes = [TextNode("one links [here](http://to.url) and [another](http://omg.co)", TextType.TEXT)]
        expected = [
            TextNode("one links ", TextType.TEXT),
            TextNode("here", TextType.LINK, "http://to.url"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.LINK, "http://omg.co"),
        ]
        act = split_nodes_link(nodes)
        self.assertEqual(expected, act)


    def test_split_notes_img(self):
        node = TextNode(
                "This is text with a img: ![boot.jpg](https://www.boot.dev) and ![other bear](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        expected = [
            TextNode("This is text with a img: ", TextType.TEXT),
             TextNode("boot.jpg", TextType.IMAGE, "https://www.boot.dev"),
             TextNode(" and ", TextType.TEXT),
             TextNode(
                 "other bear", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
             ),
         ]

        act = split_nodes_img([node])
        self.assertEqual(expected, act)



    def test_text_to_textnodes(self):
        input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        act = text_to_textnodes(input)
        self.assertEqual(expected, act)


