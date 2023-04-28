select * from t_category;
describe t_category;
select * from t_stack where id = 5;
describe t_stack;
select * from t_card where stack_id = 5;
select * from t_review_stage where stack_id = 5;
select * from t_review_stage;
select review_stage_cd, odd_even_cd, weekday_cd, week_count, calendar_day, month_count from t_review_stage where stack_id = 5;
select * from t_lookup_review_stage;

select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd, c.description, lrs.description 
from t_stack s, t_review_stage rs, t_category c, t_lookup_review_stage lrs 
where s.id = rs.stack_id 
and s.category_id = c.id 
and rs.review_stage_cd = lrs.id
and s.active = 1 
and rs.review_stage_cd = 1;

select s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, rs.review_stage_cd, c.description, lrs.description 
from t_stack s, t_review_stage rs, t_category c, t_lookup_review_stage lrs 
where s.id = rs.stack_id 
and s.category_id = c.id 
and rs.review_stage_cd = lrs.id
and s.active = 1 
and s.next_view_date <= curdate() 
and rs.review_stage_cd != 1;

show tables;
