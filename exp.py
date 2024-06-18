class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = {}

    def display_books(self):
        if not self.books:
            print("No books in the library right now.")
        else:
            print("Books currently available:")
            for book, availability in self.books.items():
                print(f"{book} - {'Available' if availability else 'Not Available'}")

    def add_book(self, book_name):
        if book_name in self.books:
            print(f"{book_name} is already in the library.")
        else:
            self.books[book_name] = True
            print(f"{book_name} has been added to the library.")

    def lend_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name]:
                self.books[book_name] = False
                print(f"You have borrowed {book_name}. Please return it within 30 days.")
            else:
                print(f"Sorry, {book_name} is currently not available.")
        else:
            print(f"{book_name} is not in the library catalog.")

    def return_book(self, book_name):
        if book_name in self.books:
            if not self.books[book_name]:
                self.books[book_name] = True
                print(f"Thank you for returning {book_name}.")
            else:
                print(f"{book_name} is already available in the library.")
        else:
            print(f"{book_name} is not in the library catalog.")

    def delete_book(self, book_name):
        if book_name in self.books:
            del self.books[book_name]
            print(f"{book_name} has been deleted from the library catalog.")
        else:
            print(f"{book_name} is not in the library catalog.")

# Example usage:
if __name__ == "__main__":
    library = Library("My Library")

    while True:
        print("\nWelcome to", library.library_name)
        print("1. Display all books")
        print("2. Add a book")
        print("3. Lend a book")
        print("4. Return a book")
        print("5. Delete a book")
        print("0. Exit")

        choice = input("Enter choice (0-5): ")

        if choice == '0':
            print("Exiting the library management system.")
            break
        elif choice == '1':
            library.display_books()
        elif choice == '2':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book to lend: ")
            library.lend_book(book_name)
        elif choice == '4':
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
        elif choice == '5':
            book_name = input("Enter the name of the book to delete: ")
            library.delete_book(book_name)
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")
