import uuid


class Book:
    def __init__(self, title, author):
        self.id = uuid.uuid7()
        self.title = title
        self.author = author
        self.favourite = False


class FavouriteBooks:
    def __init__(self):
        self.favourite_ids = set()

    def add(self, book_id):
        if book_id not in self.favourite_ids:
            self.favourite_ids.add(book_id)

    def remove(self, book_id):
        if book_id in self.favourite_ids:
            self.favourite_ids.remove(book_id)

    def is_favourite(self, book_id):
        return book_id in self.favourite_ids


class BookStore:
    def __init__(self, favourites_manager=FavouriteBooks()):
        self.books = {}
        self.max_title_length = 150
        self.max_author_length = 100
        self.favourites_manager = favourites_manager

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
        self.books[book.id] = book

        return book

    def get_books(self):
        return list(self.books.values())

    def toggle_favourite(self, book_id):
        if book_id in self.books:
            # Check current favourite status and toggle it
            is_favourite = self.favourites_manager.is_favourite(book_id)
            if is_favourite:
                self.favourites_manager.remove(book_id)
            else:
                self.favourites_manager.add(book_id)

            # sync the favourite status on the book object (for UI purposes)
            book = self.books[book_id]
            book.favourite = self.favourites_manager.is_favourite(book_id)

        return book
