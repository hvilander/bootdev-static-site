# block md functions

from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from inline_md import text_to_textnodes
from textnode import to_html_node
import re

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = to_html_node(text_node)
        children.append(html_node)
    return children

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
        children = text_to_children(l[2:])
        nodes.append(ParentNode('li', children))

    return nodes

def get_li_for_ol(block):
    lines = block.split("\n")
    nodes = []
    for l in lines:
        text = l[3:]
        children = text_to_children(text)
        nodes.append(ParentNode('li', children))
    return nodes

def get_block_quote(block):
    lines = block.split("\n")
    new_lines = []
    for l in lines:
        new_lines.append(l.lstrip(">").strip())
        content = " ".join(new_lines)
        children = text_to_children(content)
    return ParentNode("blockquote", children)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


## NEED TO FIX more things need to be parents
def block_to_html_node(block):
    type = block_to_block_type(block)
    match type:
        case BlockType.HEADING:
            tag = get_heading_lvl(block)
            s = block.split("# ") # TODO handle more than h1
            return LeafNode(tag, s[1])
        case BlockType.CODE:
            s = block.split("```")
            child = LeafNode("code", s[1])
            return ParentNode("pre", [child])
        case BlockType.UL:
            children = get_li_for_ul(block)
            return ParentNode("ul", children)
        case BlockType.OL:
            children = get_li_for_ol(block)
            return ParentNode("ol",  children)
        case BlockType.QUOTE:
            return get_block_quote(block)
        case _:
            return paragraph_to_html_node(block) 


def markdown_to_html_node(document):
    blocks = markdown_to_blocks(document)

    children = []
    for b in blocks:
        n = block_to_html_node(b)
        children.append(n)


    root_node = ParentNode("div", children, None)


    return root_node


