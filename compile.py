"""
Compile mdzk docs to hugo-friendly format.

Get all files in specific dir by default.

TODO
- Generate backlinks
"""
from dataclasses import dataclass
import os
import re
import shutil

import yaml

DOCS_DIR = os.path.expanduser("~/Dropbox/notes")
COMPILED_DIR = "content/notes"

BLACKLIST_REGEX = ["archive", "20.*"]


@dataclass
class Note:

    filename: str

    def body(self):
        with open(os.path.join(DOCS_DIR, self.filename)) as f:
            return f.read()

    def note_name(self):
        return os.path.splitext(self.filename)[0]

    def tags(self):
        """
        Returns a [[list]] of all [[tags]] like so: ['list', 'tags']
        """
        tag_regex = r"\[\[([a-z0-9-]*)\]\]"
        results = re.findall(tag_regex, self.body()) or []
        return results

    def is_private(self):
        return '#private' in self.body()

    def compiled_body(self):
        body = self.body()
        for tag in self.tags():
            tag_clean = tag.replace('-', ' ')
            body = body.replace(
                f'[[{tag}]]',
                f"[{tag_clean}]" + '({{< relref ' + f'"{tag}.md"' + " >}} )",
            )
        return body


def md_files():
    return sorted(
        f for f in os.listdir(DOCS_DIR) if not f.startswith(".") and f.endswith('.md')
    )


def compile_notes():
    shutil.rmtree(COMPILED_DIR)
    os.makedirs(COMPILED_DIR)
    for filename in md_files():  # notes()
        n = Note(filename=filename)
        if n.is_private() or any(re.match(br, n.note_name()) for br in BLACKLIST_REGEX):
            continue
        with open(f"{COMPILED_DIR}/{n.note_name()}.md", "w") as f:
            print(os.path.join(DOCS_DIR, n.filename))
            f.write(n.compiled_body())


def main():
    compile_notes()


if __name__ == "__main__":
    main()
