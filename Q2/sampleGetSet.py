"""
※INCOMPLETE

"""
from os import system as sys #makes it simple
import time
from important_module import *#REQUIRED TO DOWNLOAD "important_module"

class Student:
    def __init__(self,__name):
        self.__name = __name
    def set_name(self,__name):self.__name=__name
    def get_name(self):return self.__name
    def set_age(self,__age):
        if __age>0:self.__age=__age
        else:self.__age=0
    def get_age(self):return self.__age
    def greet(self):return f"Hi! My name is {self.__name}"

def Program_run():#starts program and simple explanation
    sys("cls")
    time.sleep(0.5)
    
    time.sleep(1)

    print(f"{effect(3)}Program terminated.{effect(0)}")
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb

if __name__ == "__main__":Program_run()
