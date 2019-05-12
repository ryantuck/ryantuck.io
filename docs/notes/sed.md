`sed` is a cool tool for text manipulation.

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

## edit in place

The following will edit a file in-place using the `-i` flag:

```
sed -i -e 's/a/blah/g' test.txt
```
