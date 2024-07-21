/*
Run SQuirrel:
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh
*/

/*
Squirrel 

java -jar squirrel-sql-4.5.1-standard.jar
Installation directory: /usr/local/squirrel-sql-4.5.1
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh

Mysql Driver (Platform Independent): https://dev.mysql.com/downloads/connector/j/
*/

drop database qcards;
create database qcards;

ALTER TABLE t_card CHANGE COLUMN summary title varchar(100);
select * from t_card;

/* Cards */
ALTER TABLE t_card MODIFY back_content varchar(2000);

CREATE TABLE t_card (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    front_content VARCHAR(200),
    back_content VARCHAR(1000),
    stack_id INT(6),
    view_count INT(6),
    group_cd INT(6),
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

select * from t_card where id = 26;
select * from t_card where stack_id = 1;

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

describe t_card;

/* Review Stages
1 Daily
2 Every other day
3 Weekly
4 Monthly
*/
CREATE TABLE t_lookup_group (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100)
);

insert into t_lookup_group (description) values('Front');
insert into t_lookup_group (description) values('Middle');
insert into t_lookup_group (description) values('Back');

select * from t_lookup_group;

select c.id, 
c.summary, 
c.front_content, 
c.back_content, 
c.stack_id, 
c.view_count, 
c.group_cd, 
c.active, 
c.last_view_date,
s.description,
cat.description
from t_card c
left join t_stack s on c.stack_id = s.id
left join t_category cat on s.category_id = cat.id
where c.stack_id = 1;


select c.id, 
c.summary, 
c.front_content, 
c.back_content, 
c.stack_id, 
c.view_count, 
c.group_cd, 
c.active, 
c.last_view_date,
s.description,
cat.description
from t_card c
left join t_stack s on c.stack_id = s.id
left join t_category cat on s.category_id = cat.id
where c.id = 1;
