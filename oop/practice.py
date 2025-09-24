class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Title: {self.title}\n"
              f"Author: {self.author},\n"
              f"Year: {self.year}")


class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_info(self):
        print(f"Title: {self.title}\n"
              f"Author: {self.author},\n"
              f"Year: {self.year}\n"
              f"Genre: {self.genre}\n"
              f"---------------------")

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_num):
        super().__init__(title, author, year)
        self.issue_num = issue_num

    def get_info(self):
        print(f"Title: {self.title}\n"
              f"Author: {self.author},\n"
              f"Year: {self.year}\n"
              f"Issue Number: {self.issue_num}\n"
              f"---------------------")

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
            self.items.append(book)
        elif item_type == "magazine":
            issue_num = input("Enter magazine issue number: ").strip()
            magazine = Magazine(title, author, year, issue_num)
            self.items.append(magazine)

    def list_items(self):
        print("=====Items=====")
        for item in self.items:
            item.get_info()

    def search(self):
        keyword = input("Please enter keyword to search: ").strip().lower()

        for item in self.items:
            if keyword in item.title.lower():
                item.get_info()

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

def main():
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