import pymongo

# Tạo biến để lưu đường dẫn kết nối 
connection_str = "mongodb+srv://mailongkf:22LCNuBgzPZksiMX@cluster0-mailong.4lpjsis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0-MaiLong"
try:
    # Tạo kết nối đến MongoDB
    print("Connect done")
    client = pymongo.MongoClient(connection_str)
except Exception:
    # Nếu kết nối bị lỗi
    print("Error" + Exception)

# Truy cập vào cơ sở dữ liệu
"""
"title": "Học Văn",
"completed": true

"""

mydb = client["mydatabase"]
mycol = mydb["todolist"]
mydict = {"title": "a meetting with Khang", "completed" : False}

one_data = mycol.insert_one(mydict)
print(one_data)

for x in mycol.find():
    print("value: ", x)



