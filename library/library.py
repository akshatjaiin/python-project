class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")

        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("ID\tTitle\t\t\tAuthor")
        print("-----------------------------------------------")
        for book in self.books:
            print(f"{book.id}\t{book.title:<20}\t{book.author:<20}")

    def search_book(self):
        book_id = int(input("Enter Book ID to search: "))
        for book in self.books:
            if book.id == book_id:
                print("Book found:")
                print(f"ID: {book.id}\nTitle: {book.title}\nAuthor: {book.author}")
                return
        print("Book not found.")

    def delete_book(self):
        book_id = int(input("Enter Book ID to delete: "))
        for i, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[i]
                print("Book deleted successfully.")
                return
        print("Book not found.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            library.search_book()
        elif choice == 4:
            library.delete_book()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
