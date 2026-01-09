# models/book.py

class Book:
    def __init__(self, isbn, title, author, category, publication_year, is_available=True):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._category = category
        self._publication_year = publication_year
        self._is_available = is_available

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def category(self):
        return self._category

    @property
    def publication_year(self):
        return self._publication_year

    @property
    def is_available(self):
        return self._is_available

    def borrow(self):
        if not self._is_available:
            raise ValueError("Book is already borrowed")
        self._is_available = False

    def return_book(self):
        self._is_available = True

    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"{self._isbn} | {self._title} | {self._author} | {self._category} | {self._publication_year} | {status}"