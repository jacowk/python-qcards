import stack_dao as sd
import qcards_util as qu
import stack_constant as sc

"""
A stack domain class

Jaco Koekemoer
2023-04-23
"""
class Stack:

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_active(self):
        return self.active

    def set_active(self, active):
        self.active = active

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    def set_category_id(self, category_id):
        self.category_id = category_id

    def get_category_id(self):
        return self.category_id

    def get_next_view_date(self):
        return self.next_view_date

    def set_next_view_date(self, next_view_date):
        self.next_view_date = next_view_date

    def get_review_stage_id(self):
        return self.review_stage_id

    def set_review_stage_id(self, review_stage_id):
        self.review_stage_id = review_stage_id

    def get_review_stage(self):
        return self.review_stage

    def set_review_stage(self, review_stage):
        self.review_stage = review_stage

"""
Business layer for adding stacks

Jaco Koekemoer
2023-04-23
"""
class AddStack:

    def run(self, stack):
        add_stack_dao = sd.AddStackDAO()
        add_stack_dao.run(stack.description, stack.active, stack.source, stack.category_id)

"""
Business layer for updating stacks

Jaco Koekemoer
2023-04-23
"""
class UpdateStack:

    def run(self, stack):
        update_stack_dao = sd.UpdateStackDAO()
        update_stack_dao.run(stack.id, stack.description, stack.active, stack.source, stack.category_id)

"""
Business layer for updating the next view date for a stack

Jaco Koekemoer
2023-05-05
"""
class UpdateNextViewDate:

    def run(self, stack):
        update_next_view_date_dao = sd.UpdateNextViewDateDAO()
        update_next_view_date_dao.run(stack.get_id(), stack.get_next_view_date())

"""
Business layer for retrieve a stack by id

Jaco Koekemoer
2023-04-24
"""
class RetrieveStackById:

    def run(self, id):
        retrieve_category_dao = sd.RetrieveStackByIdDAO()
        result = retrieve_category_dao.run(id) # Returns 2 dimensional tuple
        # id, description, active, source, category_id, next_view_date

        # Convert result to Category class
        stack = Stack()
        stack.set_id(result[0][0])
        stack.set_description(result[0][1])
        qcards_util = qu.QCardsUtil()
        stack.set_active(qcards_util.convert_tinyint_to_boolean(result[0][2]))
        stack.set_source(result[0][3])
        stack.set_category_id(result[0][4])
        stack.set_next_view_date(result[0][5])
        stack.set_review_stage_id(result[0][6])
        stack.set_review_stage(result[0][7])
        return stack

"""
Business layer for retrieving all stacks

Jaco Koekemoer
2023-04-24
"""
class RetrieveAllStacks:

    def run(self):
        # Retrieve all stacks via the DAO
        retrieve_stack = sd.RetrieveAllStacksDAO()
        stacks = retrieve_stack.run()

        # Convert data for front-end display
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            # s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, c.description
            converted_category = (
                stack[0], # id
                stack[1], # description
                qcards_util.convert_tinyint_to_boolean(stack[2]), # active
                stack[3], # source
                stack[4], # category_id
                stack[5] if stack[5] is not None else '', # next_view_date
                stack[6] if stack[6] != None else '', # category_description
                stack[7], # review stage id
                stack[8]  # review stage
            )
            converted_stacks = converted_stacks + (converted_category,)  # Building up a tuple of tuples
        return converted_stacks

"""
Business layer for retrieving all active stacks by category id

Jaco Koekemoer
2023-04-24
"""
class RetrieveActiveStacksByCategoryId:

    def run(self, category_id, active = None):
        # Retrieve all stacks via the DAO
        retrieve_stack = sd.RetrieveActiveStacksByCategoryIdDAO()
        stacks = retrieve_stack.run(category_id, active)

        # Convert data for front-end display
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            # s.id, s.description, s.active, s.source, s.category_id, s.next_view_date, c.description
            converted_stack = (
                stack[0],  # id
                stack[1],  # description
                qcards_util.convert_tinyint_to_boolean(stack[2]),  # active
                stack[3],  # source
                stack[4],  # category_id
                stack[5] if stack[5] is not None else '',  # next_view_date
                stack[6] if stack[6] is not None else '', # category_description
                stack[7], # review stage id
                stack[8]  # review stage
            )
            converted_stacks = converted_stacks + (converted_stack,)  # Building up a tuple of tuples
        return converted_stacks

