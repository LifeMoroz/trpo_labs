import datetime

from pymongo import MongoClient

# docker run -p 27017:27017 --name mongo1 mongo
client = MongoClient('localhost', 27017)
db = client.test_database
posts = db.posts
post = {"pc": "1",
        "configuration": {
            'description': "My!",
            'allow_internet': True
        },
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }
post = posts.insert_one(post)
print(post.inserted_id)
print(posts.find_one({'_id': post.inserted_id}))
for item in posts.find():
    print(item)
