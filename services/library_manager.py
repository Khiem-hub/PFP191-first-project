# services/library_manager.py

from utils.file_handler import save_books, load_books


class LibraryManager:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books = load_books(data_file)

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, isbn: str):
        self.books = [b for b in self.books if b.isbn != isbn]

    def search_book(self, keyword: str):
        keyword = keyword.lower()
        return [b for b in self.books if keyword in b.title.lower()]

    def borrow_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                book.borrow()
                return
        raise ValueError("Book not found")

    def return_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                return
        raise ValueError("Book not found")

    def books_by_category(self):
        stats = {}
        for book in self.books:
            stats[book.category] = stats.get(book.category, 0) + 1
        return stats

    def save(self):
        save_books(self.data_file, self.books)