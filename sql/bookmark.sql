/*
Run SQuirrel:
sudo /usr/local/squirrel-sql-4.5.1/squirrel-sql.sh
*/

/* Bookmarks */
CREATE TABLE t_bookmark (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    stack_id INT(6),
    card_id INT(6),
    active BOOLEAN,
    create_date TIMESTAMP NOT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

show tables;
describe t_bookmark;
drop table t_bookmark;
truncate table t_bookmark;
select * from t_bookmark;

insert into t_bookmark(stack_id, card_id, active, create_date)
values(1, 0, True, NOW());

update t_bookmark
set active = False,
    last_modified_date = NOW()
where id = 1;

update t_bookmark
set stack_id = -1
where id = 2;

