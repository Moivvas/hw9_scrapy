import json

from models import Author, Quote

author_file_path = "D:/projects/pyhon web/m9//hw9_scrapy/hw9_scrapy/hw9/authors.json" #hw9_scrapy\hw9\authors.json
qoutes_file_path = "D:/projects/pyhon web/m9/hw9_scrapy/hw9_scrapy/hw9/qoutes.json"

def main_download_json():
    with open(author_file_path, "r", encoding="utf-8") as authors_file:
            authors_data = json.load(authors_file)

    with open(qoutes_file_path, "r", encoding="utf-8") as quotes_file:
        quotes_data = json.load(quotes_file)

    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

    for quote_data in quotes_data:
        author_fullname = quote_data['author']
        author = Author.objects(fullname=author_fullname).first()

        del quote_data['author']

        quote = Quote(**quote_data, author=author)
        quote.save()
        
def read_json_test():
    with open(author_file_path, "r", encoding="utf-8") as authors_file:
        bibi = json.load(authors_file)
        print(bibi)
        
if __name__ == '__main__':
        # main_download_json()
        read_json_test()


    


# from models import Author, Quote
# import json

# if __name__ == '__main__':
#     with open('authors.json', 'r') as json_a_file:
#         authors = json.load(json_a_file)
#     with open('authors.json', 'r') as json_q_file:
#         quotes = json.load(json_q_file)
#         for author in authors:
#             aut = author["fullname"]
#             aut = Author(fullname=author["fullname"], born_date=author["born_date"], born_location=author["born_location"], description=author["description"]).save()
#             for quote_i in quotes:
#                 if quote_i.get("author") == str(author["fullname"]):
#                     Quote(tags=quote_i["tags"], author=aut, quote=quote_i["quote"])


# from pymongo import *
# import json
# from mongoengine import connect

# connect(host="mongodb+srv://moivvas:password@moivvas.am1rhde.mongodb.net/hw8_1?retryWrites=true&w=majority")

# with open("authors.json", "r") as json_file:
#     authors = json.load(json_file)

# collection = Author._get_collection() 

# collection.insert_many(authors)

#     quotes = json.load(json_file)

# collection = Quote._get_collection()  

# collection.insert_many(quotes)
