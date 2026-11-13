"""
※INCOMPLETE but not important

"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

from abc import *

class Sensor(ABC):
    @abstractmethod
    def get_data(self):None

class TempSensor(Sensor):
    def get_data(self):return "26 °C"
    def __str__(self):
        return "26 °C"

def Program_run():#starts program and simple explanation
    sys("cls")
    time.sleep(0.5)
    
    tempSensor = TempSensor()
    print(tempSensor)
    

    input()
    time.sleep(0.5)
    print(f"{effect(3)}Program terminated.{effect(0)}")
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    print(f"{effect(3)}Program terminated.{effect(0)}")

if __name__ == "__main__":Program_run()
