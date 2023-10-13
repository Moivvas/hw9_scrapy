from mongodb_module.models import Author, Quote
from mongoengine import *

connect(host="mongodb+srv://moivvas:password@moivvas.am1rhde.mongodb.net/hw8_1?retryWrites=true&w=majority")

def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [(quote.quote, quote.author.fullname) for quote in quotes]
    else:
        return []

def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [(quote.quote, quote.author.fullname) for quote in quotes]

def search_quotes_by_tags(tags_list):
    quotes = Quote.objects(tags__in=tags_list)
    return [(quote.quote, quote.author.fullname) for quote in quotes]

if __name__ == '__main__':
    
    while True:
        command = input("Введіть команду ('name: Steve Martin' або 'tags: life,live'): ").strip()

        if command == 'exit':
            print("Завершення роботи програми.")
            break

        parts = command.split(': ')
        if len(parts) != 2:
            print("Невірний формат команди(моживо, ви забули пробіл після двокрапки). Спробуйте ще раз.")
            continue

        action, value = parts
        if action == 'name':
            quotes = search_quotes_by_author(value)
        elif action == 'tag':
            quotes = search_quotes_by_tag(value)
        elif action == 'tags':
            tags_list = value.split(',')
            quotes = search_quotes_by_tags(tags_list)
        else:
            print("Невідома команда. Спробуйте ще раз.")
            continue

        if quotes:
            for quote, author in quotes:
                print(f"Цитата: {quote}\nАвтор: {author}\n")
        else:
            print("Цитати не знайдено.")
