from textnode import TextType, TextNode

def text_type_by_delim(delim):
    match delim:
        case "**":
            return TextType.BOLD
        case "`":
            return TextType.CODE
        # its stupid that they use * for italic
        case "*":
            return TextType.ITALIC
        case _:
            raise Exception("Not Implemented")


def split_text_node(old_text_node, delimiter):
    lst = old_text_node.text.split(delimiter)
    new_lst = []
    ttype = text_type_by_delim(delimiter)

    # odd number of split is unmatched
    is_unmatched = len(lst) % 2 == 0 

    if is_unmatched:
        raise ValueError(f"Unmatched deliminator: '{delimiter}'")
    
    if "" in lst:
        if lst[0] == '':
            new_lst.append(TextNode(lst[1], ttype))
            new_lst.append(TextNode(lst[2], TextType.TEXT))
        elif lst[-1] == '':
            new_lst.append(TextNode(lst[0], TextType.TEXT))
            new_lst.append(TextNode(lst[1], ttype))
    else:
        new_lst.append(TextNode(lst[0], TextType.TEXT))
        new_lst.append(TextNode(lst[1], ttype))
        new_lst.append(TextNode(lst[2], TextType.TEXT))

    return new_lst
    




# list of old nodes
# a delimiter
# text type
# return a list of nodes
def split_nodes_delim(old_nodes, delimiter, text_type):
    new_list = []


    for n in old_nodes:
        to_append = n
        # todo no nesting of inline markdown for now
        if n.text_type == TextType.TEXT:
            to_append = split_text_node(n, delimiter)

        new_list.extend(to_append)

    
    return new_list
