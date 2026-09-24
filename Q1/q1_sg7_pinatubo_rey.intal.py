"""
※A creative title and explaination🥰
※Text effects, time module, and os module for emphasis and style
※May have been used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg7_Pinatubo_Espiritu.py because plagiarizing without crediting is bad, also sampleInheristance and sampleComposition notes.
※I regret this but it would be difficult but also uses chatgpt to make dynamic variables. ...and a little bit more for understanding ...
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
    print(f"You opened {effect(1)}Unstably Living Beakers{effect(22)} program. You can organize a tray into existence that will compose 5 beakers.")
    time.sleep(0.5)
    print(f"You can delete the tray and view the trays too. This program trayns you for organizing the inventory.")
    time.sleep(0.5)
    print(f"The beakers are unstably living⏳, and travels vast distances, just like a 𝓂𝓊𝑜𝓃⚛. They travel so vast they get lost into the system.")
    time.sleep(0.5)
    print(f"{effect(3)}...Yes, the tray itself will compose the beakers. When the tray is deleted, the beakers would also be lost.")
    time.sleep(0.5)
    print(f"Also the beaker does nothing. It simply exists and gets lost when the tray is deleted.{effect(23)}\n") 
    time.sleep(0.5)
    trays = []
    while True:#Example Input
        print(f"{effect(22)}Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to create a tray, {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to delete a tray.")
        inventory = input(f"Input {effect(1)}{effect(3)}v{effect(22)}{effect(23)} to view current trays. Otherwise, program would be terminated.{effect(1)}{effect(3)}").lower()
        time.sleep(0.5)
        if inventory == "y":#create a tray
            varname = input(f"\n{effect(22)}{effect(23)}Name your tray with a unique name.\nIf it is not unique. it would replace the first tray.\n{effect(1)}")
            trays.append(varname)
            globals()[varname] = Tray()
            trays = list(dict.fromkeys(trays))
            time.sleep(0.5)
        elif inventory == "x":
            print()
            while True:
                try:traydel = int(input(f"{effect(22)}{effect(23)}How many trays would you delete?\n"))
                except ValueError:print(f"{effect(3)}Please input an integer.")
                else:
                    if traydel < 0:print(f"{effect(3)}Please input a non-negative number.")
                    else:break
            time.sleep(0.4)
            candel = False
            for indivtray in range(traydel):
                try:print(f"Tray {effect(1)}{trays[0]}{effect(22)} has been deleted.")
                except IndexError:candel = True
                else:
                    del globals()[trays[0]]
                    trays.pop(0)
                    time.sleep(0.4)
                    candel = False
            if candel:print(f"Can't delete any more trays.\n")
        elif inventory == "v":
            print()
            if len(trays) == 1:print(f"{effect(22)}{effect(23)}There is just a tray.")
            elif len(trays) == 0:print(f"{effect(22)}{effect(23)}Not a tray there are.")
            else:print(f"{effect(22)}{effect(23)}There are {len(trays)} trays.")
            for indivtray in trays:
                print(f"{effect(1)}{effect(3)}{indivtray}{effect(22)}{effect(23)} with {effect(1)}{len(globals()[indivtray].beakers)} {effect(3)}{Beaker().object_type}{effect(23)} beakers{effect(22)}")
        else:break
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)
    print(f"{effect(3)}Program terminated.{effect(22)}")

if __name__ == "__main__":Program_run()
