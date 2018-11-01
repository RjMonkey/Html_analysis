# import pymongo
# client = pymongo.MongoClient(host='localhost', port=27017)
# db_list = client.database_names()
#
# my_db = client["test"]
# my_col = my_db["test_mongodb"]
# my_list = [
#     {"name": "Taobao", "alexa": "100", "url": [{"name": "Github", "alexa": "109", "url": "https://www.github.com"}]},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"}
#
# ]
#
# x = my_col.insert_many(my_list)
# print(x.inserted_ids)
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
#
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# from bs4 import BeautifulSoup
#
#
# soup = BeautifulSoup(html_doc)
# first_link = soup.a
# first_link
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#
# first_link.find_all_next()
# # [u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',
# #  u';\nand they lived at the bottom of a well.', u'\n\n', u'...', u'\n']
#
# first_link.find_all_next()
# # <p class="story">...</p>
# pass


list = [1, 2, 3, 4]
print(list)
list.remove(3)
print(list)
print(list[len(list) - 1])
