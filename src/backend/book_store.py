import uuid


class Book:
    def __init__(self, title, author):
        self.id = uuid.uuid7()
        self.title = title
        self.author = author


class BookStore:
    def __init__(self):
        self.books = []
        self.max_title_length = 150
        self.max_author_length = 100

    def add_book(self, title, author):
        if not title:
            raise ValueError("Title is required")
        if not author:
            raise ValueError("Author is required")
        if len(title) > self.max_title_length:
            raise ValueError(f"Title must be at most {self.max_title_length} characters long")
        if len(author) > self.max_author_length:
            raise ValueError(f"Author must be at most {self.max_author_length} characters long")

        book = Book(title=title, author=author)
        self.books.append(book)

        return book

    def get_books(self):
        return self.books
