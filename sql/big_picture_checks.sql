select * from t_category;
select * from t_stack where id = 5;
select * from t_card where stack_id = 5;
select * from t_review_stage where stack_id = 5;
select review_stage_cd, odd_even_cd, weekday_cd, week_count, calendar_day, month_count from t_review_stage where stack_id = 5;
select * from t_lookup_review_stage;
