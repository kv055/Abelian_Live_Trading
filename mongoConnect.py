import pymongo

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
connectionStr = "mongodb+srv://HarterMongo:BehinderterMongo@cluster0.ojn4q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionStr,serverSelectionTimeoutMS=5000)

#Choosing the Database and the Collection
database = client.AbelianCapital
collection = database.LogBook.find()

#Print out all Databases of the Account
# print(client.list_database_names())

#Put out all elements of the Collection
for x in collection:
    print(x)

