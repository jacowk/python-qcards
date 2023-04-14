/* Return review stages not daily, but scheduled for today or in the past */
select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd 
from t_stack s, t_review_stage rs
where s.id = rs.stack_id
and s.active = 1
and s.next_view_date <= curdate()
and rs.review_stage_cd != 1; --Not Daily

/* Return review stages not daily, but scheduled for today or in the past */
select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd 
from t_stack s, t_review_stage rs
where s.id = rs.stack_id
and s.active = 1
and rs.review_stage_cd = 1; --Daily


update t_stack set next_view_date = curdate() where id = 4;
show tables;
select * from t_lookup_review_stage;
select * from t_review_stage;

select * from t_stack;

select 