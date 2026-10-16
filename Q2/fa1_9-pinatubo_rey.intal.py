"""
※Text effects, time module, and os module for emphasis and style
※Used for reference: https://github.com/krey2030/CS3/blob/main/Q1/q1_sg7_pinatubo_rey.intal.py
※#some comments
※There's no deletion of publications due to limited time

"""
from os import system as sys #makes it simple
import time
from important_module import *#REQUIRED TO DOWNLOAD "important_module"

class Publication:
    def __init__(self, __title, __author):
        self.title = __title
        self.author = __author
    def get_title(self):return self.__title
    def get_author(self):return self.__author
    def set_title(self,__title):self.__title = __title
    def set_author(self,__author):self.__author = __author
    def display_info(self):print(f"Title: {effect(3)}{self.title}{effect(23)}\nAuthor: {effect(1)}{self.author}{effect(22)}")#APA citation kasi diba title must be italics😉

class Book(Publication):
    def __init__(self, __title, __author, __page_amount):
        self.__page_amount = __page_amount
        super().__init__(__title,__author)
    def get_page_amount(self):return self.__page_amount
    def set_page_amount(self, __page_amount):
        if __page_amount <= 0:
            print(f"{effect(3)}The number of pages must be positive.{effect(23)}")
        else:self.__page_amount = __page_amount

class Magazine(Publication):
    def __init__(self, __title, __author, __issue_number):
        self.__issue_number = __issue_number
        super().__init__(__title,__author)
    def get_issue_number(self):return self.__issue_number
    def set_issue_number(self, __issue_number):
        if __issue_number <= 0:
            print(f"{effect(3)}The number of pages must be positive.{effect(23)}")
        else:self.__issue_number = __issue_number

def Program_run():#starts program and simple explanation
    sys("cls")
    print(f"You opened {effect(1)}{effect(22)} program. This program is for the school librarian who needs a clear and organized way to display information about library materials.\n")
    time.sleep(1)

    #Creating objects
    pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    mag1 = Magazine("National Geographic", "Various Authors", 202)

    #Printing the information
    
    print(f"\n{effect(1)}Publication Information:{effect(22)}")
    pub1.display_info()
    time.sleep(0.5)

    print(f"\n{effect(1)}Book Information:{effect(22)}")
    book1.set_page_amount(-310)
    book1.display_info()
    print(book1.get_page_amount())
    time.sleep(0.5)

    print(f"\n{effect(1)}Magazine Information:{effect(22)}")
    mag1.display_info()
    print(mag1.get_issue_number())
    time.sleep(0.5)

    #Creating YOUR own objects
    publications = []
    while True:
        print(f"\nInput {effect(1)}{effect(3)}p{effect(22)}{effect(23)} to create a simple publication. Input {effect(1)}{effect(3)}b{effect(22)}{effect(23)} to create a book.")
        pubchoice = input(f"Input {effect(1)}{effect(3)}m{effect(22)}{effect(23)} to create a magazine. Input {effect(1)}{effect(3)}s{effect(22)}{effect(23)} to show all publications.{effect(1)}{effect(3)}").lower()
        time.sleep(0.5)
        if pubchoice == "p" or pubchoice == "b" or pubchoice == "m":
            pub_title = input(f"{effect(22)}{effect(23)}Input publication title.{effect(3)}\n")
            time.sleep(0.5)
            pub_author = input(f"{effect(22)}{effect(23)}Input publication author.{effect(1)}\n")
            time.sleep(0.5)
        elif pubchoice != "s":break

        if pubchoice == "b":
            book_page_amount = input(f"{effect(22)}{effect(23)}Input number of pages.{effect(1)}\n")
        elif pubchoice == "m":
            mag_issue_number = input(f"{effect(22)}{effect(23)}Input number of pages.{effect(1)}\n")
        time.sleep(1)


        varname = input(f"\n{effect(23)}{effect(22)}Name a shorter version of a title with a unique name.\nIf it is not unique. it would replace the publication with the same name.\n{effect(1)}")
        publications.append(varname)
        if pubchoice == "p":globals()[varname] = Publication(pub_title,pub_author)
        elif pubchoice == "b":globals()[varname] = Book(pub_title,pub_author,book_page_amount)
        elif pubchoice == "m":globals()[varname] = Magazine(pub_title,pub_author,mag_issue_number)
        

        
        time.sleep(1)

    print(f"{effect(3)}Program terminated.{effect(0)}")
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb

if __name__ == "__main__":Program_run()