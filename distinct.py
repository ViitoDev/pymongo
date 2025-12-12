from pymongo import MongoClient

client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

print(db.laureates.distinct('gender'))
print(db.laureates.count_documents({'gender': 'female'}))
print(db.laureates.count_documents({'gender': 'male'}))
print(db.laureates.count_documents({'gender': 'org'}))

print(db.laureates.distinct('prizes.category'))

print(db.laureates.distinct(
    'prizes.category',
    {'prizes.share': '4'} 
))

print(db.laureates.distinct(
    'category',
    {'laureates.share': '4'}
))

print(db.laureates.distinct(
    'prizes.category',
    {'prizes.1': {
        '$exists': True
    }}
))