import re
import os
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
    title = extract_title(md)
    out = template.replace(' {{ Title }} ', title).replace("{{ Content }}", html_string)


    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(out)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)

    for i in items:
        path = f"{dir_path_content}/{i}"
        if os.path.isdir(path):
            new_content_dir = f"{dir_path_content}/{i}"
            new_dest_dir = f"{dest_dir_path}/{i}"
            generate_pages_recursive(new_content_dir, template_path, new_dest_dir)
        elif os.path.isfile(path):
            (name, ext) = os.path.splitext(i)
            if ext != ".md":
                return

            new_dest_dir = f"{dest_dir_path}/{name}.html"

            generate_page(path, template_path, new_dest_dir)


