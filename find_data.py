from pymongo import MongoClient

client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

print(db.laureates.count_documents({'gender': 'female'}))
print(db.laureates.count_documents({'gender': 'male'}))

print(db.laureates.count_documents({'diedCountry': 'France'}))

filter_doc =  {
    'diedCountry': 'France',
    'gender': 'female',
    'bornCity': 'Warsaw',
}

print(db.laureates.count_documents(filter_doc))
print(db.laureates.find_one(filter_doc))

filter_in = db.laureates.count_documents(
    {
        'diedCountry': {
            '$in':['France', 'USA']
        }
    }
)

print(filter_in)

filter_ne = db.laureates.count_documents(
    {
        'diedCountry': {
            '$ne': 'USA'
        }
    }
)

print(filter_ne)