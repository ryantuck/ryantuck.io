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
- `g_` goes to last non-blank character
- `P` pastes before cursor
- `:let` shows all vars

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

## `sed`

test.txt:

```
a
b
c
```

```
cat test.txt | sed -e 's/a/blah/g'
```

output:

```
blah
b
c
```

### edit in place

The following will edit a file in-place using the `-i` flag:

```
sed -i -e 's/a/blah/g' test.txt
```

## create an ssh key pair

Here's how to create a key pair on a machine.

```
ssh-keygen -t rsa -b 4096 -C "ryan@tuck.com"
```

To authorize that key as one you want to allow onto the
machine:

```
cat ~/.ssh/new_key.pub >> ~/.ssh/authorized_keys
```

