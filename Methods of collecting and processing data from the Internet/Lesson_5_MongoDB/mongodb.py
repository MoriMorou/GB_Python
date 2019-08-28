from pymongo import MongoClient
import pprint

client = MongoClient("mongodb+srv://mori:Morou4774@cluster0-t3zhj.gcp.mongodb.net/GBdb?retryWrites=true&w=majority")
db = client['lesson']
lesson = db.lesson
lesson.drop()
lesson.insert_many([{'name': "test abc",
                   'size': 2000,
                    'author': "Mike Dowson"},
                    {'name': "Name space",
                     'size': 1500,
                    'author': "Peter Pan"}
                     ])
print("Added new information. The total account is :", lesson.count_documents({}))
print('\n')

doc_data = {
     "name": "One more document",
     "author": {"fullname": "Sergie",
                "age": 18,
                "address":
                    {'street': "City Center°",
                     'city': 'Moscow°'}},
                "created": "01.12.1982",
                "genres": ["philosophy", "action", "psy"]}

lesson.insert_one(doc_data)

print("All data in a database")
print("the total account is :", lesson.count_documents({}))
all_data = list(lesson.find())
pprint.pprint(all_data)
print('\n')

print("Only part of information from the DB:")
find_one_data = lesson.find_one({'author.address.city': 'Moscow'})
pprint.pprint(find_one_data)
print('\n')

doc_data_updates = {"author": {"fullname": "Mark"}}
lesson.update_one({"name": "One more document"}, {'$set': doc_data_updates})

print("Only part of information from the DB after update:")
find_one_data = lesson.find_one({"name": "One more document"})
pprint.pprint(find_one_data)
print('\n')

lesson.delete_one({'name': "test abc"})
print("All data in the database after delete")
print("the total account is :", lesson.count_documents({}))
all_data_after_delete = list(lesson.find())
pprint.pprint(all_data_after_delete)