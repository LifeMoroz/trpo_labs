import datetime

from pymongo import MongoClient

# docker run -p 27017:27017 --name mongo1 mongo
client = MongoClient('localhost', 27017)
db = client.test_database
pcs = db['PC']
confs = db['Confs']
adapters = db['Adapters']

pcs.drop()
pc1 = pcs.insert_one({'name': 'ПБД', 'year': 1}).inserted_id
pc2 = pcs.insert_one({'name': 'СПАСОИУ', 'year': 1, }).inserted_id

confs.drop()
confs.insert([{'name': '7', 'year': 1, 'department': '5', 'active': True},
              {'name': '8', 'year': 1, 'department': '5', 'active': True}])

adapters.drop()
adapters.insert([{'pc': pc1}, {'pc': pc2}])
for collection in [pcs, adapters, confs]:
    print(collection.name)
    for r in collection.find():
        print(r)

confs = db.confs
post = {"pc": "1",
        "configuration": {
            'description': "My!",
            'allow_internet': True
        },
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }
post2 = {"pc": "2",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

post = confs.insert_one(post)
confs.find_one({'_id': post.inserted_id})
confs.find_one_and_replace({'_id': post.inserted_id}, post2)
confs.update({'pc': 2}, {'$push': {'configuration': {'allow_internet': False}}})
confs.update({'pc': 2}, {'$set': {"date": datetime.datetime.utcnow()}})
confs.update({'pc': 2}, {'$unset': {"tags": ''}})
confs.remove({'pc': 2})

for item in confs.find():
    print(item)
