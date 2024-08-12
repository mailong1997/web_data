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

mydb = client["mydatabase"]
mycol = mydb["todolist"]

delete_data = {"title": "a meetting with Lisa"}

mycol.delete_many({})
for x in mycol.find():
    print(x)




