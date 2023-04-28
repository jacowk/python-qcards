import review_stage_dao as rsd
import review_stage_constant as rsc
import qcards_date_util as qdu

"""
A review stage domain class

Jaco Koekemoer
2023-04-28
"""
class ReviewStage:

    def __init__(self):
        self.id = None
        self.stack_id = None
        self.review_stage_cd = None
        self.odd_even_cd = None
        self.weekday_cd = None
        self.week_count = None
        self.calendar_day = None
        self.month_count = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_stack_id(self):
        return self.stack_id

    def set_stack_id(self, stack_id):
        self.stack_id = stack_id

    def get_review_stage_cd(self):
        return self.review_stage_cd

    def set_review_stage_cd(self, review_stage_cd):
        self.review_stage_cd = review_stage_cd

    def get_odd_even_cd(self):
        return self.odd_even_cd

    def set_odd_even_cd(self, odd_even_cd):
        self.odd_even_cd = odd_even_cd

    def get_weekday_cd(self):
        return self.weekday_cd

    def set_weekday_cd(self, weekday_cd):
        self.weekday_cd = weekday_cd

    def get_week_count(self):
        return self.week_count

    def set_week_count(self, week_count):
        self.week_count = week_count

    def get_calendar_day(self):
        return self.calendar_day

    def set_calendar_day(self, calendar_day):
        self.calendar_day = calendar_day

    def get_month_count(self):
        return self.month_count

    def set_month_count(self, month_count):
        self.month_count = month_count

"""
A business layer class for adding a new review stage

Jaco Koekemoer
2023-04-28
"""
class AddReviewStage:

    def run(self, review_stage):
        add_review_stage = rsd.AddReviewStageDAO()
        add_review_stage.run(review_stage.stack_id)

"""
A business layer class for updating a review stage for every second day

Jaco Koekemoer
2023-04-28
"""
class UpdateEverySecondDayReviewStage:

    def run(self, review_stage):
        # stack_id, odd_even_cd
        update_review_stage_dao = rsd.UpdateEverySecondDayReviewStageDAO()
        update_review_stage_dao.run(review_stage.stack_id, review_stage.odd_even_cd)

"""
A business layer class for updating a daily review stage

Jaco Koekemoer
2023-04-28
"""
class UpdateDailyReviewStage:

    def run(self, review_stage):
        update_review_stage_dao = rsd.UpdateDailyReviewStageDAO()
        update_review_stage_dao.run(review_stage.stack_id)

"""
A business layer class for updating a weekly review stage

Jaco Koekemoer
2023-04-28
"""
class UpdateWeeklyReviewStage:

    def run(self, review_stage):
        # stack_id, weekday_cd, week_count
        update_review_stage_dao = rsd.UpdateWeeklyReviewStageDAO()
        update_review_stage_dao.run(review_stage.stack_id, review_stage.weekday_cd, review_stage.week_count)

"""
A business layer class for updating a monthly review stage

Jaco Koekemoer
2023-04-28
"""
class UpdateMonthlyReviewStage:

    def run(self, review_stage):
        # stack_id, calendar_day, month_count
        update_review_stage_dao = rsd.UpdateMonthlyReviewStageDAO()
        update_review_stage_dao.run(review_stage.stack_id, review_stage.calendar_day, review_stage.month_count)

"""
A business layer class for retrieving a review stage

Jaco Koekemoer
2023-04-28
"""
class RetrieveReviewStageByStackId:

    def run(self, stack_id):
        retrieve_review_stage = rsd.RetrieveReviewStageByStackIdDAO()
        results = retrieve_review_stage.run(stack_id)

        if len(results) > 0:
            review_stage = ReviewStage()
            # id, stack_id, review_stage_cd, odd_even_cd, weekday_cd, week_count, calendar_day, month_count
            review_stage.set_id(results[0][0])
            review_stage.set_stack_id(results[0][1])
            review_stage.set_review_stage_cd(results[0][2])
            review_stage.set_odd_even_cd(results[0][3])
            review_stage.set_weekday_cd(results[0][4])
            review_stage.set_week_count(results[0][5])
            review_stage.set_calendar_day(results[0][6])
            review_stage.set_month_count(results[0][7])
            return review_stage
        return None

"""
Calculate the next review date if the review stage cd is every second day

Jaco Koekemoer
2023-04-08
"""
class CalculateEverySecondDayNextViewDate:

    def run(self, odd_even_cd):
        # Get today's date
        today = qdu.DateUtil().get_now_as_date()

        # Determine which date to calculate
        if odd_even_cd == rsc.OddEven.ODD.value:
            next_odd_date = qdu.DateUtil().calculate_next_odd_date(today)
            return next_odd_date
        else:
            next_even_date = qdu.DateUtil().calculate_next_even_date(today)
            return next_even_date

"""
Calculate the next view date if the review stage cd is weekly

Jaco Koekemoer
2023-04-11
"""
class CalculateWeeklyNextViewDate:

    def run(self, weekday_cd, week_count):
        # Get today's date
        today = qdu.DateUtil().get_now_as_date()

        # Calculate the next view date
        next_view_date = qdu.DateUtil().calculate_next_weekly_date(today, weekday_cd, week_count)
        return next_view_date

"""
Calculate the next view date if the review stage cd is monthly

Jaco Koekemoer
2023-04-10
"""
class CalculateMonthlyNextViewDate:

    def run(self, calendar_day, month_count):
        # Get today's date
        today = qdu.DateUtil().get_now_as_date()

        # Calculate the next view date
        next_view_date = qdu.DateUtil().calculate_next_monthly_date(today, calendar_day, month_count)
        return next_view_date

