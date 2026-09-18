"""
※Formatted using functions for organization
※Alternate solution but conflicts with the use of selection structure to determine the chinese zodiac sign and displaying the correct output
so original and expected solution is retained.
※Text effects, time module, and os module for emphasis and style
※#comments everywhere
※Title for program kasi i am muon themed.
"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

def Program_run():#starts program and simple explanation
    print(f"{effect(0)}You opened the 『Zodiac:{effect(1)}Muonkey 【猴 / Hóu】』{effect(22)} Program.")#intentional spelling.
    time.sleep(0.5)
    print(f"This program simply lets you know your chinese zodiac sign, given the year of birth.")
    time.sleep(0.5)
    yearinput()
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb


def yearinput():#a. Ask the user to enter a year of birth.  The baseline year 1900.
    try:birthyear = int(input(f"Input your birth year:\t{effect(1)}"))
    except ValueError:print(f"{effect(22)}{effect(3)}Please input a natural number only.")
    else:
        if birthyear >=1900:determination(birthyear)#   d. Otherwise
        else:print(f"{effect(22)}{effect(3)}Please input a year {effect(1)}not{effect(22)} earlier than {effect(1)}1900{effect(22)}.{effect(23)}")#b. Validate user input that it should not be earlier than 1900.
    #c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

def determination(birthyear):#determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.
    """
    #Alternate solution using lists makes it efficient and less repetitive.
    #However, it does not follow the rubrics regarding the use of selection structure to determine the chinese zodiac sign and displaying the correct output.
    zodiac = ["Rat【鼠 / Shǔ】"     ,   "Ox 【牛 / Niú】"   ,   "Tiger【虎 / Hǔ】", "Rabbit【兔 / Tù】" ,
              "Dragon 【龙 / Lóng】",   "Snake【蛇 / Shé】" ,   "Horse【马 / Mǎ】", "Goat 【羊 / Yáng】",
              "Monkey【猴 / Hóu】"  ,   "Rooster【鸡 / Jī】",   "Dog 【狗 / Gǒu】", "Pig【猪 / Zhū】"   ]
    i = (birthyear - 1900) % 12
    print(f"{effect(22)}Your Chinese Zodiac Sign is :", zodiac[i])
    """
    #This solution follows the use of selection structure to determine the chinese zodiac sign and displaying the correct output
    #But it conflicts with code efficiency. Alternate solution above uses lists and indexes instead.
    print(f"{effect(22)}Your chinese Zodiac sign is:" ,end="\t")
    zodiac = ((birthyear - 1900) % 12) + 1
    match zodiac:
        case 1:print("Rat【鼠 / Shǔ】")
        case 2:print("Ox 【牛 / Niú】")
        case 3:print("Tiger【虎 / Hǔ】")
        case 4:print("Rabbit【兔 / Tù】")
        case 5:print("Dragon 【龙 / Lóng】")
        case 6:print("Snake【蛇 / Shé】")
        case 7:print("Horse【马 / Mǎ】")
        case 8:print("Goat 【羊 / Yáng】")
        case 9:print("Monkey【猴 / Hóu】")
        case 10:print("Rooster【鸡 / Jī】")
        case 11:print("Dog 【狗 / Gǒu】")
        case 12:print("Pig【猪 / Zhū】")
    time.sleep(0.2)
    input(f"\nPress enter to terminate program.")

sys("cls")#"cls" for VSCode, "clear" for onlinegdb
Program_run()
