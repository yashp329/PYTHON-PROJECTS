class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks
  
    def displayAvailableBooks(self):
        print("Books available in this library are : ")
        for book in self.books:
            print("\t" + book)
            
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it with 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued by someone. Please wait until the book is returned.")
            return False    

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoy reading it.")

class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book 
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book 



if __name__ == "__main__":
    centraLibrary = Library(["Algorithms","Django","Clrs","Python Notes"])
    student =  Student()
    while(True):
        welcomemsg = '''\n====Welcome to the Central Library====
        Please choose an option
        1. List all the books
        2. Request a Book
        3. Add/Return a Book
        4. Exit the Library
        '''

        print(welcomemsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())    
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())    
        elif a == 4:
            print("Thanks for choosing central library have a great day ahead!")
            exit()
        else:
            print("Invalid Choice ")
