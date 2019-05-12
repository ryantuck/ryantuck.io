`psql` is a tool used for accessing postgres databases via
the command line.

## install

```
brew install postgresql
```

## load csv into sql really fast

`psql` can load csv data into an existing table insanely
fast. It requires that you have an existing table and a csv
file that has the appropriate number of columns.

Assuming `test.csv` is on your desktop and looks like this:

```
a,b,c
1,2,3
4,5,6
```

And you've created a table in your database like so:

```sql
create table test (
    a integer,
    b integer,
    c integer
);
```

Then load that bad boy in using `\copy`:

```
$ psql
> \copy test from /Users/ryan/test.csv csv header
```
