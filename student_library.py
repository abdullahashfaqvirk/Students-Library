class Library:
    def __init__(self, booksList):
        self.books = booksList

    @staticmethod
    def studLibrary():
        print("\t\t\t\t\tWelcome to Student Library")

    def getDetails(self):
        print("Rules and Regulations:")
        print("01. For 10 Days, fees per book is Rs.100")
        print("02. Any Damage to Book may charge fine of Rs.50")
        print("03. After 10 days, Rs.5 are fined as extra charges.")
        print("For More Detaisls: www.studentlibrary.com")

    def availableBooks(self):
        print("Available Books:")
        for index, i in enumerate(self.books):
            print(f"{index+1}: {i}")

    def borrowBook(self, bookNum):
        if bookNum < len(self.books):
            print(f"Book '{self.books[bookNum]}' is awarded. Please return in 10 Days!")
            self.books.pop(bookNum)
        else:
            print("Unavailable...")

    def returnBook(self, book):
        print(f"Book '{book}' is received!\nThank You!")
        self.books.append(book)


class Student(Library):
    def borrowBook(self):
        number = int(input("Enter Book Number to Borrow: "))
        super().borrowBook(number-1)

    def returnBook(self):
        name = input("Enter Book Name you want to Return: ")
        super().returnBook(name)
    
    def donateBook(self):
        name = input("Enter Book Name for Donation: ")
        super().returnBook(name)


if __name__ == "__main__":
    line = "-" * 110

    booksList = [
        "Inside the Machine | Author: Jon Stokes ",
        "Structure and Interpretation of Computer Programs | Author: Harold Abelson",
        "Design Patterns | Author: Erich Gamma",
        "The Hidden Language of Computer Hardware and Software | Author: Charles Petzold",
        "Cracking the Coding Interview | Authors: Gayle Laakmann McDowell",
        "Programming Pearls | Authors: Jon Bentley",
        "The Fundamentals of Software | Author: Max Kanat-Alexander",
        "Think Like a Programmer | Author: V. Anton Spraul"
    ]

    lib = Library(booksList)
    stu = Student(booksList)

    print(line)
    lib.studLibrary() # Welcome Message
    print(line)
    name = input("Enter Name: ")
    id = input("Enter ID: ")
    print(line)

    print("Choose an Option:")
    print("1. Available Books in Library")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Donate the Book")
    print("5. Rules and Regulations")
    print("6. Exit")

    while True:
        try:
            print(line)
            num = int(input("Enter Option Number: "))
            print(line)
            if num == 1:
                stu.availableBooks()
            elif num == 2:
                stu.borrowBook()
            elif num == 3:
                stu.returnBook()
            elif num == 4:
                stu.donateBook()
            elif num == 5:
                stu.getDetails()
            elif num == 6:
                print("Thank You!\n", line)
                break
            else:
                print("Invalid Input!")
        except:
            print("Error Found!")
