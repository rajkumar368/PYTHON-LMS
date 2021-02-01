from datetime import date,timedelta
class User:
    def __init__(self,username,password,user,email,mobile,address):
        self.username = username
        self.password = password
        self.user = user
        self.email = email
        self.mobile = mobile
        self.address = address
        
class Member(User):
    def __init__(self,username,password,user,email,mobile,address,member_id):
        super().__init__(username,password,user,email,mobile,address)
        self.member_id = member_id
        self.max_book_count = {}
        self.bookdict = {}
        
    def Count_book(self,user,book):
        if user not in self.max_book_count:
            self.max_book_count[user] = [book]
            return len(self.max_book_count[user])
        else:
            if len(self.max_book_count[user])<=4:
                self.max_book_count[user].append(book)
                return len(self.max_book_count[user])
            else:
                return len(self.max_book_count[user])
            
    def lend_book(self,library,book,user):
    # Issuing book to the user by cross verifying libray stock and user can issue only one book of particular subject
    # maintaining record   
            if book in library.Count_book_dict.keys():
                if library.Count_book_dict[book][0]>=1:
                    if (book,user) not in self.bookdict.keys():
                        if not self.cheack_pervious_fine(book,user):
                            if self.Count_book(user,book)<=5:
                                lend_date = date.today()
                                return_date = date.today()+timedelta(days = 10)
                                self.bookdict.update({(book,user):return_date})
                                library.Count_book_dict[book][0] -= 1
                                for value in self.bookdict.keys():
                                    if value == (book,user):
                                        print("{} book is issued to your name {} on {}. you can get the book".format(value[0],value[1],lend_date))
                                        print("you have 10 days to read book. please return book on time otherwise 10 rupess/day fine will be charge")
                                        print(self.max_book_count)
                            else:
                                print("you can issue maximum 5 books only")
                        else:
                            print("you have to pay to fine first then you will be able to lend book")
                    else:
                        print("this book is already issued to your name")
                else:
                    print("this book is out of stock")
            else:
                print("sorry we haven't this book in our library")


            
    def cheack_pervious_fine(self,book,user):
        current_date = date.today()
        for key,value in self.bookdict.items():
            if key[1]==user:
                return_date = self.bookdict[key]
                if current_date > return_date:
                    delay_days = (current_date - return_date).days
                    total_fine = delay_days*10
                    return total_fine
                else:
                    return 0 
                
    def return_book(self,library,book,user):
# return book,updating records and if dealy then charge fine 10rs/day.
        if (book,user)in self.bookdict.keys():
            return_date =  self.bookdict[(book,user)]
            current_date = date.today()
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days*10
                print("please pay fine,you have to pay {} rupess" .format(total_fine))
                print("we are rediracting to you on payment page")
                self.payment(library,book,user)
            else:
                self.max_book_count[user].remove(book)
                self.bookdict.pop((book,user))
                library.Count_book_dict[book][0] += 1
                print("book sucessfully returned")
        else:
            print("please provide correct username and book name")
            
            
    def payment(self,library,book,user):
        print("for payment process. Enter your choice ")
        choice = input("yes/no: ")
        if choice == "yes":
            print("your payment is processing")
            print("payment successful")
            self.max_book_count[user].remove(book)
            self.bookdict.pop((book,user))
            library.Count_book_dict[book][0] += 1
        else:
            print("we are rediracting you to homepage")
            
            
    def cheack_fine(self,library,book,user):
        if (book,user)in self.bookdict.keys():
            return_date =  self.bookdict[(book,user)]
            current_date = date.today()
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days*10
                print("please pay fine,you have to pay {} rupess" .format(total_fine))
                print("DO you want to pay fine now")
                choice = input("yes/no")
                if choice == "yes":
                    self.payment(library,book,user)
                else:
                    print("we are rediracting to homepage")
            else:
                print("you don't need to pay fine")
        else:
            print("Enter correct information")
