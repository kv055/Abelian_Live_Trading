import pymongo

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
connectionStr = "mongodb+srv://HarterMongo:BehinderterMongo@cluster0.ojn4q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionStr,serverSelectionTimeoutMS=5000)

#Choosing the Database and the Collection
database = client.AbelianCapital
collection = database.LogBook

#Data to insert
mydict = { "name": "John", "address": "Highway 37" }


try:
    collection.insert_one(mydict)
    print("Inserted successfully!!!")
except:  
    print("Could not connect to MongoDB")