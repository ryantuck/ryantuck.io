# vim

- `q:` - command line history
- `q/` - search history
- `:sort u` - sort the file
- `:set tw=80` for soft word wrap, and works with outlines
- `gU` converts selection to ALL CAPS
- `gu` converts selection to lowercase
- `gf` goes to file under cursor
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
- `Ctrl+N/P` provides autocompletion for words already defined in your file.
- `<C-w>f` opens file under cursor in new vim window (not tmux window)
- `<C-w><C-w>` switches between vim windows
- `:! <command>` to run commands from a vim window
- `:set suffixesadd+=.md` to allow for interpreting `my_file` as `my_file.md` when using `gf`
- `<C-O>` goes back to the last file you jumped from

https://shapeshed.com/vim-netrw/ has great stuff about `netrw` and navigating files

https://andrew.stwrt.ca/posts/vim-ctags/ ctags seem like they could be cool, should experiment with these more.
