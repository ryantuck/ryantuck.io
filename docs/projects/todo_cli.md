I wanted to manage my todos via the command line and didn't
know of any obvious solution. I really didn't want to use
anything that was too complicated or overkill. I basically
just wanted to manage todos as easily as I would if I were
just editing markdown files. So I made something painfully
simple and it works really well for me.

## markdown files

I started with a directory of markdown files.

```
mkdir ~/todo
vim ~/todo/work.md
vim ~/todo/done.md
```

## shell script

Cool, now I can just edit those guys. Great. But I didn't
want to have to type `vim ~/todo/blah.md` every time I
wanted to edit a file. So I made a script.

I created `/usr/local/bin/todo`:

```
#!/bin/bash

echo editing: $1
vim ~/todo/$1.md
```

Then made it executable:

```
chmod +x /usr/local/bin/todo
```

And now I can simply:

```
todo work
```

It's nice because if the file already exists I'll edit it
and if not it will automatically create a new one. Simple
functionality.

## autocomplete

Once I started getting tons of files in my `~/todo`
directory, I wanted to enable autocomplete, especially so I
wouldn't have to type out long names. Turns out this is p
easy.

In my `~/.bash_profile`:

```bash
# simple todo autocomplete
_todo_autocomplete()
{
    local cur opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    opts="$(ls ~/todo | sed -e 's/\.md//g')"
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _todo_autocomplete todo
```

Now I can type `todo [TAB]` and see all options.

Basically, autocomplete seems like it's a bunch of garbage
boilerplate with the only really important part being what
you set for the `opts` variable. In my case, I wanted to
remove the `.md` extension from anything in my list because
that's just how I want to interact with these files:

```
opts="$(ls ~/todo | sed -e 's/\.md//g')"
```

## git

I wanted to share my active `work.md` and `done.md` files
with my PM at work so he knows what I'm working on at any
given time. So I made a github gist that I can then commit
the files to, and they're formatted all pretty because it's
markdown.

So I made a `~/todo/todo-gist` directory and added the
following script (`push.sh`):

```bash
#!/bin/bash

cp ~/todo/work.md ~/todo/todo-gist/work.md
cp ~/todo/done.md ~/todo/todo-gist/done.md

d=$(date)
echo $d

cd ~/todo/todo-gist
git add .
git commit -m "$d"
git push origin master
```

And to make my life even easier just added an alias to my
bash profile to fire this guy off:

```
# push todo to gist
alias push="~/todo/todo-gist/push.sh"
```

## conclusion

Now my workflow for managing todos looks like this:

```
todo work
todo done
push
```

It's extremely extensible and painfully simple. No external
dependencies - just editing text files. 🙏












