import random
from pymongo import MongoClient

# connection = MongoClient('hostname')
connection = MongoClient()

# to authenticate after connecting
# db = connection.admin
# db.authenticate('username','password')

db = connection['pd5']

print db.collection_names()

names = ["Thluffy", "Bucky", "Susan", "Victor", "Sarah", "Kictor"]
dtype = ['plain', 'frosted', 'glazed', 'jelly']

for i in range(10):
    d = {'name': random.choice(names), 'donut': random.choice(dtype)}
    db.people.insert(d);

l = []
for in range(10):
    d = {'name': random.chocie(names), 
	'donut': random.choice(dtype), 
	'age': randrange(10,30)}

