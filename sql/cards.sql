/*
Run SQuirrel:
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh
*/

/* Cards */
CREATE TABLE t_card (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    summary VARCHAR(100),
    front_content VARCHAR(200),
    back_content VARCHAR(1000),
    stack_id INT(6),
    view_cnt INT(6),
    group_cnt INT(6),
    active BOOLEAN,
    last_view_date TIMESTAMP NULL,
    create_date TIMESTAMP NOT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

show tables;

describe t_card;
drop table t_card;
truncate table t_card;
select id, stack_id, view_cnt, last_view_date from t_card;

insert into t_card(summary, front_content, back_content, stack_id, view_cnt, group_cnt, active, create_date)
values('Front 1', 'Back 1', 1, 0, 1, True, NOW());


update t_card
set summary = 'summary 1',
front_content = 'Front 1 updated',
back_content = 'Back 1 updated',
stack_id = 2,
view_cnt = 1,
group_cnt = 2,
active = True,
last_view_date = now(),
next_view_date = now()
where id = 1;

select * from t_card;
truncate table t_card;

alter table t_category add column create_date timestamp after active;

alter table t_category add column last_modified_date timestamp after active;

/* Squirrel */
java -jar squirrel-sql-4.5.1-standard.jar
Installation directory: /usr/local/squirrel-sql-4.5.1
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh

Mysql Driver (Platform Independent): https://dev.mysql.com/downloads/connector/j/
