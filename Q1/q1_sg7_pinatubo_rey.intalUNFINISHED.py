"""
UNFINISHED** https://www.geeksforgeeks.org/python/convert-string-into-variable-name-in-python/
※3 examples
※Text effects, time module, and os module for emphasis and style
※Lore-accurate to pshs-clc
※May have been used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg7_Pinatubo_Espiritu.py because plagiarizing without crediting is bad, also sampleInheristance and sampleComposition notes.
※#some comments
※Title for program kasi i am muon themed.

"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

class Glassware:
    def __init__(self):
        None

class Beaker(Glassware):
    def __init__(self, object_type):
        super().__init__(object_type)
    def __del__(self):
        print(f"Beaker is lost into the system. You can't see it in the inventory anymore...")#is this foreshadowing a future game.

class Tray:
    def __init__(self):
        print(f"A tray was organized into existence in the inventory.")
        self.Glassware = Glassware()
    def __del__(self):
        print(f"A tray has been deleted.") 
        del self.Glassware

def Program_run():#starts program and simple explanation
    sys("cls")
    time.sleep(0.5)
    print(f"You opened {effect(1)}Lab Muonager Mission{effect(22)} program. You can organize a tray into existence that will compose 5 beakers.")
    time.sleep(0.5)
    print(f"{effect(3)}...Yes, the tray itself will compose the beakers. When the tray is deleted, the beakers would also be lost.")
    print(f"Also the beaker does nothing. It simply exists.{effect(23)}") 
    time.sleep(0.5)
    trays = []
    while True:#Example Input
        inventory = input(f"{effect(22)}Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to create a tray, {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to delete a tray. Otherwise, program would be terminated.{effect(1)}{effect(3)}")
        time.sleep(0.5)
        if inventory == "y":#create a tray
            varname = input(f"{effect(22)}{effect(23)}{effect(22)}Name your tray with a unique name.{effect(1)}")
            trays.append(varname)
            exec("trays[-1] = Tray()")
        elif inventory == "x":
            while True:
                try:traydel = int(input(f"How many trays would you delete?"))
                except ValueError:print(f"{effect(3)}Please input an integer.")
                else:
                    if traydel < 0:print(f"{effect(3)}Please input a non-negative number.")
                    else:break
            for indivtray in range(traydel):
                del (exec("trays[traydel-indivtray]"))
        else:break

    print(f"{effect(3)}Program terminated.{effect(0)}")
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb

if __name__ == "__main__":Program_run()