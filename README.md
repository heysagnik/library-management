# library-management

## mySQL queries:
``` sql
create database library_app;
use library_app;
create table books (bname varchar(50), author varchar(50),bcode varchar(50), total int(20), subject varchar(50));
create table issue (name varchar(50),regno varchar(50),bcode int(50),issue_date date);
create table retarn (name varchar(50),regno varchar(50),bcode int(50),return_date date);
```


