Basic PostgreSQL commands:

psql postgres
> starts postgres session

ctrl + d		(or \q)
> exits postgres session

psql womentor
> starts fomenter database (?) > requires the database to already exist



To create the database and database user:

psql postgres
CREATE DATABASE womentor;
CREATE USER madeleine WITH PASSWORD 'maliwome78’;
		>> when already created a user on the server >> can skip CREATE USER step
GRANT ALL PRIVILEGES ON DATABASE womentor TO madeleine;

\connect [database-name]

CREATE TABLE [table-name] (
	[column-name] [column-type] [additional data],	>> specifies one column
	activities_ID bigserial primary key				      >> specifies that the second column is named ‘activities_ID’, can only contain incrementing positive integers(?) (so useful for ID # column) (i.e. bigserial), and each # has to be unique (i.e. primary key)
);

>> each ,…, represents one column / each comma divides two columns
>> can write it all on one line within postgres / command line >> OR divide lines using ENTER to make it more readable
>> some say best practice is to use '[table-name]_ID', others to just use ‘ID’
>> ‘text’ is more forgiving, allows more varied input content >> BUT takes longer to load

For each column >> name of column, type of data to be put into column, additional info reg the column

data types:
  varchar(x) == column has a variable length, with max limit of x
  text == variable unlimited length
  char(x) == column has fixed lenght, with max limit of x

  <!-- According to postgresql.org (https://www.postgresql.org/docs/9.1/static/datatype-character.html) >> "There is no performance difference among these three types, apart from increased storage space when using the blank-padded type, and a few extra CPU cycles to check the length when storing into a length-constrained column. While character(n) has performance advantages in some other database systems, there is no such advantage in PostgreSQL; in fact character(n) is usually the slowest of the three because of its additional storage costs. In most situations text or character varying should be used instead." -->

Additional info:
  NOT NULL == The column is not allowed to contain null values / the column has to include some data





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
