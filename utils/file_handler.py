# utils/file_handler.py

from __future__ import annotations

from models.book import Book


def save_books(filename: str, books: list[Book]) -> None:
    """Save books to a CSV-like text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for book in books:
                f.write(
                    f"{book.isbn},{book.title},{book.author},{book.category},"
                    f"{book.publication_year},{book.is_available}\n"
                )
    except OSError:
        print("Error saving file")


def load_books(filename: str) -> list[Book]:
    """Load books from a CSV-like text file."""
    books: list[Book] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                isbn, title, author, category, year, available = line.split(",")
                books.append(
                    Book(isbn, title, author, category, int(year), available == "True")
                )
    except FileNotFoundError:
        print("Data file not found. Starting empty.")
    return books