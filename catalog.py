import sys
class Catalog:
    def searchByName(self,library,book_name):
        for key,value in library.Count_book_dict.items():
           if book_name in library.Count_book_dict.keys():
                    print("we are fetching book deatails on the basis of your quary")
                    print("\n")
                    print("book_name: {} and Other details like  quantity,author_name,rack_number,publish_date,number_of_page respectivey: {}".format(book_name,library.Count_book_dict[book_name]))
                    print("\n")
                    print("if you want to proceed further then enter your choice")
                    choice = input("yes/no: ")
                    if choice == "yes":
                        break
                    else:
                        print("you are exiting from system")
                        sys.exit()
           else:
                print("we don't have have this book in our library please cheack your input")
                break

    
    def searchByAuthor(self,library,Author):
        for key,value in library.Count_book_dict.items():
            if Author in value[1]:
                print("we are fetching book deatails on the basis of your quary")
                print("\n")
                print("book_name: {} and Other details like  quantity,author_name,rack_number,publish_date,number_of_page respectivey: {}".format(key,value))
                print("\n")
                print("if you want to proceed further then enter your choice")
                choice = input("yes/no: ")
                if choice == "yes":
                    break
                else:
                    print("you are exiting from system")
                    sys.exit()
        else:
            print("we don't have have this book in our library please cheack your input")

                