"""
Business layer for retrieving all sheduled active stacks

Jaco Koekemoer
2023-04-24
"""
class RetrieveScheduledActiveStacks:

    def run(self):
        # Retrieve all stacks via the DAO
        retrieve_stack = sd.RetrieveScheduledActiveStacksDAO()
        stacks = retrieve_stack.run()

        # Convert data for front-end display
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            converted_category = (
                stack[0], # id
                stack[1], # description
                qcards_util.convert_tinyint_to_boolean(stack[2]), # active
                stack[3], # source
                stack[4], # category_id
                stack[5] if stack[5] is not None else '', # next_view_date
                stack[6], # review_stage_cd
                stack[7] if stack[7] != None else '', # category_description
                stack[8]  # review stage description
            )
            converted_stacks = converted_stacks + (converted_category,)  # Building up a tuple of tuples
        return converted_stacks

"""
Business layer for retrieving daily active stacks

Jaco Koekemoer
2023-04-24
"""
class RetrieveDailyActiveStacks:

    def run(self):
        # Retrieve all stacks via the DAO
        retrieve_stack = sd.RetrieveDailyActiveStacksDAO()
        stacks = retrieve_stack.run()

        # Convert data for front-end display
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            converted_category = (
                stack[0], # id
                stack[1], # description
                qcards_util.convert_tinyint_to_boolean(stack[2]), # active
                stack[3], # source
                stack[4], # category_id
                stack[5] if stack[5] is not None else '', # next_view_date
                stack[6], # review_stage_cd
                stack[7] if stack[7] is not None else '', # category_description
                stack[8]  # review stage description
            )
            converted_stacks = converted_stacks + (converted_category,)  # Building up a tuple of tuples
        return converted_stacks

"""
A class for retrieving a stacks to be reviewed

Jaco Koekemoer
2023-04-12
"""
class RetrieveStacksForReview:

    def run(self):
        # Retrieve scheduled stacks
        retrieve_scheduled_stacks = sd.RetrieveScheduledActiveStacksDAO()
        scheduled_stacks = retrieve_scheduled_stacks.run()

        # Retrieve active stacks
        retrieve_daily_stacks = sd.RetrieveDailyActiveStacksDAO()
        daily_stacks = retrieve_daily_stacks.run()

        # Combine stacks and return
        return scheduled_stacks + daily_stacks

"""
Business layer for retrieving all stacks as a dictionary

Jaco Koekemoer
2023-04-27
"""
class RetrieveAllStacksDict:

    def run(self):
        # Retrieve all categories via the DAO
        retrieve_stack = sd.RetrieveAllStacksDAO()
        stacks = retrieve_stack.run()

        # Convert data for front-end display
        stack_dictionary = dict()
        stack_dictionary[sc.StackConstant.SELECT_STACK.value] = -1
        for stack in stacks:
            stack_dictionary[stack[1]] = stack[0] # description: id
        return stack_dictionary

"""
Business layer for retrieving stacks by category id as a dictionary

Jaco Koekemoer
2023-04-27
"""
class RetrieveStacksByCategoryIdDict:

    def run(self, category_id):
        # Retrieve all categories via the DAO
        retrieve_stack = sd.RetrieveActiveStacksByCategoryIdDAO()
        stacks = retrieve_stack.run(category_id)

        # Convert data for front-end display
        stack_dictionary = dict()
        stack_dictionary[sc.StackConstant.SELECT_STACK.value] = -1
        for stack in stacks:
            stack_dictionary[stack[1]] = stack[0] # description: id
        return stack_dictionary


"""
A class for updating the hidden value of a given stack id to true

Jaco Koekemoer
2024-07-28
"""
class HideStack:

    def run(self, stack_id):
        hide_stack_dao = sd.HideStackDAO()
        hide_stack_dao.run(stack_id)


"""
A class for updating the hidden value for all stacks to be reviewed to false

Jaco Koekemoer
2024-07-28
"""
class ShowAllActiveStacks:

    def run(self):
        # Show active scheduled stacks
        show_all_active_scheduled_stacks = sd.ShowAllActiveScheduledStacksDAO()
        show_all_active_scheduled_stacks.run()

        # Show active daily stacks
        show_all_active_daily_stacks = sd.ShowAllActiveDailyStacksDAO()
        show_all_active_daily_stacks.run()
