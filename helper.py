
class Helper:

    """
    A utility method for generating getters and setters
    """
    @staticmethod
    def generate_get_set():
        variables = ["review_stage_cd", "odd_even_cd", "weekday_cd", "week_count", "calendar_day", "month_count"]
        for variable in variables:
            print("\tdef get_{:s}(self):".format(variable))
            print("\t\treturn self.{:s}\n".format(variable))
            print("\tdef set_{:s}(self, {:s}):".format(variable, variable))
            print("\t\tself.{:s} = {:s}\n".format(variable, variable))

    @staticmethod
    def generate_init_variables():
        variables = ["id", "stack_id", "review_stage_cd", "odd_even_cd", "weekday_cd", "week_count", "calendar_day", "month_count"]
        for variable in variables:
            print("\t\tself.{:s} = None".format(variable))


helper = Helper()
#helper.generate_get_set()
helper.generate_init_variables()