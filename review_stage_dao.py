import review_stage_constant as rsc
import qcards_db as qcards_db

"""
When adding a review stage for a stack, it will always be for Daily review initially

Jaco Koekemoer
2023-04-08
"""
class AddReviewStageDAO:

    def run(self, stack_id):
        review_stage_cd = rsc.ReviewStage.DAILY.value

        # Prepare SQL
        sql = "insert into t_review_stage(stack_id, review_stage_cd, create_date) \
                values({:d}, {:d}, current_timestamp());".format(stack_id, review_stage_cd)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Update the review stage to every 2nd day, for the given odd_even_cd.
If Odd, the stack will be review on odd days, for example 1, 3, 5
If Event, the stack will be review on even days, for example 2, 4, 6

Jaco Koekemoer
2023-04-08
"""
class UpdateEverySecondDayReviewStageDAO:

    def run(self, stack_id, odd_even_cd):
        review_stage_cd = rsc.ReviewStage.EVERY_2ND_DAY.value

        # Prepare SQL
        sql = "update t_review_stage set review_stage_cd = {:d}, odd_even_cd = {:d} \
                where stack_id = {:d};".format(review_stage_cd, odd_even_cd, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Update the review stage to daily.

Jaco Koekemoer
2023-04-15
"""
class UpdateDailyReviewStageDAO:

    def run(self, stack_id):
        review_stage_cd = rsc.ReviewStage.DAILY.value

        # Prepare SQL
        sql = "update t_review_stage \
        set review_stage_cd = {:d} \
        where stack_id = {:d};".format(review_stage_cd, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Update the review stage to weekly, for the given weekday_cd and week_count.
weekday_cd refers to t_lookup_weekday (Monday, Tuesday, etc)
week_count column (1 = once a week, 2 = every 2nd week, 3 = every third week

Jaco Koekemoer
2023-04-08
"""
class UpdateWeeklyReviewStageDAO:

    def run(self, stack_id, weekday_cd, week_count):
        review_stage_cd = rsc.ReviewStage.WEEKLY.value

        # Prepare SQL
        sql = "update t_review_stage \
        set review_stage_cd = {:d}, \
        weekday_cd = {:d}, \
        week_count = {:d} \
        where stack_id = {:d};".format(review_stage_cd, weekday_cd, week_count, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Update the review stage to monthly
calendar_day (1, 2, 3, 4, etc)
month_count column (1 = once a month, 2 = every 2nd month, etc)

Jaco Koekemoer
2023-04-08
"""
class UpdateMonthlyReviewStageDAO:

    def run(self, stack_id, calendar_day, month_count):
        review_stage_cd = rsc.ReviewStage.MONTHLY.value

        # Prepare SQL
        sql = "update t_review_stage \
        set review_stage_cd = {:d}, \
        calendar_day = {:d}, \
        month_count = {:d} \
        where stack_id = {:d};".format(review_stage_cd, calendar_day, month_count, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Retrieve the review stage by stack id

Jaco Koekemoer
2023-04-15
"""
class RetrieveReviewStageByStackIdDAO:

    def run(self, stack_id):
        # Prepare SQL
        sql = "select id, stack_id, review_stage_cd, odd_even_cd, weekday_cd, week_count, calendar_day, month_count \
        from t_review_stage \
        where stack_id = {:d}".format(stack_id)
        print(sql)

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql)
