import qcards_db as qcards_db
import MySQLdb as mysql
import qcards_util as qu

class Stack:

    def __init__(self, id, description, active, source, category_id, last_view_date, next_view_date):
        self.id = id
        self.description = description
        self.active = active
        self.source = source
        self.category_id = category_id
        self.last_view_date = last_view_date
        self.next_view_date = next_view_date

    def convert_to_list(self):
        return [ self.id, self.description, self.active, self.source, self.category_id, self.last_view_date, self.next_view_date ]

class AddStack:

    def run(self, description, active, source, category_id):
        # Prepare SQL
        sql = "insert into t_stack(description, active, source, category_id, next_view_date, create_date) \
            values('{:s}', {}, '{:s}', {:d}, '{:%Y-%m-%d}', current_timestamp());".format(description, active, source, category_id, next_view_date);
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);


class UpdateStack:

    def run(self, id, description, active, source, category_id, last_view_date, next_view_date):
        # Prepare SQL
        sql = "update t_stack  \
            set description = '{:s}', \
            active = {}, \
            source = '{:s}', \
            category_id = {:d} \
            last_view_date = '{:%Y-%m-%d}', \
            next_view_date = '{:%Y-%m-%d}' \
            where id = {:d};".format(description, active, source, category_id, last_view_date, next_view_date, id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);

class RetrieveStackById:

    def run(self, id):
        # Prepare SQL
        sql = "select id, description, active, source, category_id, last_view_date, next_view_date from t_stack where id = {:d};".format(id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql);

class RetrieveAllStacks:

    def run(self):
        # Prepare SQL
        sql = "select id, description, active, source, category_id, last_view_date, next_view_date from t_stack;"
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        stacks = execute_query.execute(sql);
        return self.convert_active(stacks)

    def convert_active(self, stacks):
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            converted_stack = (stack[0], stack[1], qcards_util.convert_tinyint_to_boolean(stack[2]), stack[3], stack[4])
            converted_stacks = converted_stacks + (converted_stack,) # Building up a tuple of tuples
        return converted_stacks

class RetrieveStackByCategoryId:

    def run(self, category_id):
        # Prepare SQL
        sql = "select id, description, active, source, category_id, last_view_date, next_view_date from t_stack where category_id = {:d};".format(category_id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        stacks = execute_query.execute(sql);
        return self.convert_active(stacks)

    def convert_active(self, stacks):
        converted_stacks = ()
        qcards_util = qu.QCardsUtil()
        for stack in stacks:
            converted_stack = (stack[0], stack[1], qcards_util.convert_tinyint_to_boolean(stack[2]), stack[3], stack[4])
            converted_stacks = converted_stacks + (converted_stack,) # Building up a tuple of tuples
        return converted_stacks

class AdaptRecordsToCategories:

    def run(self, records):
        stacks = []
        for row in records:
            id = row[0]
            description = row[1]
            active = row[2]
            source = row[3]
            category_id = row[4]
            stack = Stack(id, description, active, source, category_id)
            stacks.append(stack);
        return stacks

class PrintCategories:

    def run(self, stacks):
        for stack in stacks:
            print("{} {} {}".format(stack.id, stack.description, stack.active))

"""
Test code
"""

"""
# Test adding multiple stacks
for n in range(1, 100):
    stack_description = f'stack{n}'
    add_stack = AddStack()
    add_stack.run(stack_description, True)
"""

"""
# Test adding multiple stacks
stacks = ['Java', 'Python', 'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'JQuery']
for stack in stacks:
        add_stack = AddStack()
        add_stack.run(stack, True)
"""

"""
# Test adding a single stack
add_stack = AddStack()
add_stack.run("HTML", True)
"""

"""
# Test updating a stack
update_stack = UpdateStack()
update_stack.run(3, "Python Update", False);
"""

"""
# Test retrieving all stacks
retrieve_stack = RetrieveStackById()
records = retrieve_stack.run(2);
print(type(records[0]))
print(records[0])
"""

"""
# Test retrieving stacks by id
retrieve_stacks = RetrieveAllCategories()
records = retrieve_stacks.run();
#print(records)
adapt_records_to_stacks = AdaptRecordsToCategories()
adapted_records = adapt_records_to_stacks.run(records)
#print(adapted_records)
print_stacks = PrintCategories()
print_stacks.run(adapted_records)
"""

"""
# Test convert to list on Stack
stack = Stack(1, "Test Stack", True)
print(stack.convert_to_list())
"""
