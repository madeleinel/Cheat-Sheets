# PostgreSQL

### Basic PostgreSQL commands

#### Starting Postgres locally
```
$ psql postgres
```

#### Connect to an existing database
```
$ \connect db_name;
```

#### Starting Postgres in a Docker container and connecting to a specified database
This command has to be run in the relevant directory.
```
$ docker-compose exec postgres psql -U postgres db_name
```

#### Exiting Postgres and/or Docker
```
$ ctrl + d

$ \q
```

### Setup for first-time use

#### Creating users, databases and granting access to databases
```
# Create database
$ CREATE DATABASE gorillas;

# Create user
$ CREATE USER jane_goodall WITH PASSWORD 'password’;

# Grant access to the database
$ GRANT ALL PRIVILEGES ON DATABASE gorillas TO jane_goodall;
```

## Working with table contents

### Create commands

#### To create a table
```
$ CREATE TABLE [table-name] (
  [column-name-1] [column-type-1] [additional data-1],
  [column-name-2] [column-type-2] [additional data-2]
  );
```
+ For each column, need to specify:
  + Its name
  + The type of data it will contain
  + Additional info about it (eg whether it can contain blank cells or not)
+ Each line (,[...],) represents one column of the table.
+ This can all be written on one line within the command line -- but can also split it over several lines to make it easier to read.
+ Best practice for column names varies; some argue ```[table-name]_[column-name]``` is best, others argue for ```[column-name]```.  

Eg:  
```
$ CREATE TABLE Activities (
  Activities_ID bigserial primary key,
  Activities_Name varchar(10) NOT NULL
  );
```
+ Creates a table names Activities which contains two columns:
  + The first column contains the acitivity ID; can only contain incrementing positive integers. (?)
  + The second column contains the activity name; can contain various characters, with a max limit of 10 characters.
+ ```NOT NULL``` Specifies that the column has to include some data, ie it is not allowed to contain null values.

### List commands
```
# To view all local roles (ie users)
$ \du

# To view all local databases
$ \l

# When connected to a database; To view all relations (eg tables)
$ \d

# To view the details of each column of a table
$ db_table \d

# To view all entries within a table
$ SELECT * FROM db_table;

# To view the first five entries within a table
$ SELECT * FROM db_table WHERE ID<6;

# To view all entries, ordered by the column entitled first_name
$ SELECT * FROM db_table ORDER BY first_name;
```

### Update commands

### Delete commands

#### To delete a database
```
$ DROP DATABASE database_name;
```

#### To delete a table
```
$ DROP TABLE db_table;
```

#### To delete all entries from a table
```
$ DELETE FROM db_table;
```

#### To delete one or more specific entries from a table
```
$ DELETE FROM db_table WHERE ID=[ID_number];

$ DELETE FROM db_table WHERE ID>[ID_number];

$ DELETE FROM db_table WHERE ID IN([ID_number_1], [ID_number_2]);
```

## Working with table properties

#### To update table properties
(Eg column data types and character limits)

<!-- Notes to go through and clean up below -->

### To edit existing tables

#### SELECT * FROM [table-name];
+ Displays the whole table within the command line.

#### INSERT INTO
+ Will insert data into an existing table.  
Eg:
```
INSERT INTO [table-name] ([column-1], [column-2,] [column-3]) VALUES
  ([r1-c1], [r1-c2], [r1-c3]),
  ([r2-c1], [r2-c2], [r1-c3]);

INSERT INTO activities (id, name, time) VALUES
  (1, 'Take a walk', '20min'),
  (2, 'Read a book', '1h'),
  (3, 'Listen to music', '30min'),
  (4, 'Code', '4hrs');
```
+ If don't specify the ID value:
```
INSERT INTO activities (name, time) VALUES
  [...];
```
  + An ID number will be assigned automatically, starting at 1 (and increasing as i++).
  + So if have already inserted records where we've specified the ID number, we will receive an error message when it tries to create a record with an ID number that already exists.
    + Eg, if ID=1 already exists, then will receive an error message the first time using this command, as it will try setting ID=1, which has already been used.
    + If we then run the exact same command over and over, it will try to set the ID number as 2, then 3, etc, until we find an ID number that is available
  + If don't specify ID numbers from the beginning, each record will be automatically be assigned it's own unique ID value, starting from 1 (and increasing as i++).

### Other notes

+ What it's used for...
+ Difference between database and server (eg laptop) - in terms of creating users etc.
+ Have to end all lines with ';' >> if miss and press enter without it >> can add it on the next line and then press enter -- as lines not separated by a ';' are read as being the same line >> this can also be used to split up content onto separate lines to make them more easily readable, even if the code itself needs to be within the same line.

<!-- Notes from codebar below -- some/a lot of duplicated notes -->

CREATE TABLE [table-name] (
	activities_ID bigserial primary key				      >> specifies that the second column is named ‘activities_ID’, can only contain incrementing positive integers(?) (so useful for ID # column) (i.e. bigserial), and each # has to be unique (i.e. primary key)
);

>> ‘text’ is more forgiving, allows more varied input content >> BUT takes longer to load

data types:
  varchar(x) == column has a variable length, with max limit of x
  text == variable unlimited length
  char(x) == column has fixed length, with max limit of x

  <!-- According to postgresql.org (https://www.postgresql.org/docs/9.1/static/datatype-character.html) >> "There is no performance difference among these three types, apart from increased storage space when using the blank-padded type, and a few extra CPU cycles to check the length when storing into a length-constrained column. While character(n) has performance advantages in some other database systems, there is no such advantage in PostgreSQL; in fact character(n) is usually the slowest of the three because of its additional storage costs. In most situations text or character varying should be used instead." -->

  To update data within the table:
  UPDATE [table-name] SET [column-name-1]=[‘new value’] WHERE [column-name]=[value];
  UPDATE activities SET name='Bikeride', time='20days' WHERE ID=11;
  >> Best practice >> to update table in rows based on ID number

  crud application	- create, read, update, delete abilities
