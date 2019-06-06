# Notes

Grab-bag of notes.

## `vim`

- `q:` - command line history
- `q/` - search history
- `:sort u` - sort the file
- `:set tw=80` for soft word wrap, and works with outlines
- `gU` converts selection to ALL CAPS
- `gu` converts selection to lowercase
- `:! <command>` - run commands in vim

https://shapeshed.com/vim-netrw/ has great stuff about `netrw` and navigating
files

## `git`

Set upstream branch on forked repo:

```
git remote add upstream git@github.com:official/repo.git
```

Update origin url:

```
git remote set-url origin git@github.com:my/origin.git
```

Push an empty commit (to trigger a build or something):

```
git commit --allow-empty -m 'changing nothing'
```
