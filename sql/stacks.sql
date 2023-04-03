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
    create_date TIMESTAMP NULL DEFAULT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

show tables;
select * from t_stack;

describe t_stack;
DROP TABLE t_stack;

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
