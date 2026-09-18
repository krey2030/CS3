"""
※Formatted with functions for organization
※Scrapped __del__ function :C
※Text effects, time module, and os module for emphasis and style
※Used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg5_a1_Pinatubo_Espiritu.py
※#comments
"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

class Hero():
    def __init__(self, name: str, HP: float):
        self.name = name
        self.HP = HP #is supposed to return ValueError since it is not input
        self.ogHP = HP
    def take_damage(self, amount: float):
        self.HP -= amount
    def __str__(self):
        #if self.HP <= 0:del self #Didn't worked, limited time
        return f"Hero {effect(1)}{self.name}{effect(22)}'s attributes:\n{effect(3)}current HP{effect(23)}: {effect(1)}{self.HP}{effect(22)}"+f"\n{effect(3)}max HP{effect(23)}: {effect(1)}{self.ogHP}{effect(22)}\n{effect(3)}% HP{effect(23)}: {effect(1)}{100*self.HP/self.ogHP}%{effect(22)}\n"
    """#Didn't worked, limited time
    def __del__(self):
        print(f"{self.name}'s HP went down. {self.name} has been annihilated.")"""

def Program_run():#starts program and simple explanation
    print(f"You opened {effect(1)}The RPG Hero{effect(22)} program. This program simply shows HP of two created heroes.")
    
    hero1_Arthur = Hero("Arthur", 100)
    hero2_Morgana = Hero("Morgana", 100)

    hero1_Arthur.take_damage(10)

    print(hero1_Arthur)
    print(hero2_Morgana)

    input(f"\nPress enter to terminate program.")
    time.sleep(2)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb

if __name__ == "__main__":Program_run()