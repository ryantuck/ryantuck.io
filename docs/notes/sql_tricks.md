# SQL Tricks

Random SQL tricks. Not 101 material.

### Find columns that exist or don't in two tables

```
with

old_cols as (
    select
        table_name, column_name from information_schema.columns
    where
        table_name in ('my_table_1')
),

new_cols as (
    select
        table_name, column_name from information_schema.columns
    where
        table_name in ('my_table_2')
),

combo as (
    select distinct
        column_name,
        old_cols.table_name is not null as old_exists,
        new_cols.table_name is not null as new_exists
    from new_cols
    full outer join old_cols using (column_name)
)

select * from combo where old_exists is false or new_exists is false
;
```
