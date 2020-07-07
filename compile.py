"""
Compile mdzk docs to hugo-friendly format.

Get all files in specific dir by default.

TODO
- Compilation not preserving whitespace in outlines
- Support marking notes as private, disable links to them
- Generate backlinks
- Tags ending in a period or comma aren't recognized
"""
from dataclasses import dataclass
import os
import re
import shutil

import yaml

DOCS_DIR = os.path.expanduser("~/Dropbox/notes")
COMPILED_DIR = "content/notes"

BLACKLIST_REGEX = ["archive", "20.*"]


def read_config():
    with open("mdzk.yml") as f:
        return yaml.load(f)


@dataclass
class Note:

    filename: str

    def note_name(self):
        return os.path.splitext(self.filename)[0]

    def compiled_body(self):
        return flesh_out_note(self.note_name())


def _is_tag(word):
    return word.startswith('[[') and word.endswith(']]')


def _format_tag(tag):
    tag_clean = tag.strip("[]").replace("-", " ")
    note = tag.strip("[]")
    return f"[{tag_clean}]" + '({{< relref ' + f'"{note}.md"' + " >}} )"


def _maybe_format(word):
    if _is_tag(word):
        return _format_tag(word)
    return word

def _is_valid_note(note_title):
    return not any(re.match(br, note_title) for br in BLACKLIST_REGEX)


def flesh_out_note(note):
    filename = f"{note}.md"
    with open(os.path.join(DOCS_DIR, filename)) as f:
        body = f.read()
    rows = body.split("\n")
    fmt_rows = [" ".join([_maybe_format(w) for w in row.split()]) for row in rows]

    # strip out anything from '## inbox' to the bottom of the file
    inbox_row_idx = None
    for idx, row in enumerate(fmt_rows):
        if row.lower() == '## inbox':
            inbox_row_idx = idx
    if inbox_row_idx:
        fmt_rows = fmt_rows[:inbox_row_idx]

    fmt_body = "\n".join(fmt_rows)

    return fmt_body


def notes():
    return sorted(
        f for f in os.listdir(DOCS_DIR) if not f.startswith(".") and _is_valid_note(f)
    )


def compile_notes():
    shutil.rmtree(COMPILED_DIR)
    os.makedirs(COMPILED_DIR)
    for filename in notes():
        n = Note(filename=filename)
        with open(f"{COMPILED_DIR}/{n.note_name()}.md", "w") as f:
            print(os.path.join(DOCS_DIR, n.filename))
            f.write(n.compiled_body())


def main():
    compile_notes()


if __name__ == "__main__":
    main()
