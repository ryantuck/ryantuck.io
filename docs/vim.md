# vim

- `q:` - command line history
- `q/` - search history
- `:sort u` - sort the file
- `:set tw=80` for soft word wrap, and works with outlines
- `gU` converts selection to ALL CAPS
- `gu` converts selection to lowercase
- `:! <command>` - run commands in vim
- `g_` goes to last non-blank character
- `P` pastes before cursor
- `:let` shows all vars
- `:set linebreak` allows for soft line wraps
- `:set columns=80` will limit the maximum number of columns to display to 80. This works nicely with `:set linebreak` to create a nice UI for writing text.
- `:g/=/d` will delete all lines that contain `=`
- [setting up spellcheck in vim](http://thejakeharding.com/tutorial/2012/06/13/using-spell-check-in-vim.html)
    - `:setlocal spell` to turn on spell check in a file
    - `]s` to go to next misspelled word
    - `[s` to go to previous misspelled word
    - `zg` to add word under cursor to `spellfile`


https://shapeshed.com/vim-netrw/ has great stuff about `netrw` and navigating files


