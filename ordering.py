from pymongo import MongoClient

client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

cursor = db.prizes.find(
    {'category': 'physics'},
    {'year'},
    sort=[('year', 1)]
)
print([doc['year'] for doc in cursor][:5])

cursor2 = db.prizes.find(
    {'category': 'physics'},
    {'year'},
    sort=[('year', -1)]
)
print([doc['year'] for doc in cursor2][:5])

for doc in db.prizes.find(
    {'year': {'$gt': '1966', '$lt': '1970'}},
    ['category', 'year'],
    sort=[('year', 1), ('category', -1)]):
    print('{year} {category}'.format(**doc))
