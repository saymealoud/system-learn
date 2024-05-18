from pymongo import MongoClient

# 使用连接字符串直接进行身份验证
uri = "mongodb://root:123456@localhost:27017/"
client = MongoClient(uri)

# 导出 client 供其他文件使用
