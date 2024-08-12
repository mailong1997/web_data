import pymongo
connection_str="mongodb+srv://mailongkf:22LCNuBgzPZksiMX@cluster0-mailong.4lpjsis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0-MaiLong"
client = pymongo.MongoClient(connection_str)
db = client["test-database"]
print(client.list_database_names()) 