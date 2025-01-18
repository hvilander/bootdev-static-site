import re


def extract_title(markdown):
    h1_regex = r"^# (.+)"

    matches = re.match(h1_regex, markdown)
    if not matches:
        raise ValueError("no header")

    heading = matches[0]
    heading = heading.replace('# ', '')
    heading = heading.strip()

    return heading
