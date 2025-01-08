from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):


        if self.tag == None:
            raise ValueError("Parent has no tag")

        if self.children == None:
            raise ValueError("Children requiered")

        start = f"<{self.tag}>"
        end = f"</{self.tag}>"
        middle = ""

        for child in self.children:
            middle += child.to_html()


        return start + middle + end
        




