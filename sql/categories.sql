/*
Run SQuirrel:
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh
*/

/* Categories */
CREATE TABLE t_category (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100),
    parent_id INT(6),
    active TINYINT,
    create_date TIMESTAMP NULL DEFAULT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


ALTER TABLE t_category ALTER COLUMN create_date DROP DEFAULT;

describe t_category;

drop table t_category;
truncate table t_category;
select * from t_category;

insert into t_category(description, active, create_date) values('Design Patterns', True, NOW());
insert into t_category(description, active, create_date) values('Test', True, NOW());
insert into t_category(description, active, create_date) values('Test 2', True, NOW());
insert into t_category(description, parent_id, active, create_date) values('Test 2', 3, True, NOW());

update t_category set description = 'Java JDK Update', active = False, last_modified_date = NOW() where id = 1;
update t_category set description = 'Sub Test 2' where id = 4;

select * from t_category;

alter table t_category add column create_date timestamp after active;
alter table t_category add column last_modified_date timestamp after active;
