import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db_list = client.database_names()

my_db = client["test"]
my_col = my_db["test_mongodb"]
my_list = [
    {"name": "Taobao", "alexa": "100", "url": [{"name": "Github", "alexa": "109", "url": "https://www.github.com"}]},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"}

]

x = my_col.insert_many(my_list)
print(x.inserted_ids)
