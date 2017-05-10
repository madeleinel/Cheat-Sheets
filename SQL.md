# SQL

## Intro to databases
+ Databases usually contain one or more tables of data
+ Tables are made up of columns and rows:
  + Columns:
    + "Fields"
    + Maintain specific information about every record within the table
  + Rows:
    + "Records"
    + Contain data for the table [objects]
    + There is one record for each [object] of a table
    + Eg, for a table of all customers of a store, there is one record/row for each customer
+ Most of the actions that need to be performed on databases are done with SQL statements

## Intro to SQL

### Tips and notes
+ SQL keywords are not case sensitive; eg "select" === "SELECT"
+ Semicolons are the standard method of separating SQL statements in database systems that allow >1 SQL 

statements to be executed within the same call to the server (if the system only allows 1 SQL statement 

within each call, there is no need to separate statements)
+ Some database systems require a semicolon at the end of each SQL statement (but not all of them do)

## Basic SQL Commands

### SELECT
+ Extracts data from a database
+ The data that is returned is stored within a results table, called "result-set"

#### SELECT * FROM [table-name];
+ Will display the content of all columns and rows of the table
+ Ie, will display the whole table

#### SELECT [field-name] FROM [table-name];
+ Will display the content of column [field-name]

#### SELECT [field-two], [field-one] FROM [table-name];
+ Will display the content of columns [field-one] and [field-two]
+ The chosen fields will be displayed within the results table (result-set) in the same order as they were 

specified within the statement
  + Ie, in this case [field-two] would be display within the first column, and [field-one] within the second 

column

#### SELECT DISTINCT [field-name] FROM [table-name]
+ Will display only distinct (different) values within the field [field-name]
+ Ie, it will not display duplicates

<!-- #### SELECT COUNT [field-name] FROM [table-name] >> (exact syntax?)
+ Will display the number of records within the field [field-name]
+ Not supported in Microsoft Access databases; see (W3Schools)

[https://www.w3schools.com/sql/sql_distinct.asp] for a workaround method -->

#### SELECT COUNT(DISTINCT [field-name]) FROM [table-name]
+ Will display the number of distinct values within the [field-name] field








### UPDATE
+ Updates data within a database

### DELETE
+ Deletes data from a database

### INSERT INTO
+ Inserts new data into a database
+ Ie, creates new content within the database

### CREATE DATABASE
+ Creates a new database

### ALTER DATABASE
+ Modifies a database

### CREATE TABLE
+ Creates a new table within a database

### ALTER TABLE
+ Modifies a table

### DROP TABLE
+ Deletes a table

### CREATE INDEX
+ Creates an index (a search key) for a database/table(which one?)

### DROP INDEX
+ Deletes an index
