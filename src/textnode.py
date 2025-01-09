from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "mono spaced"
    LINK = "link text"
    IMAGE = "Image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(tn1, tn2):
        is_eq_txt = tn1.text == tn2.text
        is_eq_tt = tn1.text_type.value == tn2.text_type.value
        is_eq_url = tn1.url == tn2.url

        return is_eq_txt and is_eq_tt and is_eq_url

    def __repr__(tn):
        return f"TextNode({tn.text}, {tn.text_type.value}, {tn.url})"

    def to_html_node(self):
        type = self.text_type
        tag = None
        value = self.text
        props = None

        match type:
            case TextType.TEXT:
                tag = None
            case TextType.BOLD:
                tag = "b"
            case TextType.ITALIC:
                tag = "i"
            case TextType.CODE:
                tag = "code"
            case TextType.LINK:
                tag = "a"
                props = {"href": self.url}
            case TextType.IMAGE:
                tag = "img"
                value = ''
                props = {"src": self.url, "alt": self.text}


            case _:
                raise Exception("Text Node: invalid value")



        return LeafNode(tag, value, props)


