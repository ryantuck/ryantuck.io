Had a hell of a time trying to get the results of a `.sql` file to output to a csv. Here's what I had to do:

```
#!/bin/bash

# executes a .sql file and outputs results to a .csv
# ./sql_to_csv.sh my_query.sql output.csv

CONN="psql -U my_user -d my_db"

# remove all semicolons and comments
# replace newlines with spaces
QUERY="$(sed 's/;//g;/^--/ d;s/--.*//g;' $1 | tr '\n' ' ')"
echo "$QUERY"

echo "\\copy ($QUERY) to '$2' with csv header" | $CONN > /dev/null
```

So to make it work:

```
./sql_to_csv.sh my_query.sql output.csv
```
