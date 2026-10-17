"""
Lines 1 ~ 22 — Table of Contents and important message
Lines 23 ~ 25 — Imports
Class at line 27 — Publication Class
Class at line 43 — Book Subclass
Class at line 56 — Magazine Subclass
Lines 69~73 — Introduction
Lines 75~99 — Sample use of the classes
Lines 75~85 — Creating the objects
Lines 87~99 — Displaying the objects
Lines 101~197 — Using your classes yourself with input
Lines 103,104 — Action input
Lines 106~133 — Creating Attributes of Publication
Lines 135~149 — Creating the Publication
Lines 151~155 — View Publications
Lines 157~182 — Set Publication information
Lines 184~195 — Deleting Publications
Lines 205 ~ 243 — End message, and necessities for rubrics

※Used for reference: https://github.com/krey2030/CS3/blob/main/Q1/q1_sg7_pinatubo_rey.intal.py
※IMPORTANT; needed to be downloaded alongside this: https://github.com/krey2030/CS3/blob/main/important_module.py
"""
from os import system as sys #makes it simple
import time
from important_module import * #REQUIRED TO DOWNLOAD "important_module"

class Publication:#Publication
    def __init__(self, __title, __author):
        self.__title = __title
        self.__author = __author
        time.sleep(0.2)
        print(f"{effect(22)}{effect(3)}{__title}{effect(23)} is made clear and is organized into the library.")
    def get_title(self):return self.__title
    def get_author(self):return self.__author
    def set_title(self,__title):self.__title = __title
    def set_author(self,__author):self.__author = __author
    def display_info(self):
        print(f"Title: {effect(3)}{self.__title}{effect(23)}\nAuthor: {effect(1)}{self.__author}{effect(22)}")#APA citation kasi diba title must be italics😉
        if isinstance(self, Book):print(f"Number of pages: {self.get_page_amount()}")
        elif isinstance(self, Magazine):print(f"Issue Number: {self.get_issue_number()}")
    def __del__(self):print(f'{effect(3)}{self.__title}{effect(23)} has been cleared out of the library. Like a beaker, all its contents are effectively {effect(3)}"lost"{effect(23)} into the system.')#ordinary deletion

class Book(Publication):#Book
    def __init__(self, __title, __author, __page_amount):
        if __page_amount > 0:self.__page_amount = __page_amount
        else:raise ArithmeticError#if it is an input, it can be fixed using try/except.
        super().__init__(__title,__author)
    def get_page_amount(self):return self.__page_amount
    def set_page_amount(self, __page_amount):
        try:int(__page_amount)
        except ValueError:print(f"{effect(3)}The number of pages must be an integer.{effect(23)}")#it will not set, it retains original number
        else:
            if __page_amount <= 0:print(f"{effect(3)}The number of pages must be positive.{effect(23)}")#it will not set, it retains original number
            else:self.__page_amount = __page_amount

class Magazine(Publication):#Magazine
    def __init__(self, __title, __author, __issue_number):
        if __issue_number > 0:self.__issue_number = __issue_number
        else:raise ArithmeticError#if it is an input, it can be fixed using try/except.
        super().__init__(__title,__author)
    def get_issue_number(self):return self.__issue_number
    def set_issue_number(self, __issue_number):
        try:int(__issue_number)
        except ValueError:print(f"{effect(3)}The issue number must be an integer.{effect(23)}")#it will not set, it retains original number
        else:
            if __issue_number <= 0:print(f"{effect(3)}The issue number must be positive.{effect(23)}")#it will not set, it retains original number
            else:self.__issue_number = __issue_number

sys("cls")
print(f"You opened 『{effect(1)}Heavy Subatomic Books{effect(22)}』 program. This program is for the school librarian who needs a clear and organized way to display information about library materials.")
time.sleep(0.5)
print(f"This program makes the librarian ready to swing 🕸️ their way to the library desk 👑, bringing every book and magazine to its shelves before they're gone.\n")
time.sleep(1)

#Creating objects
publications = []

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
publications.append("pub1")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
publications.append("book1")

mag1 = Magazine("National Geographic", "Various Authors", 202)
publications.append("mag1")

#Displaying the information
print(f"\n{effect(1)}Publication Information:{effect(22)}")
pub1.display_info()
time.sleep(0.5)

print(f"\n{effect(1)}Book Information:{effect(22)}")
book1.set_page_amount(-310)
book1.display_info()
time.sleep(0.5)

