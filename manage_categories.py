import qcards_db as qcards_db
import MySQLdb as mysql
import qcards_util as qu

class Category:

    def __init__(self, id, description, active):
        self.id = id
        self.description = description
        self.active = active

    def convert_to_list(self):
        return [ self.id, self.description, self.active ]

class AddCategory:

    def run(self, description, active):
        # Prepare SQL
        sql = "insert into t_category(description, active, create_date, last_modified_date) values('{:s}', {}, current_timestamp(), current_timestamp());".format(description, active);
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);


class UpdateCategory:

    def run(self, id, description, active):
        # Prepare SQL
        sql = "update t_category set description = '{:s}', active = {} where id = {:d};".format(description, active, id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteQuery()
        execute_query.execute(sql);

class RetrieveCategoryById:

    def run(self, id):
        # Prepare SQL
        sql = "select id, description, active from t_category where id = {:d};".format(id)
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        return execute_query.execute(sql);

class RetrieveAllCategories:

    def run(self):
        # Prepare SQL
        sql = "select id, description, active from t_category;"
        print(sql);

        # Run the query
        execute_query = qcards_db.QCardsExecuteSelectQuery()
        categories = execute_query.execute(sql);
        return self.convert_active(categories)

    def convert_active(self, categories):
        converted_categories = ()
        qcards_util = qu.QCardsUtil()
        for category in categories:
            converted_category = (category[0], category[1], qcards_util.convert_tinyint_to_boolean(category[2]))
            converted_categories = converted_categories + (converted_category,) # Building up a tuple of tuples
        return converted_categories

class AdaptRecordsToCategories:

    def run(self, records):
        categories = []
        for row in records:
            id = row[0]
            description = row[1]
            active = row[2]
            category = Category(id, description, active)
            categories.append(category);
        return categories

class PrintCategories:

    def run(self, categories):
        for category in categories:
            print("{} {} {}".format(category.id, category.description, category.active))

"""
Test code
"""

"""
# Test adding multiple categories
for n in range(1, 100):
    category_description = f'category{n}'
    add_category = AddCategory()
    add_category.run(category_description, True)
"""

"""
# Test adding multiple categories
categories = ['Java', 'Python', 'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'JQuery']
for category in categories:
        add_category = AddCategory()
        add_category.run(category, True)
"""

"""
# Test adding a single category
add_category = AddCategory()
add_category.run("HTML", True)
"""

"""
# Test updating a category
update_category = UpdateCategory()
update_category.run(3, "Python Update", False);
"""

"""
# Test retrieving all categories
retrieve_category = RetrieveCategoryById()
records = retrieve_category.run(2);
print(type(records[0]))
print(records[0])
"""

"""
# Test retrieving categories by id
retrieve_categories = RetrieveAllCategories()
records = retrieve_categories.run();
#print(records)
adapt_records_to_categories = AdaptRecordsToCategories()
adapted_records = adapt_records_to_categories.run(records)
#print(adapted_records)
print_categories = PrintCategories()
print_categories.run(adapted_records)
"""

"""
# Test convert to list on Category
category = Category(1, "Test Category", True)
print(category.convert_to_list())
"""
