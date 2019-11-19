# Installing a Local Database

* Make sure you have all libraries installed

```
pipenv check
```

* Install Postgreql and start a local server

MacOS (homebrew)
```
>> brew install psql
>> brew services start psql
```

* Check if Postgresql can connect successully
```
>> psql
psql (11.5)
Type "help" for help.
user=# >> \q
```

* 
