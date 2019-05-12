Ran into a weird issue having to do with calling a stored
procedure in postgres from python.

**tldr** - you have to explicitly `begin` and `commit`
transactions that call stored procs because `select`
statements don't normally explicitly get `commit`ted. We
avoid this issue in `psql` because i guess those `select`
statements actually do end up getting committed.

## example

Here's a silly stored proc:

```sql
create function do_stuff()
returns void as $$
begin

truncate table my_table;

insert into my_table values
    (1,2),
    (3,4)
;

end;
$$ language plpgsql;
```

To test if it works:

1. `truncate table my_table;`
2. run python script.
3. `select * from my_table;` and check whether the rows were
   inserted.

### won't work

```python
import dataset

db = dataset.connect()
db.query('select do_stuff();')
```

results:

```sql
select * from my_table; -- 0 rows
```

### will work

```python
import dataset

db = dataset.connect()
db.begin()
db.query('select do_stuff();')
db.commit()
```

or, `dataset` lets you wrap all that up as a transaction:

```python
import dataset

db = dataset.connect()
with db as tx:
    tx.query('select do_stuff();')
```

results:

```sql
select * from my_table; -- 2 rows (as expected)
```
