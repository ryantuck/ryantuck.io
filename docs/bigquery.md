# BigQuery

- [Notes on differences between BigQuery SQL and PostgreSQL](https://gist.github.com/ryantuck/78170a52734745add2026b57c70dec72)
- [Unnest stringified array of json objects in BigQuery](https://stackoverflow.com/questions/57117805/unnest-stringified-array-of-json-objects-in-bigquery)

### CLI

Run a query using standard SQL:

```
bq query --nouse_legacy_sql "select ..."
```

### Splitting string into rows

```
with

src as (
  select 1 as visit_id, '123-456' as tx_ids
  union all
  select 2 as visit_id, '789' as tx_ids
)

select
  src.tx_ids,
  tx_ids_unpacked as tx_id_unpacked
from
  src
  left join unnest(split(src.tx_ids, '-')) as tx_ids_unpacked
```
