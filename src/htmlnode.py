
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
    # An HTMLNode without a tag will just render as raw text
    # An HTMLNode without a value will be assumed to have children
    # An HTMLNode without children will be assumed to have a value
    # An HTMLNode without props simply won't have any attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        foo = ""
        if self.props == None:
            return
        for k,v in self.props.items():
            foo += f" {k}=\"{v}\""

        return foo

    def __eq__(n1, n2):
        is_eq_tag = n1.tag == n2.tag
        is_eq_value = n1.value == n2.value
        is_eq_children = n1.children == n2.children
        is_eq_props = n1.props == n2.props


          # do do the child equal probably needs to walk the tree 
        return is_eq_tag and is_eq_value and is_eq_children and is_eq_props



    def __repr__(node):
        return f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})"
