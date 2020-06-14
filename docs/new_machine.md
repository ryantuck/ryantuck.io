# New Machine Notes

Get a new macOS device and make sure it gets up to speed real quick.

## brew

get brew http://brew.sh/

`brew install git python vim tmux postgresql node bash-completion tree`

### install `brew-autoupdate`

Auto-update `brew` every 24h so you don't need to wait for it to update whenever you need to use it.

https://github.com/DomT4/homebrew-autoupdate

## keyboard

### key bindings

Download karabiner-elements: https://pqrs.org/osx/karabiner/

#### Map caps lock to ctrl / esc, and esc to shift+cmd

More detailed discussion here: https://github.com/tekezo/Karabiner-Elements/issues/8

Add the following to `~/.config/karabiner/karabiner.json` (path created only once Karabiner Elements app is opened):

```
{
    "profiles": [
        {
            "complex_modifications": {
                "rules": [
                    {
                        "manipulators": [
                            {
                                "description": "Change caps_lock to control when used as modifier, escape when used alone",
                                "from": {
                                    "key_code": "caps_lock",
                                    "modifiers": {
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "left_control"
                                    }
                                ],
                                "to_if_alone": [
                                    {
                                        "key_code": "escape",
                                        "modifiers": {
                                            "optional": [
                                                "any"
                                            ]
                                        }
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    },
                    {
                        "manipulators": [
                            {
                                "description": "Change esc to shift+cmd",
                                "from": {
                                    "key_code": "escape",
                                    "modifiers": {
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "left_shift",
                                        "modifiers": [
                                            "left_command"
                                        ]
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

For windows-default keyboards, configure the following:

`right/left_alt/gui` swaps in simple modifications, and select device in device list.

### key repeat rate

```
defaults write -g InitialKeyRepeat -int 10
defaults write -g KeyRepeat -int 1
```

then restart to have key repeat changes take effect.

### disable silly accented characters dialog box on keypress

```
defaults write -g ApplePressAndHoldEnabled -bool false
```

then restart for changes to take effect.

### remove ridiculous defaults

System Preferences > Keyboard > Text

- uncheck 'Capitalize words automatically'
- uncheck 'Add period with double-space'
- uncheck 'Use smart quotes and dashes'
- remove 'omw' = 'On my way!' replacement

## 1password

Download 1password 6.x. 

They will try to get you to download 1password 7, which requires an account and a monthly membership. If you've already paid for the app, that's obscene. 

Sync with iCloud vault via the app. 

Install the 1password chrome extension (not 1passwordX, which only works with the new system).


## vim

```
git clone git@github.com:VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
vim
:PluginInstall
```

## ssh keys

https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/

## git

```
git config --global user.name "Joe Schmo"
git config --global user.email "joe.schmo@gmail.com"
```

## postgres

```
brew services start postgresql
createdb ryan
psql -U ryan
```

Also be sure to edit the file at `/usr/local/var/postgres/postgresql.conf` to update any timezone settings to `UTC`.

## tmux

### system clipboard

i have the following line in my `.tmux.conf` file:

```
# use system clipboard
set-option -g default-command "reattach-to-user-namespace -l bash"
```

and so i need to do the following to get `tmux` working out of the box on a mac:

```
brew install reattach-to-user-namespace
```

## terminal

[osx-terminal-themes](https://github.com/lysyi3m/osx-terminal-themes) - Symfonic theme is neat.


## fonts

[droid sans mono](https://fonts.google.com/specimen/Droid+Sans+Mono?selection.family=Droid+Sans+Mono)

download, unzip, then:

```
open DroidSansMono.ttf
```

and select 'install font'.

## aws

```
pip install awscli
```

Ensure the following files are populated (assumes `rt` is default profile):

```
# ~/.aws/credentials
[rt]
aws_access_key_id = xxx
aws_secret_access_key = xxx
```

```
# ~/.aws/config
[profile rt]
region = us-east-1
output = json
```

And you set the appropriate environment variable:

```
export AWS_PROFILE="rt"
```

## docker

get docker for mac. it's great. install takes 2 seconds and you're ready to rock.

https://download.docker.com/mac/stable/Docker.dmg

Or whatever the latest download links are provided at this thread: https://github.com/docker/docker.github.io/issues/6910

### Ctrl-P in docker

To ensure Ctrl-P works within containers, add the following to `~/.docker/config.json`:

```
{
  ...
  "detachKeys": "ctrl-e,e",
  ...
}
```

## ipython

```
pip install ipython
```

### enable autoreload

Autoreload ensures you can work on python module logic and have the changes show up instantly in `ipython`.

Create a file at `~/.ipython/profile_default/ipython_config.py` with the following lines:

```
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
```

## chrome

Extensions: 

- uBlock
- Merge Windows
- Open in new tab

Disable swipe-to-go-back (requires chrome restart after):

```
defaults write com.google.Chrome AppleEnableSwipeNavigateWithScrolls -bool FALSE
```

## messages

Edit > Spelling and Grammar > Uncheck 'Correct Spelling Automatically' (phew)

## etc

Python code formatter:

```
pip3 install black
```

Jira to markdown converter:

```
npm install -g j2m
```

Simpler `man` pages:

```
npm install -g tldr
```

## Case-insensitive bash autocomplete

Add the following to `~/.inputrc`:

```
set completion-ignore-case on
```

Then hit `^X^R` to reload it
