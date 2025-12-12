from pymongo import MongoClient

client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

print(db.laureates.count_documents({
    'prizes': {
        'category': 'physics',
        'share': '1'
    }
}))

print(db.laureates.count_documents({
    'prizes':{
        '$elemMatch':{
            'category': 'physics',
            'share': '1'
        }
    }
}))

print(db.laureates.count_documents({
    'prizes':{
        '$elemMatch':{
            'category': 'physics',
            'share': '1',
            'year':{'$lt': '1945'}
        }
    }
}))

