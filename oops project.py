#welcome to aapki apni library
class library:
    def __init__(self,book_list,library_name):
        self.booklist=book_list
        self.libname=library_name
        self.lend_record={} # empty dictionary created
    def display(self):
        print(f'we have following book in library:{self.libname}')
        for book in self.booklist:
            print(book)

    def add_book(self,book):
        # book=input('enter book which you want to add')
        self.booklist.append(book)
        print('book has been added to the book list')

    def lend_book(self,user,book):   
        # book=input('enter book which you want to lend from library')
        if book not in self.lend_record.keys():
            self.lend_record.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f' book is already in use by {self.lend_record[book]}')

    def return_func (self,book):
        self.lend_record.pop(book)

        """book=input('enter book name you want to enter')
        if book in self.lend_record:
            self.booklist.append(book)
            del self.lend_record[book]
        else:
            print('enter valid input')"""

if __name__=='__main__' :
    goyal=library(['harry potter','rich dad',' atomic habits'],'aapki apni library')
    
while True:
    print('welcome')
    print('Q for quit\na for add\nd for display\nr for return\nl for lend')
    userinput=input('enter input\n ')
    if userinput=='q' or userinput=='Q':
        print('you quit\n thank you')
        break
    elif userinput=='a' or userinput=='A':
        book=input('enter the name of book you want to add:')
        goyal.add_book(book)
    elif userinput=='r' or userinput=='R':
        book=input('enter the name of book you want to return:')
        goyal.return_func(book)
    elif userinput=='l' or userinput=='L':
        book=input('enter the name of book you want to lend:')
        user=input('enter your name')
        
        goyal.lend_book(user,book)

    elif userinput=='d' or userinput=='D':
        
        goyal.display()
    else:
        print('not valid input')
        print('Thank you for using aapki apni library')



