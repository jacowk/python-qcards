/* Review Stage
-id
-stack_id
-review_phase_cd (t_lookup_review_phase)
-odd_even (t_lookup_odd_even)
-week_day (Mon, Tue, Wed - Only applicable to Weekly review phase)
-week_count (1 = once a week, 2 = every 2nd week, 3 = every third week)
-calendar_day (1, 2, 3 - Only applicable to Monthly review phase)
-month_count (1 = once a month, 2 = every 2nd month, etc)
*/
CREATE TABLE t_review_stage (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    stack_id INT(6),
    review_stage_cd INT(6),
    odd_even_cd INT(6),
    weekday_cd INT(6),
    week_count INT(6),
    calendar_day INT(6),
    month_count INT(6),
    create_date TIMESTAMP NOT NULL,
    last_modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

select * from t_review_stage;
truncate table t_review_stage;
drop table t_review_stage;

/* Insert a new review stage */
insert into t_review_stage(stack_id, review_stage_cd, create_date) values(1, 1, current_timestamp());
insert into t_review_stage(stack_id, review_stage_cd, create_date) values(2, 1, current_timestamp());

/* Update to every 2nd day review stage */
update t_review_stage set review_stage_cd = 2, odd_even_cd = 1 where stack_id = 1;

/* Update to weekly review stage */
update t_review_stage set review_stage_cd = 3, weekday_cd = 1, week_count = 1 where stack_id = 1;

/* Update to monthly review stage */
update t_review_stage set review_stage_cd = 4, calendar_day = 12, month_count = 2 where stack_id = 1;

/* Review Stages
1 Daily
2 Every other day
3 Weekly
4 Monthly
*/
CREATE TABLE t_lookup_review_stage (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100)
);

insert into t_lookup_review_stage (description) values('Daily');
insert into t_lookup_review_stage (description) values('Every other day');
insert into t_lookup_review_stage (description) values('Weekly');
insert into t_lookup_review_stage (description) values('Monthly');

select * from t_lookup_review_stage;

/* Odd Even
1 Odd
2 Even
*/
CREATE TABLE t_lookup_odd_even (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100)
);

insert into t_lookup_odd_even (description) values('Odd');
insert into t_lookup_odd_even (description) values('Even');

select * from t_lookup_odd_even;

/* Weekday
1 Monday (Python: 0)
2 Tuesday
3 Wednesday
4 Thursday
5 Friday
6 Saturday
7 Sunday (Python: 6)
*/

CREATE TABLE t_lookup_weekday (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100)
);

insert into t_lookup_weekday (description) values('Monday');
insert into t_lookup_weekday (description) values('Tuesday');
insert into t_lookup_weekday (description) values('Wednesday');
insert into t_lookup_weekday (description) values('Thursday');
insert into t_lookup_weekday (description) values('Friday');
insert into t_lookup_weekday (description) values('Saturday');
insert into t_lookup_weekday (description) values('Sunday');

select * from t_lookup_weekday;

select * from t_stack s where s.id = 6;
select * from t_review_stage rs where rs.id = 8;

update t_review_stage
set odd_even_cd = -1,
weekday_cd = -1,
week_count = -1,
calendar_day = -1,
month_count = -1
where id = 4

insert into t_review_stage(stack_id, review_stage_cd, odd_even_cd, weekday_cd, week_count, calander_day, month_count, create_date)
values({:d}, {:d}, -1, -1, -1, -1, -1, current_timestamp());