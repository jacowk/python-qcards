import review_stage_dao as rsd
import review_stage_constant as rsc
import qcards_date_util as qdu
import stack_bl as sbl

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
A business layer class for setting up the initial review stage

Jaco Koekemoer
2023-04-28
"""
class SetupInitialReviewStage:

    def run(self, stack_id):
        review_stage = ReviewStage()
        review_stage.set_stack_id(stack_id)

        # Check if a review stage already exists first for the stack id
        retrieve_review_stage = RetrieveReviewStageByStackId()
        existing_review_stage = retrieve_review_stage.run(stack_id)

        # If the review stage does not exist, then create it
        if existing_review_stage == None:
            add_review_stage = AddReviewStage()
            add_review_stage.run(review_stage)
            print("Review stage created for for stack id {:d}".format(stack_id))
        else:
            print("Review stage already exists for stack id {:d}".format(stack_id))

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
A business layer class for updating the review stage based on the selected review stage

Jaco Koekemoer
2023-05-05
"""
class UpdateReviewStage:

    def run(self, review_stage):
        if review_stage.get_review_stage_cd() == rsc.ReviewStage.DAILY.value:
            update_review_stage = UpdateDailyReviewStage()
            update_review_stage.run(review_stage)
        elif review_stage.get_review_stage_cd() == rsc.ReviewStage.EVERY_2ND_DAY.value:
            update_review_stage = UpdateEverySecondDayReviewStage()
            update_review_stage.run(review_stage)
        elif review_stage.get_review_stage_cd() == rsc.ReviewStage.WEEKLY.value:
            update_review_stage = UpdateWeeklyReviewStage()
            update_review_stage.run(review_stage)
        elif review_stage.get_review_stage_cd() == rsc.ReviewStage.MONTHLY.value:
            update_review_stage = UpdateMonthlyReviewStage()
            update_review_stage.run(review_stage)

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
A business layer class for calculating

Jaco Koekemoer
2023-05-05
"""
class CalculateNextViewDate:

    def run(self, review_stage):
        if review_stage.get_review_stage_cd() == rsc.ReviewStage.EVERY_2ND_DAY.value:
            calculate_next_view_date = CalculateEverySecondDayNextViewDate()
            return calculate_next_view_date.run(review_stage.get_odd_even_cd())
        elif review_stage.get_review_stage_cd() == rsc.ReviewStage.WEEKLY.value:
            calculate_next_view_date = CalculateWeeklyNextViewDate()
            return calculate_next_view_date.run(review_stage.get_weekday_cd(), review_stage.get_week_count())
        elif review_stage.get_review_stage_cd() == rsc.ReviewStage.MONTHLY.value:
            calculate_next_view_date = CalculateMonthlyNextViewDate()
            return calculate_next_view_date.run(review_stage.get_calendar_day(), review_stage.get_month_count())
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

"""
Calculate and update the next view date

Jaco Koekemoer
2023-05-05
"""
class CalculateAndUpdateNextViewDate():

    def run(self, stack_id):
        # Retrieve stack
        retrieve_stack = sbl.RetrieveStackById()
        stack = retrieve_stack.run(stack_id)

        # Retrieve review stage
        retrieve_review_stage = RetrieveReviewStageByStackId()
        review_stage = retrieve_review_stage.run(stack_id)

        # Calculate the next view date
        calculate_next_view_date = CalculateNextViewDate()
        next_view_date = calculate_next_view_date.run(review_stage)
        stack.set_next_view_date(next_view_date)

        # Update the stack
        if next_view_date is not None:
            update_next_view_date = sbl.UpdateNextViewDate()
            update_next_view_date.run(stack)

        return next_view_date

"""
Retrieve a list of all the review stages

Jaco Koekemoer
2023-05-04
"""
class ReviewStageLookupDict:

    def run(self):
        review_stage_lookup_dict = dict()
        review_stage_lookup_dict[rsc.ReviewStageSelectValues.SELECT_REVIEW_STAGE.value] = -1
        for review_stage in rsc.ReviewStage:
            review_stage_lookup_dict[review_stage.name] = review_stage.value
        return review_stage_lookup_dict

"""
Retrieve a list of odd and even

Jaco Koekemoer
2023-05-04
"""
class OddEvenLookupDict:

    def run(self):
        odd_even_lookup_dict = dict()
        odd_even_lookup_dict[rsc.ReviewStageSelectValues.SELECT_ODD_OR_EVEN.value] = -1
        for odd_even in rsc.OddEven:
            odd_even_lookup_dict[odd_even.name] = odd_even.value
        return odd_even_lookup_dict

"""
Retrieve a list of weekdays

Jaco Koekemoer
2023-05-04
"""
class WeekdayLookupDict:

    def run(self):
        weekday_lookup_dict = dict()
        weekday_lookup_dict[rsc.ReviewStageSelectValues.SELECT_WEEKDAY.value] = -1
        for weekday in rsc.Weekday:
            weekday_lookup_dict[weekday.name] = weekday.value
        return weekday_lookup_dict

# TODO: Week count and Month count
