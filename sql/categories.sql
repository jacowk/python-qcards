/*
Run SQuirrel:
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh
*/

/* Categories */
CREATE TABLE t_category (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	description VARCHAR(100),
	active BOOLEAN,
	create_date TIMESTAMP,
	last_modified_date TIMESTAMP
);

CREATE TABLE t_category (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100),
    active TINYINT,
    create_date TIMESTAMP NULL DEFAULT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


ALTER TABLE t_category ALTER COLUMN create_date DROP DEFAULT;

describe t_category;

DROP TABLE t_category;

insert into t_category(description, active, create_date) values('Java SDK', True, NOW());

update t_category set description = 'Java JDK Update', active = False, last_modified_date = NOW() where id = 1;
update t_category set description = 'Java JDK Update', active = False where id = 1;

update t_category
	set description = "",
	active =
where id = ;

select id, description, active from t_category where id = ;

alter table t_category add column create_date timestamp after active;

alter table t_category add column last_modified_date timestamp after active;
