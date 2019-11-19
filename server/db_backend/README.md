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

* Install gdal

MacOS (homebrew)
```
>> brew install gdal
```

* Install postgis
MacOS (homebrew)
```
>> brew install postgis
```

* At this point all dependencies should be fulfilled, so we can migrate our database
```
# within pipenv shell
>> ./manage.py makemigrations
# some output
>> ./manage.py migrate
# some output
>> ./manage.py runserver
# check that Django is hosting website on localhost:8000
```
