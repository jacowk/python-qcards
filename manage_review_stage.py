import qcards_db as qcards_db
from enum import Enum
import qcards_util as qu
import qcards_date_util as qdu

"""
An enum representing the data in t_lookup_review_stage

Jaco Koekemoer
2023-04-08
"""
class ReviewStage(Enum):

    DAILY = 1
    EVERY_2ND_DAY = 2
    WEEKLY = 3
    MONTHLY = 4

"""
An enum representing the data in t_lookup_odd_even

Jaco Koekemoer
2023-04-08
"""
class OddEven(Enum):

    ODD = 1
    EVEN = 2


"""
An enum representing the data in t_lookup_weekday

Jaco Koekemoer
2023-04-08
"""
class Weekday(Enum):

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

"""
When adding a review stage for a stack, it will always be for Daily review initially

Jaco Koekemoer
2023-04-08
"""
class AddReviewStage:

    def run(self, stack_id):
        review_stage_cd = ReviewStage.DAILY.value

        # Prepare SQL
        sql = "insert into t_review_stage(stack_id, review_stage_cd, create_date) values({:d}, {:d}, current_timestamp());".format(
            stack_id, review_stage_cd)

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
class UpdateEverySecondDayReviewStage:

    def run(self, stack_id, odd_even_cd):
        review_stage_cd = ReviewStage.EVERY_2ND_DAY.value

        # Prepare SQL
        sql = "update t_review_stage set review_stage_cd = {:d}, odd_even_cd = {:d} where stack_id = {:d};".format(review_stage_cd, odd_even_cd, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)

"""
Calculate the next review date if the review stage cd is every second day

Jaco Koekemoer
2023-04-08
"""
class CalculateEverySecondDayNextViewDate:

    def run(self, stack_id, odd_even_cd):
        # Get today's date
        today = qdu.DateUtil().get_now_as_date()

        # Determine which date to calculate
        if odd_even_cd == OddEven.ODD.value:
            next_odd_date = qdu.DateUtil().calculate_next_odd_date(today)
            return next_odd_date



"""
Update the review stage to weekly, for the given weekday_cd and week_count.
weekday_cd refers to t_lookup_weekday (Monday, Tuesday, etc)
week_count column (1 = once a week, 2 = every 2nd week, 3 = every third week

Jaco Koekemoer
2023-04-08
"""
class UpdateWeeklyReviewStage:

    def run(self, stack_id, weekday_cd, week_count):
        review_stage_cd = ReviewStage.WEEKLY.value

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
class UpdateMonthlyReviewStage:

    def run(self, stack_id, calendar_day, month_count):
        review_stage_cd = ReviewStage.MONTHLY.value

        # Prepare SQL
        sql = "update t_review_stage \
        set review_stage_cd = {:d}, \
        calendar_day = {:d}, \
        month_count = {:d} \
        where stack_id = {:d};".format(review_stage_cd, calendar_day, month_count, stack_id)

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql)
