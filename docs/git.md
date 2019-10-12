# git

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
