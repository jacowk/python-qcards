/*
Run SQuirrel:
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh
*/

/* Stacks */
CREATE TABLE t_stack (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	description VARCHAR(100),
    active BOOLEAN,
	source VARCHAR(300),
	category_id INT(6),
    next_view_date DATE NULL,
    create_date TIMESTAMP NOT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

alter table t_stack drop column last_view_date;

show tables;
select * from t_stack;
describe t_stack;
drop table t_stack;
truncate table t_stack;
select * from t_stack;

insert into t_stack(description, active, source, category_id, create_date)
values('HTML in W3Schools', True, 'www.w3schools.com', 3, NOW());

update t_stack
set description = 'Java Updated Stack',
active = True,
source = 'test source',
category_id = 2
where id = 1;


alter table t_category add column create_date timestamp after active;

alter table t_category add column last_modified_date timestamp after active;

/* Squirrel */
java -jar squirrel-sql-4.5.1-standard.jar
Installation directory: /usr/local/squirrel-sql-4.5.1
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh

Mysql Driver (Platform Independent): https://dev.mysql.com/downloads/connector/j/

/* Update the next_view_date */
update t_stack set next_view_date = '2023-04-10' where id = 4;

select * from t_stack;