print(f"\n{effect(1)}Magazine Information:{effect(22)}")
mag1.display_info()
time.sleep(0.5)

#Creating YOUR own objects
while True:
    print(f"{effect(22)}{effect(23)}\nInput {effect(1)}{effect(3)}p{effect(22)}{effect(23)} to create a simple publication. Input {effect(1)}{effect(3)}b{effect(22)}{effect(23)} to create a book. Input {effect(1)}{effect(3)}m{effect(22)}{effect(23)} to create a magazine. ")
    pubchoice = input(f"Input {effect(1)}{effect(3)}v{effect(22)}{effect(23)} to show all or one publication. Input {effect(1)}{effect(3)}z{effect(22)}{effect(23)} to alter information. Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to clear out one or all publications.\n{effect(1)}{effect(3)}").lower()
    time.sleep(0.5)
    if pubchoice == "p" or pubchoice == "b" or pubchoice == "m":#title and author
        pub_title = input(f"{effect(22)}{effect(23)}Input publication title.{effect(3)}\n")
        time.sleep(0.5)
        pub_author = input(f"{effect(22)}{effect(23)}Input publication author.{effect(1)}\n")
        time.sleep(0.5)
    elif pubchoice != "v" and pubchoice != "x" and pubchoice != "z":break#end of program
    if pubchoice == "b":#number of pages
        time.sleep(0.5)
        while True:
            try:book_page_amount = int(input(f"{effect(22)}{effect(23)}Input number of pages.{effect(1)}\n"))
            except ValueError:
                print(f"{effect(22)}{effect(3)}The number of pages must be an integer. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
                time.sleep(0.1)
            else:break
    elif pubchoice == "m":#issue number
        time.sleep(0.5)
        while True:
            try:mag_issue_number = int(input(f"{effect(22)}{effect(23)}Input issue number.{effect(1)}\n"))
            except ValueError:
                print(f"{effect(22)}{effect(3)}The issue number must be an integer. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
                time.sleep(0.1)
            else:break
    if pubchoice != "v" and pubchoice != "x" and pubchoice != "z":#variable for the new publication
        time.sleep(0.5)
        varname = input(f"\n{effect(23)}{effect(22)}Label it with an ID—a shorter version of a title with a unique name.\nIf it is not unique, it would replace the publication with the same name.\n{effect(1)}")
        publications.append(varname)

    publications = list(dict.fromkeys(publications))#remove duplicates

    #Create the Publication
    if pubchoice == "p":globals()[varname] = Publication(pub_title,pub_author)#is easy to create
    elif pubchoice == "b":#book
        while True:
            try:globals()[varname] = Book(pub_title,pub_author,book_page_amount)
            except ArithmeticError:
                print(f"{effect(22)}{effect(3)}The number of pages must be an integer. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
                try:book_page_amount = int(input(f"{effect(22)}{effect(23)}Input number of pages.{effect(1)}\n"))
                except ValueError:print(f"{effect(22)}{effect(3)}The number of pages must be an integer. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
    elif pubchoice == "m":#magazine
        try:globals()[varname] = Magazine(pub_title,pub_author,mag_issue_number)
        except ArithmeticError:
            print(f"{effect(22)}{effect(3)}The issue number must be positive. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
            try:mag_issue_number = int(input(f"{effect(22)}{effect(23)}Input number of pages.{effect(1)}\n"))
            except ValueError:print(f"{effect(22)}{effect(3)}The issue number must be an integer. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
            
    elif pubchoice == "v": #View (gets)
        for publication in publications:
            time.sleep(0.5)
            print(f"\n{effect(3)}ID{effect(23)}: {effect(1)}{publication}{effect(22)}")
            globals()[publication].display_info()

    elif pubchoice == "z": #Set
        print(f"{effect(22)}{effect(23)}List of publication IDs")
        for publication in publications:print(f"{effect(1)}{publication}{effect(22)}")
        pubalterwhat = None
        pubalterwhich = input(f"\nInput the ID of the publication to alter information with.\n{effect(1)}")#Choose the publication to set information
        try:publications.index(pubalterwhich)
        except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{pubalterwhich}{effect(22)} in publication IDs. Nothing was cleared away.{effect(23)}")
        
        else:#Set the publication information
            time.sleep(0.5)
            print(f"{effect(23)}{effect(22)}What do you want to alter? Input {effect(1)}{effect(3)}title{effect(22)}{effect(23)} or {effect(1)}{effect(3)}author{effect(22)}{effect(23)}.")
            if isinstance(globals()[pubalterwhich],Book):pubalterwhat = input(f"Or to set number of pages, input {effect(1)}{effect(3)}page{effect(22)}{effect(23)}.\n{effect(1)}").lower()
            elif isinstance(globals()[pubalterwhich], Magazine):pubalterwhat = input(f"Or to set issue number, Input {effect(1)}{effect(3)}issue{effect(22)}{effect(23)}\n{effect(1)}").lower()
            elif isinstance(globals()[pubalterwhich],Publication):pubalterwhat = input(f"{effect(1)}{effect(3)}").lower()
        if pubalterwhat == "title":
            pubalterto = input(f"Set the new title of the publication {effect(1)}{pubalterwhich}{effect(22)}.\n{effect(3)}")
            globals()[pubalterwhich].set_title(pubalterto)
        elif pubalterwhat == "author":
            pubalterto = input(f"Set the new author of the publication {effect(1)}{pubalterwhich}{effect(22)}.\n{effect(1)}")
            globals()[pubalterwhich].set_author(pubalterto)
        elif pubalterwhat == "page":
            pubalterto = input(f"Set the number of pages of the publication {effect(1)}{pubalterwhich}{effect(22)}.\n{effect(1)}")
            globals()[pubalterwhich].set_page_amount(pubalterto)
        elif pubalterwhat == "issue":
            pubalterto = input(f"Set the issue number of the publication {effect(1)}{pubalterwhich}{effect(22)}.\n{effect(1)}")
            globals()[pubalterwhich].set_issue_number(pubalterto)
    
    else:#if it is x; it can't be not x
        pubremove = input(f"{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to clear all publications. Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to clear one publication. Otherwise nothing will be cleared.\n{effect(1)}{effect(3)}").lower()
        if pubremove == "x":
            for publication in range(len(publications)):del globals()[publications[publication]]#deletes the object
            publications.clear()
        elif pubremove == "y":
            print(f"{effect(22)}{effect(23)}List of publication IDs")
            for publication in publications:print(f"{effect(1)}{publication}{effect(22)}")
            pubremove1 = input(f"Input the ID of the publication to clear out.\n{effect(1)}")
            try:publications.remove(pubremove1)
            except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{pubremove1}{effect(22)} in publication IDs. Nothing was cleared away.{effect(23)}")
            else:del globals()[pubremove1]#deletes the object

    time.sleep(1)

print(f"{effect(22)}{effect(3)}Program terminated.{effect(0)}")
time.sleep(1)
sys("cls")#"cls" for VSCode, "clear" for onlinegdb
print(f"{effect(3)}Program terminated.{effect(0)}")
time.sleep(1)

"""
• It is long enough so I included Table of Contents.

Following Instructions and Requirements:
    Code Functionality:
    →Classes has their attributes and methods and a little more. get/set_number_of_pages() have been renamed.
    →Book and Magazine is inherited from Publication.
    →Objects in the example are provided, and you can create your own objects and also alter the sample objects.
    →Hopefully no errors.

    Code Efficiency:
    →display_info() would also display number of pages or issue number.
    →Methods are used in the sample and can be used when creating your own objects.
    Good coding practice:
    →Comments are present naman
    →Variables aren't nonsense naman ata

    Error handling:
    →ALOT of error handling; implementing the delete actions was so difficult and everything needs alot of debugging but finally works seemingly perfectly.
    Portfolio → Portfolio was updated naman

    Creativity:
    →Obvious naman andami ko nilagay dito
    →Table of Contents
    →Effect function like my usual style
    →Delete function
    →Creating your own objects
    →Basta napakadami

※stupidly used AI many times since it returns AttributeError. The problem is literally because of inconsistency. self.title = __title instead of self.__title = __title
    →Google would never gives personalized results, my case is a bit specific yata
    →The other time, also looking for the word "personalized" which is ironic. Google wouldn't have gave me the word, but AI would be personalized...
    →and again, trying to delete publications, it sucks to use AI, im sorry
    →nothing was copy pasted from AI (that i did not originally write)
    →I ended up getting rid of "program_run" function and if __name__ = "__main__" because there's problems with using locals()

• This took a whole day to make. 【Combined with yesterday Oct.16,2026 class】【About 11 hours ata】
• A project under "Spider Commuons" which is like my new "company name"
"""