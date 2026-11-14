"""
※A creative title and explaination🥰
※Text effects, time module, and os module for emphasis and style
※May have been used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg7_Pinatubo_Espiritu.py because plagiarizing without crediting is bad, also sampleInheristance and sampleComposition notes.
※I regret this but it would be difficult but also uses chatgpt to make dynamic variables. ...and a little bit more for understanding ...
※#some comments
※Title for program kasi i am muon themed.
※BETTER VERSION: https://github.com/krey2030/CS3/blob/main/Q2/fa2_9-pinatubo_rey.intal.py
 → This version can't be uploaded alongside more files, so the function used from an imported file is moved directly here.

"""
from os import system as sys #makes it simple
from abc import *   
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        print(f"testing {self.varname}{self.Temp}{self.pH}")#my preference rather than pass

class TempSensor(Sensor):
    def get_reading(self):print(f"The temperature of beaker {self.varname} is {self.Temp}°C.")
    
class PHSensor(Sensor):
    def get_reading(self):print(f"{effect(22)}{effect(23)}{effect(4)}The pH of beaker {effect(1)}{self.varname}{effect(22)} is {effect(1)}{self.pH}{effect(22)}{effect(24)}")

class Glassware:
    def __init__(self, object_type="Glassware"):
        self.object_type = object_type
    
