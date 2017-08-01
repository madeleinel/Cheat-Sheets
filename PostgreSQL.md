# PostgreSQL

## Introduction
+ What it's used for...
+ Difference between database and server (eg laptop) - in terms of creating users etc.
+ Have to end all lines with ';' >> if miss and press enter without it >> can add it on the next line and then press enter -- as lines not separated by a ';' are read as being the same line >> this can also be used to split up content onto separate lines to make them more easily readable, even if the code itself needs to be within the same line.

## Basic PostgreSQL commands:

### To get started
#### To set up and create a new database and user access
```
psql postgres
CREATE DATABASE womentor;
CREATE USER madeleine WITH PASSWORD 'maliwome78’;
GRANT ALL PRIVILEGES ON DATABASE womentor TO madeleine;
\connect womentor;
```

#### To connect to and view an existing database table
```
psql postgres
\connect [database-name]
SELECT * FROM [table-name];
```

### Starting and exiting Postgres sessions
Commands to run within the command line:
```
psql postgres
```
Starts a Postgres session.
```
ctrl + d
OR
\q
```
Exits the Postgres session.
```
psql [database-name]
```
Starts the [database-name] database (requires the database to already exist on the local server).

### To create a new database

#### CREATE DATABASE [database-name];
+ Creates a new database named [database-name].

#### CREATE USER [username] WITH PASSWORD ['password'];
+ Creates this user on the server.
+ So if creating a new database, and the user already exists on the server >> Can skip to the next step (ie granting database access to the user).

#### GRANT ALL PRIVILEGES ON DATABASE [database-name] TO [username];
+ Connect the user to the database (ie grant them access to it and its data).

#### \connect [database-name];
+ Connect to the database.
+ Ensures that any following commands are conducted on the database [database-name]. (?)

### To create a table
```
CREATE TABLE [table-name] (
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
CREATE TABLE Activities (
  Activities_ID bigserial primary key,
  Activities_Name varchar(10) NOT NULL
  );
```
+ Creates a table names Activities which contains two columns:
  + The first column contains the acitivity ID; can only contain incrementing positive integers. (?)
  + The second column contains the activity name; can contain various characters, with a max limit of 10 characters.
+ ```NOT NULL``` Specifies that the column has to include some data, ie it is not allowed to contain null values.

#### Table data types

+

#### \d [table-name]
+ Displays the columns of the table, laying out the name, type and modifiers of each
+ Press 'q' to exit

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















  To insert data into the table:
  >> the type of quotes used MATTERS >> either type it directly in the command line or Atom

  >> Can insert rows 1&2, then view table, and then add rows 3&4 separately
  >> will insert most recent rows at the bottom >> so even if set e.g. ID (which has ‘primary key’ specified) >> will still insert most recent at the bottom, even if the ID # is lower than the second most recent entry

  To delete one row:
  DELETE FROM activities WHERE ID=[ID-number);

  To delete several rows:
  DELETE FROM activities WHERE ID IN([ID-number-1],[ID-number-2]);

  To update data within the table:
  UPDATE [table-name] SET [column-name-1]=[‘new value’] WHERE [column-name]=[value];
  UPDATE activities SET name='Bikeride', time='20days' WHERE ID=11;
  >> Best practice >> to update table in rows based on ID number

  SELECT * FROM activities ORDER BY name;
  >> Display table and order rows alphabetically by the content within the ‘name’ column

  SELECT * FROM activities ORDER BY ID;
  >> Display table and order rows in numerical order, based on the  content within the ‘ID’ column

   SELECT * FROM activities WHERE ID<6;
  >> Will display all columns of rows 1-5



  crud application	- create, read, update, delete abilities









<!-- old notes (see if anythin g usefel ie re what a specific term/keyword means)
[table-name]_id bigserial primary key,			>> set type of data for this column
											bigserial = incrementing positive integers (?)
											‘primary key’ = each # has to be unique
											(useful for ID # column)
	[table-name]_name varchar(x) NOT NULL,		>> Setting the max number of characters
											each cell in that column can contain
											varchar(x) stating the maximum number of
											characters, can contain ‘varied characters’(meaning?)
	[table-name]_desc text NOT NULL,			>>
	date_added timestamp default NULL			>> -->
