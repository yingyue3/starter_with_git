from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['Test']

##huasof
name = db.customers


results = artists.aggregate([
    
    {"$project": {"_id":1, "artist_id":1, "name":1, "num_tracks":{"$size":"$tracks"}}
        
    },
    {"$match": {"num_tracks": {"$gt":0}}}
    
])


for i in results:
    print(i)
