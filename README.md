# library-management

## mySQL queries:
``` sql
create database library_app;
use library_app;
create table books (bname char(30), author char(50),bcode int(6) PRIMARY KEY, total int(20), subject char(20));
create table issue (name char(10),roll int(3) PRIMARY KEY ,bcode int(6) ,issue_date date);
create table retarn (name char(10),roll int(3) PRIMARY KEY,bcode int(6) ,return_date date);
```


