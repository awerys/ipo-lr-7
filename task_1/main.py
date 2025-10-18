 # Создаем список книг
books = [
    {"title": "Портрет Дориана Грея", "author": "Уайльд", "year": 1860},
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"title": "Идиот", "author": "Достоевский", "year": 1869},
    {"title": "1984", "author": "Оруэлл", "year": 1949},
    {"title": "Трое", "author": "Маяковский", "year": 1900}
]
# Выводим информацию о каждой книге
for i in range(5):
    print(f"Книга {i+1}")
    print(f"Название: {books[i]['title']}, Автор: {books[i]['author']}, -{books[i]['year']}")
    print() 
