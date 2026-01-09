# main.py

from models.book import Book
from services.library_manager import LibraryManager

def menu():
    print("\n=== Library Management ===")
    print("1. Add book")
    print("2. Display books")
    print("3. Search book")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Statistics")
    print("0. Exit")

def main():
    manager = LibraryManager("data/books.txt")

    while True:
        menu()
        choice = input("Choose: ")

        try:
            if choice == "1":
                isbn = input("ISBN: ")
                title = input("Title: ")
                author = input("Author: ")
                category = input("Category: ")
                year = int(input("Year: "))
                manager.add_book(Book(isbn, title, author, category, year))

            elif choice == "2":
                for book in manager.books:
                    print(book)

            elif choice == "3":
                key = input("Keyword: ")
                for book in manager.search_book(key):
                    print(book)

            elif choice == "4":
                manager.borrow_book(input("ISBN: "))

            elif choice == "5":
                manager.return_book(input("ISBN: "))

            elif choice == "6":
                print(manager.books_by_category())

            elif choice == "0":
                manager.save()
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()