class Beaker(Glassware):
    def __init__(self, object_type="Glassware"):
        super().__init__(object_type)
        self.filled = False
        self.varname = None
    def fill(self, varname, Temp, pH):
        self.Temp = Temp
        self.pH = pH
        self.filled = True
        self.varname = varname
    def sense(self, SenseType):
        if self.filled:
            if SenseType == "temp":
                TempSensor.get_reading(self)
            elif SenseType == "ph":
                PHSensor.get_reading(self)
            else:Sensor().get_reading(self)#without the parenthesis, it doesnt work, but finally done WITHOUT AI
        
    def __str__(self):
        if self.filled:return f"Filled {effect(3)}Glassware{effect(23)} Beaker labeled {effect(1)}{self.varname}{effect(22)}"
        else:return f"{effect(1)}Empty {effect(3)}Glassware{effect(23)} Beaker{effect(22)}"

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
    print(f"You opened 『{effect(1)}Unstably Living Beakers:{effect(22)} {effect(3)}Stable Beaker Readings{effect(23)}』 program. You can organize a tray into existence that will compose 5 beakers.")
    time.sleep(0.5)
    print(f"You can delete the tray and view the trays too. This program trayns you for organizing the inventory.")
    time.sleep(0.5)
    print(f"The beakers are unstably living⏳, and travels vast distances, just like a 𝓂 𝓊𝑜𝓃 ⚛. They travel so vast they get lost into the system.")
    time.sleep(0.5)
    print(f"The beakers can now {effect(4)}be filled with a liquid; the liquid will have 2 properties: {effect(1)}pH{effect(22)} and {effect(1)}Temperature{effect(22)}{effect(24)}.")#main point of FA3
    time.sleep(0.5)
    print(f"{effect(4)}You can use a {effect(1)}sensor{effect(22)} that could either check the {effect(1)}temperature{effect(22)} or the {effect(1)}pH{effect(22)} of the liquid.{effect(24)}")#main point of FA3
    time.sleep(0.5)
    print(f"{effect(3)}...Yes, the tray itself will compose the beakers. When the tray is deleted, the beakers would also be lost.\n")
    time.sleep(0.5)
    trays = []
    while True:#Example Input
        print(f"{effect(22)}Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to create a tray, {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to delete a tray, {effect(1)}{effect(3)}f{effect(22)}{effect(23)} to fill a beaker, {effect(1)}{effect(3)}s{effect(22)}{effect(23)} to sense a beaker.")
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
        
        elif inventory == "f":
            try:pH = float(input(f"{effect(22)}{effect(23)}Input the pH of the liquid.{effect(1)}\n"))
            except ValueError:
                print(f"{effect(22)}{effect(3)}The pH must be an integer/decimal number between 0-14.{effect(23)}")
                time.sleep(0.1)
            else:
                try:Temp = float(input(f"{effect(22)}{effect(23)}Input the temperature of the liquid.【Only in °C】{effect(1)}\n"))
                except ValueError:
                    print(f"{effect(22)}{effect(3)}The temparature must be an integer/decimal number more than -273.15°C.{effect(23)}")
                    time.sleep(0.1)
                else:
                    if Temp > -273.15:
                        while True:
                            try:fills = int(input(f"{effect(22)}{effect(23)}Input the number of beakers to fill. You can only fill one tray.{effect(1)}\n"))#In a more advanced Lab Inventory System, the user might be able to input a different glassware
                            except ValueError:
                                print(f"{effect(22)}{effect(3)}Please input a whole number.{effect(23)}")
                                time.sleep(0.1)
                            else:
                                if fills < 0:
                                    print(f"{effect(22)}{effect(3)}Please input a whole number.{effect(23)}")
                                    time.sleep(0.1)
                                elif fills > 5:
                                    print(f"{effect(22)}{effect(3)}You cannot input more than 5 beakers. Please input a number between 0-5.{effect(23)}")
                                else:break
                        
                        print(f"{effect(22)}{effect(23)}List of trays:")
                        for tray in trays:print(f"{effect(1)}{tray}{effect(22)}")
                        trayview1 = input(f"Input the tray to fill its beakers with.\n{effect(1)}")
                        try:trays.index(trayview1)
                        except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{trayview1}{effect(22)} in the trays. No beakers were filled.{effect(23)}")
                        else:
                            if fills != 5:#must label
                                for fill in range(fills):
                                    varname = input(f"\n{effect(23)}{effect(22)}Add a {effect(1)}label{effect(22)} to your beaker—it must be unique.\nIf it is not unique, it would replace the liquid in the beaker with the same label.\n{effect(1)}")
                                    globals()[trayview1].beakers[fill].fill(varname, Temp, pH)#NOW MAKE IT BIG!!! i meant filled
                            else:
                                for fill in range(len(globals()[trayview1])):globals()[trayview1].beakers[fill].fill(Temp, pH)
                    else:print(f"{effect(22)}{effect(3)}The pH must be an integer/decimal number between 0-14.{effect(23)}")

        elif inventory == "s":
            SenseType = input(f"\n{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}Temp{effect(22)}{effect(23)} to check the temperature of the liquid in a beaker. Input {effect(1)}{effect(3)}pH{effect(22)}{effect(23)} to check the pH of the liquid.{effect(1)}{effect(3)}\n").lower()#inputting nothing will sense it generally...
            print(f"{effect(22)}{effect(23)}List of trays:")
            for tray in trays:print(f"{effect(1)}{tray}{effect(22)}")
            traysense1 = input(f"{effect(22)}{effect(23)}Input the tray to sense a beaker of.\n{effect(1)}")
            try:trays.index(traysense1)
            except ValueError:print(f"{effect(22)}{effect(3)}There is no {effect(1)}{traysense1}{effect(22)} in the trays. No beakers were filled.{effect(23)}")
            else:
                print(f"{effect(1)}{effect(3)}{traysense1}{effect(22)}{effect(23)} has:{effect(22)}")
                for _ in globals()[traysense1].beakers:
                    print(_)
                beakersense1 = input(f"{effect(22)}Input the label of the unique beaker to sense.\n{effect(1)}")
                for _ in range(len(globals()[traysense1].beakers)):
                    if globals()[traysense1].beakers[_].varname == beakersense1:break
                else:
                    _=-1
                    print(f"{effect(22)}{effect(3)}There is no unique {effect(1)}{beakersense1}{effect(22)} in the trays. No beakers were filled.{effect(23)}")
                if _ != -1:globals()[traysense1].beakers[_].sense(SenseType)
    
        elif inventory == "v":
            print()
            if len(trays) == 1:print(f"{effect(22)}{effect(23)}There is just a tray.")
            elif len(trays) == 0:print(f"{effect(22)}{effect(23)}Not a tray there are.")
            else:print(f"{effect(22)}{effect(23)}There are {len(trays)} trays.")
            for indivtray in trays:
                print(f"{effect(1)}{effect(3)}{indivtray}{effect(22)}{effect(23)} has:{effect(22)}")
                for _ in globals()[indivtray].beakers:
                    print(_)
                #print all the properties of each
        
        else:break
    input()
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)
    print(f"{effect(3)}Program terminated.{effect(22)}")

if __name__ == "__main__":Program_run()