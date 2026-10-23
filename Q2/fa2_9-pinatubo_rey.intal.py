"""
• Text effects, time module, and os module for emphasis and style
※ I made it so the user could input the patient and all their details, and can view one or all the patient details, and set their details too.
 → An explanation was given too and user-friendly inputs. Also a  muon-themed title🥰
※Heavily used for reference: https://github.com/krey2030/CS3/blob/main/Q2/fa1_9-pinatubo_rey.intal.py
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
        print(f"Final Bill: {c}{self.calculate_bill()}")

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
                try:patient_bill = float(input(f"{effect(22)}{effect(23)}Input Original Bill without discounts.{effect(1)}\n"))
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
        if patientchoice == "r":globals()[varname] = Patient(patient_name,patient_bill)#is easy to create
        elif patientchoice == "s":globals()[varname] = SeniorPatient(patient_name,patient_bill)
        elif patientchoice == "h":globals()[varname] = PhilHealthPatient(patient_name,patient_bill)
        
        elif patientchoice == "v": #View (gets)
            patientview = input(f"{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to view all patient details. Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to view one patient detail. Otherwise you won't view a patient detail.\n{effect(1)}{effect(3)}").lower()
            if patientview == "x":
                for patient in patients:
                    time.sleep(0.5)
                    print(f"\n{effect(3)}ID{effect(23)}: {effect(1)}{patient}{effect(22)}")
                    globals()[patient].display_info(c)
            elif patientview == "y":
                print(f"{effect(22)}{effect(23)}List of patient IDs")
                for patient in patients:print(f"{effect(1)}{patient}{effect(22)}")
                patientview1 = input(f"Input the patient ID to view details.\n{effect(1)}")
                try:patients.index(patientview1)
                except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{patientview1}{effect(22)} in patient IDs. No details were viewed.{effect(23)}")
                else:globals()[patient].display_info(c)
        
        elif patientchoice == "z": #Set
            print(f"{effect(22)}{effect(23)}List of patient IDs")
            for patient in patients:print(f"{effect(1)}{patient}{effect(22)}")
            patientalterwhat = None
            patientalterwhich = input(f"\nInput the ID of the patient to alter information with.\n{effect(1)}")#Choose the patient to set information
            try:patients.index(patientalterwhich)
            except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{patientalterwhich}{effect(22)} in patient IDs. Nothing was altered.{effect(23)}")
            else:#Set the patient information
                time.sleep(0.5)
                patientalterwhat = input(f"{effect(23)}{effect(22)}What do you want to alter? Input {effect(1)}{effect(3)}name{effect(22)}{effect(23)} or {effect(1)}{effect(3)}bill{effect(22)}{effect(23)}.{effect(1)}{effect(3)}\n").lower()
            if patientalterwhat == "name":
                patientalterto = input(f"{effect(23)}{effect(22)}Set the new name of patient {effect(1)}{patientalterwhich}{effect(22)}.\n{effect(1)}")
                globals()[patientalterwhich].set_name(patientalterto)
            elif patientalterwhat == "bill":
                patientalterto = input(f"Set the new original bill of the patient {effect(1)}{patientalterwhich}{effect(22)}.\n{effect(1)}")
                globals()[patientalterwhich].set_billamount(patientalterto)
            else:print(f"{effect(22)}Nothing was altered.{effect(23)}")

    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)
    print(f"{effect(3)}Program terminated.{effect(22)}")

if __name__ == "__main__":Program_run()

"""
• This took 2.5 periods to make. 【Oct.22,2026 wellness】Progress on Oct.22 3:45-4:15 was not saved so time taken to do it in CS period on 7:50-8:20am
• A project under "Spider Commuons" which is like my new "company name"
"""