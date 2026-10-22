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
Lines 101~205 — Using your classes yourself with input
Lines 103,104 — Action input
Lines 106~133 — Creating Attributes of Publication
Lines 135~157 — Creating the Publication
Lines 159~163 — View Publications
Lines 165~190 — Set Publication information
Lines 192~203 — Deleting Publications
Lines 213 ~ 252 — End message, and necessities for rubrics

※Used for reference: https://github.com/krey2030/CS3/blob/main/Q1/q1_sg7_pinatubo_rey.intal.py
※IMPORTANT; needed to be downloaded alongside this: https://github.com/krey2030/CS3/blob/main/important_module.py
"""
from os import system as sys #makes it simple
import time
from important_module import * #REQUIRED TO DOWNLOAD "important_module"

class Patient:
    def __init__(self, __name, __billamount):
        self.__name = __name
        self.__billamount = __billamount
        time.sleep(0.2)
        #print(f"{effect(22)}{effect(3)}{__name}{effect(23)} is made clear and is organized into the library.")
    def get_name(self):return self.__name
    def get_billamount(self):return self.__billamount
    def set_name(self,__name):self.__name = __name
    def set_billamount(self,__billamount):
        try:self.__billamount = float(__billamount)
        except ValueError:print(f"{effect(3)}The number of pages must be an integer/decimal number.{effect(23)}")#it will not set, it retains original number
    def calculate_bill(self):return self.__billamount
    def display_info(self,c):
        print(f"Patient Name: {self.__name}")
        print(f"Orignal Bill: {c}{self.__billamount}")
        print(f"Final Bill: {c}{self.__name}")

class SeniorPatient(Patient):
    def calculate_bill(self):
        return super().get_billamount()*0.8

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return super().get_billamount()*0.85

def Program_run():#starts program and simple explanation
    sys("cls")
    print(f"You opened 『{effect(1)}Patient's Muoney{effect(22)}』 program.\nThis is a Hospital Billing System program that computes different type of patient bills.")
    time.sleep(1)
    print("Please input the currency symbol first. It would be used consistently in all currencies and before the number no matter what since conversion is not covered by this program.\n")
    time.sleep(0.2)
    c = input(f"Case sensitive. For easy copy of the most common currency symbols: ₱$¥¤€£⨴")#⨴is just easter egg, not a real currency but it's referencing my own "currency" in my minecraft world
    time.sleep(0.5)
    patients = []
    while True:
        time.sleep(0.5)
        print(f"{effect(22)}{effect(23)}\nInput the type of patient. {effect(1)}{effect(3)}r{effect(22)}{effect(23)} for {effect(1)}Regular Patient{effect(22)}, {effect(1)}{effect(3)}s{effect(22)}{effect(23)} for {effect(1)}Senior Citizen{effect(22)}, {effect(1)}{effect(3)}h{effect(22)}{effect(23)} for {effect(1)}PhilHealth Member{effect(22)}.")
        patientchoice = input(f"Otherwise, input {effect(1)}{effect(3)}v{effect(22)}{effect(23)} to show all or one patient details. Input {effect(1)}{effect(3)}z{effect(22)}{effect(23)} to alter a patient's detail. Otherwise program will terminate.\n{effect(1)}{effect(3)}").lower()
        time.sleep(0.5)
        if patientchoice == "r" or patientchoice == "s" or patientchoice == "h":#name
            patient_name = input(f"{effect(22)}{effect(23)}Input Patient Name.{effect(1)}\n")
            time.sleep(0.5)
            while True:
                try:patient_bill = input(f"{effect(22)}{effect(23)}Input Original Bill without discounts.{effect(1)}\n")
                except ValueError:
                    print(f"{effect(22)}{effect(3)}The bill must be an integer/decimal number. {effect(1)}Try again{effect(22)}.{effect(23)}")#user must try again since it must have value.
                    time.sleep(0.1)
                else:break
        elif patientchoice != "v" and patientchoice != "z":break#end of program
        if patientchoice != "v" and patientchoice != "x" and patientchoice != "z":#variable for the new publication
            time.sleep(0.5)
            varname = input(f"\n{effect(23)}{effect(22)}Label it with an ID—like a shorter and unique version of the name.\nIf it is not unique, it would replace the patient with the same name.\n{effect(1)}")
            patients.append(varname)
        patients = list(dict.fromkeys(patients))#remove duplicates

        #Create the Publication
        if patientchoice == "p":globals()[varname] = Patient(patient_name,patient_bill)#is easy to create
        elif patientchoice == "b":globals()[varname] = SeniorPatient(patient_name,patient_bill)
        elif patientchoice == "m":globals()[varname] = PhilHealthPatient(patient_name,patient_bill)
        
        elif patientchoice == "v": #View (gets)
            patientview = input(f"{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to view all patient details. Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to view one patient detail. Otherwise you won't view a patient detail.\n{effect(1)}{effect(3)}").lower()
            if patientview == "x":
                for patient in patients:
                    time.sleep(0.5)
                    print(f"\n{effect(3)}ID{effect(23)}: {effect(1)}{patient}{effect(22)}")
                    globals()[patient].display_info()
            elif patientview == "y":
                print(f"{effect(22)}{effect(23)}List of patient IDs")
                for patient in patients:print(f"{effect(1)}{patient}{effect(22)}")
                patientview1 = input(f"Input the patient ID to view details.\n{effect(1)}")
                try:patients.index(patientview1)
                except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{patientview1}{effect(22)} in patient IDs. No details were viewed.{effect(23)}")
                else:globals()[patient].display_info()
        
        elif patientchoice == "z": #Set
            print(f"{effect(22)}{effect(23)}List of publication IDs")
            for patient in patients:print(f"{effect(1)}{patient}{effect(22)}")
            patientalterwhat = None
            patientalterwhich = input(f"\nInput the ID of the publication to alter information with.\n{effect(1)}")#Choose the publication to set information
            try:patients.index(patientalterwhich)
            except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{patientalterwhich}{effect(22)} in publication IDs. Nothing was cleared away.{effect(23)}")
            else:#Set the patient information
                time.sleep(0.5)
                patientalterwhat = input(f"{effect(23)}{effect(22)}What do you want to alter? Input {effect(1)}{effect(3)}name{effect(22)}{effect(23)} or {effect(1)}{effect(3)}bill{effect(22)}{effect(23)}.{effect(1)}{effect(3)}").lower()
            if patientalterwhat == "name":
                patientalterto = input(f"Set the new name of patient {effect(1)}{patientalterwhich}{effect(22)}.\n{effect(1)}")
                globals()[patientalterwhich].set_title(patientalterto)
            elif patientalterwhat == "bill":
                patientalterto = input(f"Set the new author of the publication {effect(1)}{patientalterwhich}{effect(22)}.\n{effect(1)}")
                globals()[patientalterwhich].set_billamount(patientalterto)
        else:break

    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)
    print(f"{effect(3)}Program terminated.{effect(22)}")

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
    →There's an error AttributeError, but it apparently the program keeps running normally.

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