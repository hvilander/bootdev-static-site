# block md functions

from enum import Enum
from htmlnode import HTMLNode
import re


class BlockType(Enum):
    HEADING = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UL = "unordered list"
    OL = "ordered list"
    PARAGRAPH = "paragraph"

# document: a string representing a full md doc
# return a list of strings that is the blocks
def markdown_to_blocks(document):
    raw =  document.split('\n\n')
    blocks = []
    for b in raw:
        if b != "":
            blocks.append(b.strip())
    return blocks 


# some regex stolen from https://gist.github.com/elfefe/ef08e583e276e7617cd316ba2382fc40
def block_to_block_type(block):
    lines = block.split("\n")


    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE 


    type = BlockType.PARAGRAPH
    heading_regex = r"^#{1,6} (.+)"
    code_regex = r"^`{3}([\S]+)?\n([\s\S]+)\n`{3}$"

    quote_regex = r"^>"
    unordered_regex = r"^\s*[-+*]\s+(.+)$"
    ordered_regex = r"^\s*\d+\.\s+(.+)$"

    is_heading = re.match(heading_regex, block)
    is_code = re.match(code_regex, block)
    is_quote = re.match(quote_regex, block, re.MULTILINE)
    is_unordered = re.match(unordered_regex, block, re.MULTILINE)
    is_ordered = re.match(ordered_regex, block, re.MULTILINE)

    if is_heading: return BlockType.HEADING
    if is_code: return BlockType.CODE
    if is_quote: return BlockType.QUOTE
    if is_ordered: return BlockType.OL
    if is_unordered: return BlockType.UL

    return type
    
def get_heading_lvl(line):
    count = 0
    for char in line:
        if char == '#':
            count +=1
        else:
            break

    return f"h{count}" 

def get_li_for_ul(block):
    lines = block.split("\n")
    nodes = []
    for l in lines:
        s = 'empty'
        if l.startswith("- "): 
            s = l.split("- ")
        if l.startswith("* "):
            s = l.split("* ")
        nodes.append(HTMLNode('li', s[1].strip("\n")))

    return nodes

def get_li_for_ol(block):
    lines = block.split("\n")
    nodes = []
    for l in lines:
        s = re.split(r"\d.\s", l)
        nodes.append(HTMLNode('li', s[1]))

    return nodes

def get_block_quote(block):
    return HTMLNode("blockquote", block)

def block_to_html_node(block):
    type = block_to_block_type(block)
    match type:
        case BlockType.HEADING:
            tag = get_heading_lvl(block)
            s = block.split("# ") # TODO handle more than h1
            return HTMLNode(tag, s[1])
        case BlockType.CODE:
            s = block.split("```")
            child = HTMLNode("code", s[1])
            return HTMLNode("pre", None, [child])
        case BlockType.UL:
            children = get_li_for_ul(block)
            return HTMLNode("ul", None, children)
        case BlockType.OL:
            children = get_li_for_ol(block)
            return HTMLNode("ol", None, children)
        case BlockType.QUOTE:
            return get_block_quote(block)
        case _:
            return HTMLNode("p", block)


def markdown_to_html_node(document):
    blocks = markdown_to_blocks(document)
    children = []
    for b in blocks:
        children.append(block_to_html_node(b))


    # HTMLNode(tag, value, children, props):
    root_node = HTMLNode("div", None, children)

    return root_node

