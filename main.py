class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict= {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booklist:
            print("Sorry, we don't have the book!")
        else:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("Lender Book database has been updated")
            else:
                print(f"The Book is in use by: {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print(f"The Book '{book}' has been added!")

    def returnBook(self, book):
        if book not in self.lendDict.keys():
            print('This Book was not borrowed')
        else:
            self.lendDict.pop(book)
            print(f"Book return successful")

def main():
    books = Library(['Harry Potter', 'The Hunger Games', 'The Odyseey', 'Percy Jackson', 'Metamorphorsis', 'Romeo and Juliet', 'Pride and Prejudice', 'Hamlet'], "Readlings Library")
    while True:
        print(f"Welcome to {books.name}. Enter your Choice to continue")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")

        user_choice = input("enter choice: ")
        if user_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid option")
            continue
        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            books.displayBooks()
        elif user_choice==2:
            book = input("Enter Book name: ")
            user = input("Enter user name: ")
            books.lendBook(user, book)
        elif user_choice == 3:
            book = input("enter a book: ")
            books.addBook(book)
        elif user_choice == 4:
            book = input("enter book name: ")
            books.returnBooks(book)
        elif user_choice == 5:
            print("Thank you for visiting!")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()