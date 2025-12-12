from pymongo import MongoClient

client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

walter = db.laureates.find_one({
    'firstname': 'Walter',
    'surname': 'Kohn'
})
print(walter)

california = db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California'
})
print(california)

san_francisco = db.laureates.count_documents({
    'prizes.affiliations.city': 'San Francisco, CA'
})
print(san_francisco)

no_country = db.laureates.count_documents({
    'bornCountry':{
        '$exists': False
    }
})
print(no_country)

qtd = db.laureates.count_documents({})
print(qtd)

qnt_prizes = db.laureates.count_documents({
    'prizes': {
        '$exists': True
    }
})
print(qnt_prizes)

prize_contain = db.laureates.count_documents({
    'prizes.0':{
        '$exists': True
    }
})
print(prize_contain)

prize_multg = db.laureates.count_documents({
    'prizes.1':{
        '$exists': True
    }
})