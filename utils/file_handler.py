# utils/file_handler.py

# File này chịu trách nhiệm LƯU/ĐỌC dữ liệu sách ra file text.
# (Thuộc đề bài: "Lưu danh sách sách ra file" và "Đọc danh sách sách từ file" để lần chạy sau vẫn còn dữ liệu)

from __future__ import annotations
# Cho phép type hint (list[Book]) hoạt động ổn định ngay cả khi Book được import/được đánh giá muộn.
# (Thuộc đề bài: không bắt buộc nghiệp vụ, nhưng là kỹ thuật Python giúp code rõ ràng)

from models.book import Book
# Import lớp Book để:
# - Khi load file: tạo đối tượng Book từ dữ liệu đọc được
# - Khi save file: lấy thuộc tính của từng Book để ghi ra file
# (Thuộc đề bài: "Quản lý đối tượng Book" + "Lưu/đọc dữ liệu")


def save_books(filename: str, books: list[Book]) -> None:
    """Save books to a CSV-like text file."""
    # Hàm lưu danh sách books xuống filename.
    # (Thuộc đề bài: "Lưu dữ liệu" / "Persist data")

    try:
        # Dùng try để nếu gặp lỗi I/O (không ghi được file, sai đường dẫn, không có quyền) thì không làm chương trình bị crash.
        # (Thuộc đề bài: "Xử lý ngoại lệ / error handling")

        with open(filename, "w", encoding="utf-8") as f:
            # Mở file ở chế độ ghi đè ("w"). Mỗi lần save sẽ thay toàn bộ nội dung file bằng dữ liệu mới.
            # encoding="utf-8" để lưu tiếng Việt/ký tự đặc biệt.
            # (Thuộc đề bài: "Ghi file")

            for book in books:
                # Duyệt từng cuốn sách trong danh sách để ghi 1 dòng.
                # (Thuộc đề bài: "Lưu danh sách nhiều sách")

                # Quy ước định dạng mỗi dòng: isbn,title,author,category,publication_year,is_available
                # Lưu ý: nếu title/author/category có dấu phẩy "," thì sẽ phá định dạng (bị tách cột sai khi load).
                # (Thuộc đề bài: "Thiết kế định dạng lưu trữ dữ liệu")
                f.write(
                    f"{book.isbn},{book.title},{book.author},{book.category},"
                    f"{book.publication_year},{book.is_available}\n"
                )
                # \n để xuống dòng, đảm bảo mỗi Book nằm trên 1 dòng tách biệt.
                # is_available lưu dạng True/False để lần sau load lên biết sách đang Available hay Borrowed.
                # (Thuộc đề bài: "Lưu trạng thái mượn/trả")

    except OSError:
        # Bắt lỗi liên quan hệ điều hành/I/O (permission denied, path not found, v.v.)
        # (Thuộc đề bài: "Xử lý lỗi khi thao tác file")
        print("Error saving file")
        # Thông báo cho người dùng biết save thất bại.
        # (Thuộc đề bài: "In thông báo lỗi")


def load_books(filename: str) -> list[Book]:
    """Load books from a CSV-like text file."""
    # Hàm đọc danh sách sách từ file và trả về list[Book].
    # (Thuộc đề bài: "Đọc dữ liệu từ file khi chương trình khởi động")

    books: list[Book] = []
    # Tạo danh sách rỗng để chứa kết quả đọc được.
    # (Thuộc đề bài: "Quản lý danh sách sách")

    try:
        # Dùng try để nếu file chưa tồn tại thì xử lý nhẹ nhàng (bắt đầu danh sách rỗng).
        # (Thuộc đề bài: "Xử lý ngoại lệ / file not found")

        with open(filename, "r", encoding="utf-8") as f:
            # Mở file ở chế độ đọc.
            # (Thuộc đề bài: "Đọc file")

            for line in f:
                # Đọc từng dòng trong file (mỗi dòng là 1 cuốn sách đã lưu).
                # (Thuộc đề bài: "Đọc danh sách nhiều sách")

                line = line.strip()
                # Xóa ký tự xuống dòng và khoảng trắng thừa ở đầu/cuối.
                # (Thuộc đề bài: "Tiền xử lý dữ liệu")

                if not line:
                    # Nếu dòng rỗng thì bỏ qua để tránh lỗi khi split.
                    # (Thuộc đề bài: "Đảm bảo dữ liệu hợp lệ")
                    continue

                # Tách dữ liệu theo đúng quy ước đã lưu ở save_books.
                # (Thuộc đề bài: "Đọc theo định dạng đã thiết kế")
                isbn, title, author, category, year, available = line.split(",")

                # Chuyển year từ chuỗi -> int, available từ chuỗi "True"/"False" -> boolean.
                # (Thuộc đề bài: "Đúng kiểu dữ liệu cho Book")
                books.append(
                    Book(isbn, title, author, category, int(year), available == "True")
                )
                # Thêm Book vừa tạo vào danh sách.
                # (Thuộc đề bài: "Tạo đối tượng Book từ dữ liệu đọc được")

    except FileNotFoundError:
        # Nếu file chưa tồn tại (chưa từng save lần nào), bắt đầu với danh sách rỗng.
        # (Thuộc đề bài: "Nếu chưa có file dữ liệu thì chương trình vẫn chạy")
        print("Data file not found. Starting empty.")

    return books
    # Trả về danh sách Book để LibraryManager dùng làm dữ liệu ban đầu.
    # (Thuộc đề bài: "Khởi tạo dữ liệu khi chạy chương trình")