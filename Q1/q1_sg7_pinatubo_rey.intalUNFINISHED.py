"""
UNFINISHED** https://www.geeksforgeeks.org/python/convert-string-into-variable-name-in-python/
※3 examples
※Text effects, time module, and os module for emphasis and style
※Lore-accurate to pshs-clc
※May have been used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg7_Pinatubo_Espiritu.py because plagiarizing without crediting is bad, also sampleInheristance and sampleComposition notes.
※I regret this but it would be difficult but also uses chatgpt to make dynamic variables.
※#some comments
※Title for program kasi i am muon themed.

"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

class Glassware:
    def __init__(self, object_type="Glassware"):
        self.object_type = object_type
    
class Beaker(Glassware):
    def __init__(self, object_type="Glassware"):
        super().__init__(object_type)

class Tray:
    def __init__(self):
        print(f"{effect(22)}{effect(3)}A tray was organized into existence in the inventory.{effect(23)}")
        self.beakers = [Beaker() for _ in range(5)]
        print(f"A {Beaker().object_type} beaker was composed by the tray.")
    def __del__(self):
        del self.beakers
        print(f"{effect(3)}The beakers from the tray is lost into the system. You can't see it in the inventory anymore..\n{effect(23)}")#To avoid duplicates. is this foreshadowing a future game.

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
        print(f"{effect(22)}Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to create a tray, {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to delete a tray. Input ")#INPUT V TO VIEW CURRENT TRAYS.
        inventory = input(f"Otherwise, program would be terminated.{effect(1)}{effect(3)}")
        time.sleep(0.5)
        if inventory == "y":#create a tray
            varname = input(f"{effect(22)}{effect(23)}Name your tray with a unique name.\nIf it is not unique. it would replace the first tray.\n{effect(1)}")
            trays.append(varname)
            globals()[varname] = Tray()
            trays = list(dict.fromkeys(trays))
        elif inventory == "x":
            while True:
                try:traydel = int(input(f"{effect(22)}{effect(23)}How many trays would you delete?\n"))
                except ValueError:print(f"{effect(3)}Please input an integer.")
                else:
                    if traydel < 0:print(f"{effect(3)}Please input a non-negative number.")
                    else:break
            time.sleep(0.4)
            candel = False
            for indivtray in range(traydel):
                try:print(f"{effect(3)}Tray {effect(1)}{trays[0]}{effect(22)} has been deleted.{effect(23)}")
                except IndexError:candel = True
                else:
                    del globals()[trays[0]]
                    trays.pop(0)
                    time.sleep(0.4)
                    candel = False
            if candel:print(f"Can't delete a tray.")
                
        else:break
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)
    print(f"{effect(3)}Program terminated.{effect(22)}")

if __name__ == "__main__":Program_run()