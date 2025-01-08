from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf nodes need value")
        if self.tag == None:
            return self.value

        props = ''
        if self.props_to_html() != None:
            props = self.props_to_html()
        tag = self.tag

        return f"<{tag}{props}>{self.value}</{tag}>"


        
