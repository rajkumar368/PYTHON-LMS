# -*- coding: utf-8 -*-
from User import User
class Librarian(User):
    def __init__(self,username,password,name,email,mobile,address,librarian_id):
        super().__init__(username,password,name,email,mobile,address)
        self.librarian_id = librarian_id
       
        
    def add_book(self,library,book_name,quantity,author,rack,publish_date,pages):
# add new_book in the library
        if quantity>0:
            if book_name in library.Count_book_dict.keys():
                library.Count_book_dict[book_name][0]+=quantity
            else:
                library.Count_book_dict.update({book_name:[quantity,author,rack,publish_date,pages]})
                print("book has been added to library")
        else:
            print("please Enter postive integer number")
            
            
    def removeBook(self,library,book_name,quantity,author,rack,publish_date,pages):
        if quantity>0:
            if book_name in library.Count_book_dict.keys():
                if library.Count_book_dict[book_name][0]>=1:
                    library.Count_book_dict[book_name][0]-=quantity
                    if library.Count_book_dict[book_name][0] < 0:
                        library.Count_book_dict[book_name][0]+=quantity
                        print("please enter correct quantity of book. we have only {} books of {}".format(library.Count_book_dict[book_name][0],book_name))
                    else:
                        print("book remove successfully")
                else:
                    library.Count_book_dict.pop(book_name)
                    print("sorry we don't have any books os {} in our libraray".format(book_name))
            else:
                print("please Enter correct book_name or quantity")
        else:
            print("please Enter postive integer number")
