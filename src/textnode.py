from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
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
        return f"TextNode({tn.text}, {tn.text_type.value}, {tn.url}"





