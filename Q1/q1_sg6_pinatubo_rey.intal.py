"""
※3 examples
※Text effects, time module, and os module for emphasis and style
※Lore-accurate to pshs-clc
※Used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg6_Pinatubo_Espiritu.py because plagiarizing without crediting is bad
※#some comments
※Title for program kasi i am muon themed.

"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

class Lab:
    def __init__(self, room_number: int,name):
        self.room_number = int(room_number)
        self.name = name
    def __str__(self):
            return self.name
class Technician:
    def __init__(self, name, assigned_lab = None):
        self.name = name
        self.assigned_lab = assigned_lab

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj
    def __str__(self):
        return self.name

def Program_run():#starts program and simple explanation
    sys("cls")
    print(f"You opened {effect(1)}Lab Muonager Mission{effect(22)} program. This program accesses labs' data through technicians.\n")
    time.sleep(0.5)

    #Original Example altered room since its inaccurate!!

    chem_lab1 = Lab(303, "Modeling Laboratory 【Chemistry】")#it should be an int right ??
    mr_cruz = Technician("Mr. Cruz")
    mr_cruz.assign_lab(chem_lab1)
    
    time.sleep(1)
    print(f"The Lab assigned to {effect(3)}{effect(1)}{mr_cruz}{effect(23)}{effect(22)} is {effect(1)}{mr_cruz.assigned_lab}{effect(22)}.")
    time.sleep(0.5)
    print(f"His/her keycard shows {effect(1)}{mr_cruz.assigned_lab.room_number}{effect(22)}, so their room number is {mr_cruz.assigned_lab.room_number}\n")
    
    #Example 2
    bio_lab1 = Lab(301, "Microbiology Laboratory 【Biology】")#it should be an int right ??
    kmdomingo = Technician("sir Kyle Miguel Domingo")
    kmdomingo.assign_lab(bio_lab1)
    
    time.sleep(1)
    print(f"The Lab assigned to {effect(3)}{effect(1)}{kmdomingo}{effect(23)}{effect(22)} is {effect(1)}{kmdomingo.assigned_lab}{effect(22)}.")
    time.sleep(0.5)
    print(f"His/her keycard shows {effect(1)}{kmdomingo.assigned_lab.room_number}{effect(22)}, so their room number is {kmdomingo.assigned_lab.room_number}\n")

    while True:#Example Input
        time.sleep(1)
        techinput1 = input(f"Who is the next technician? simply press enter to terminate program.")
        time.sleep(0.5)
        if techinput1 == "":break
        else:
            labinput1 = input(f"What is the name of his/her assigned laboratory?")
            while True:
                time.sleep(0.5)
                try:labinput1room = int(input(f"What is the room number of his/her?\n{effect(1)}"))
                except ValueError:
                    time.sleep(0.2)
                    print(f"{effect(22)}{effect(3)}Please input a room number only (integer).{effect(23)}")
                else:break

        techinput1 = Technician(techinput1)
        lab1 = Lab(labinput1room,labinput1)
        techinput1.assign_lab(lab1)

        time.sleep(1)
        print(f"The Lab assigned to {effect(3)}{effect(1)}{techinput1}{effect(23)}{effect(22)} is {effect(1)}{techinput1.assigned_lab}{effect(22)}.")
        time.sleep(0.5)
        print(f"His/her keycard shows {effect(1)}{techinput1.assigned_lab.room_number}{effect(22)}, so their room number is {techinput1.assigned_lab.room_number}\n")

    print(f"{effect(3)}Program terminated.{effect(0)}")
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb

if __name__ == "__main__":Program_run()