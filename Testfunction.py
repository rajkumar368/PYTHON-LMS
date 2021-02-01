# -*- coding: utf-8 -*-
import sys
from Library import Library
from User import Member
from catalog import Catalog  
from Librarian import Librarian         
library = Library({"the reader":[4,"bernhard schlink","120H",1995,218],"the secret garden":[3,"frances hodgson burnett","121H",1911,375],"number of stars":[5,"lois lowry","122H",1989,137]},"Study Club")
m1 = Member("@rajkumarra_123","raj123Ai_9","rajkumar","rathorerajkumar368@gmail.com","9982030680","NA","100")
catalog = Catalog()
while(True):
    print("welocome to the {} library.please Enter your choice".format(library.name))
    print("1","display_books")
    print("2","lend_book")
    print("3","return book")
    print("4","pay fine")
    print("5","search book By book_Name")
    print("6","search book By Author_Name")
    print("\n")
    print("this is Librarian task please login with Librarian_id to perform task")
    print("7","add book")
    print("8","remove book")

    user_choice = input()
    if user_choice not in ["1","2","3","4","5","6","7","8"]:
        print("please Enter correct choice \n")
        continue
    else:
        user_choice = int(user_choice)
        if user_choice == 1:
            print("we have following books in {} library".format(library.name))
            library.display_books()
            print("\n")
        elif user_choice == 2:
            book = input("please Enter the name of the book you want to lend :")
            user = input("please enter your name:")
            m1.lend_book(library,book,user)
            print("\n")

        elif user_choice == 3:
            book = input("please Enter the name of the book you want to return :")
            user = input("please enter your name:")
            m1.return_book(library,book,user)
            print("\n")
        elif user_choice == 4:
            book = input("please Enter the name of the book having fine :")
            user = input("please enter your name:")
            m1.cheack_fine(library,book,user)
            print("\n")
            
        elif user_choice == 5:
            book_name = input("Enter the name of book: ")
            catalog.searchByName(library,book_name)
            print("\n")
            
        elif user_choice == 6:
            Author = input("Enter the name of author: ")
            catalog.searchByAuthor(library,Author)
            print("\n")
            
        elif user_choice == 7:
            username = input("username: ")
            password = input("password: ")
            libr = Librarian(username,password,"kumar","rathorekumar368@gmail.com","8982030680","NA","109g")
            print("now you can add book in library")
            print("\n")
            book_name = input("Enter the name of the book you want to add: ")
            quantity = int(input("Enter quantity of book to add: "))
            author = input("Enter the name of author: ")
            rack = input("Enter rack number: ")
            publish_date = input("Enter the publish_date: ")
            pages = input("Enter the total number of page of book: ")
            libr.add_book(library,book_name,quantity,author,rack,publish_date,pages)
            print("\n")
        elif user_choice == 8:
            username = input("username: ")
            password = input("password: ")
            libr = Librarian(username,password,"kumar","rathorekumar368@gmail.com","8982030680","NA","109g")
            print("now you can remove book from library")
            print("\n")
            book_name = input("Enter the name of the book you want to remove: ")
            quantity = int(input("Enter quantity of book to remove: "))
            author = input("Enter the name of author: ")
            rack = input("Enter rack number: ")
            publish_date = input("Enter the publish_date: ")
            pages = input("Enter the total number of page: ")
            libr.removeBook(library,book_name,quantity,author,rack,publish_date,pages)
            print("\n")
        else:
            print("Not a valid option")
            
        print("press q to quit or c to conitinue")
        choice = ""
        while(choice!= "c" and choice != "q"):
            choice = input()
            if choice == "c":
                continue
            elif choice == "q":
                sys.exit()

