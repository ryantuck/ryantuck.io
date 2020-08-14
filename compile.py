"""
Compile markdown notes to hugo-friendly format.

Get all files in specific dir by default.

TODO
- Compilation not preserving whitespace in outlines
- Support marking notes as private, disable links to them
- Generate backlinks
- Tags ending in a period or comma aren't recognized
- Avoid ## private section as well as ## inbox, treat as sections
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

    def _tag_link(self, tag):
        tag_clean = tag.replace('-', ' ')
        return f"[{tag_clean}]" + '({{< relref ' + f'"{tag}.md"' + " >}} )"

    def is_private(self):
        return '#private' in self.body()

    def backlinks_section(self, backlinks):
        return '\n'.join(
            ['## Backlinks\n'] + [f'- {self._tag_link(b)}' for b in backlinks]
        )

    def compiled_body(self, backlinks):
        body = self.body()
        for tag in self.tags():
            body = body.replace(f'[[{tag}]]', self._tag_link(tag))
        return body + '\n\n' + self.backlinks_section(backlinks)


def md_files():
    return sorted(
        f for f in os.listdir(DOCS_DIR) if not f.startswith(".") and f.endswith('.md')
    )


def compile_notes():
    shutil.rmtree(COMPILED_DIR)
    os.makedirs(COMPILED_DIR)

    all_notes = [Note(f) for f in md_files()]
    valid_notes = [
        n
        for n in all_notes
        if not (
            n.is_private() or any(re.match(br, n.note_name()) for br in BLACKLIST_REGEX)
        )
    ]

    # get all edges of graph
    edges = [(n.note_name(), t) for n in valid_notes for t in n.tags()]

    for n in valid_notes:
        backlinks = sorted(set([e[0] for e in edges if e[1] == n.note_name()]))
        with open(f"{COMPILED_DIR}/{n.note_name()}.md", "w") as f:
            print(os.path.join(DOCS_DIR, n.filename))
            f.write(n.compiled_body(backlinks))


def main():
    compile_notes()


if __name__ == "__main__":
    main()
