import os

FILE_PATH = "books.txt"

class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def __str__(self):
        return f"BOOK|{self.title}|{self.author}|{self.year}|{self.genre}"

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_num):
        super().__init__(title, author, year)
        self.issue_num = issue_num

    def __str__(self):
        return f"MAGAZINE|{self.title}|{self.author}|{self.year}|{self.issue_num}"

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item_type):
        title = input(f"Enter {item_type.lower()} title: ").strip()
        author = input(f"Enter {item_type.lower()} author: ").strip()
        year = input(f"Enter {item_type.lower()} year: ").strip()

        if item_type == "book":
            genre = input("Enter book genre: ").strip()
            book = Book(title, author, year, genre)
            addItemToFile(str(book))
            self.items.append(book)
        elif item_type == "magazine":
            issue_num = input("Enter magazine issue number: ").strip()
            magazine = Magazine(title, author, year, issue_num)
            addItemToFile(str(magazine))
            self.items.append(magazine)


    def list_items(self):
        print("=====Items=====")
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()

            if not lines:
                print("No records found!")
            else:
                for line in lines:
                    print(line.strip())

    def search(self):
        keyword = input("Please enter keyword to search: ").strip().lower()

        with open(FILE_PATH, "r") as file:
            lines = file.readlines()

            # keyword = lib
            if not lines:
                print("No records found!")
            else:
                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line)


# Helper functions
def display_options():
    print("""
=====Library Menu====
1. Add a Book
2. Add a Magazine
3. List all Items
4. Search by Title
5. Exit
    """)

# Creates the file if file does not exist
def fileCheck():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            pass

def addItemToFile(item):
    with open(FILE_PATH, "a") as file:
        file.write(f"{item}\n")

def main():
    fileCheck()
    library = Library()

    while True:
        display_options()
        try:
            option = int(input("Please select an option: ").strip())

            if option == 1:
                library.add_item("book")
            elif option == 2:
                library.add_item("magazine")
            elif option == 3:
                library.list_items()
            elif option == 4:
                library.search()
            elif option == 5:
                break;
            else:
                print("Please select a valid option (1-5)")
        except ValueError:
            print("Please select a valid option (1-5)")

main()