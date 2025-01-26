import re
from block_md import *


def extract_title(markdown):
    h1_regex = r"^# (.+)"

    matches = re.match(h1_regex, markdown)
    if not matches:
        raise ValueError("no header")

    heading = matches[0]
    heading = heading.replace('# ', '')
    heading = heading.strip()

    return heading


def generate_page(from_path, template_path, dest_path):
    print(f"gen page: {from_path} to: {dest_path} using: {template_path}")
    md = None
    tempate = None
    with open(from_path, "r") as content:
        md = content.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()


    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()

