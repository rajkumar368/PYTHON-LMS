# -*- coding: utf-8 -*-
class Library:
    def __init__(self,Count_book,name):
        self.Count_book_dict = Count_book
        self.name = name
        self.bookdict = {}
        self.max_book_count = {}
        self.Count_book_dict
        
    def display_books(self):
#  display books name and quantity currently present in the library 
        for books in self.Count_book_dict.items():
            print(books)
