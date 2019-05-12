## move schema

```sql
alter table old_schema.my_table set schema new_schema;
```

## rename table

```sql
alter table my_table rename to new_table_name;
```

## rename column

```sql
alter table my_table rename column old_col to new_col;
```

## json in postgres

<script src="https://gist.github.com/ryantuck/de263704472b80d6ec801efef9a2880e.js"></script>

## admin queries

<script src="https://gist.github.com/ryantuck/46de1eec35708201d88e6beee008839a.js"></script>

## information schema

<script src="https://gist.github.com/ryantuck/bce48a40e663df83bfe832904db3ed91.js"></script>

## row number


To get just one result given a particular filter, you can use `row_number()`.

In this case, I want to see an example of `detail` for each different `id` in the table:

```sql
select * from (
    select
        id,
        detail,
        row_number() over (partition by id) as row_num
    from
        my_table
) x where row_num = 1
```
