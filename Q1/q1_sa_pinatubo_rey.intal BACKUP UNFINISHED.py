"""
※Text effects, time module, and os module for emphasis and style
※#some comments
※Title and simple explanation
※very very incomplete though :(
"""
from os import system as sys #makes it simple
import time
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline

class Bank:
    def __init__(self, name: str):
        print(f"Welcome to {effect(1)}{name}{effect(22)}. This is a banking system.")
    def showAccounts(self):
        print(f"※ACCOUNT DETAILS")
        #UNDONE
    def openAccount(self):
        print(f"Ready to open an account")
        self.Account = Account(None, None)
    def closeAccount(self):
        print(f"Ready to close an account")
        while True:
            try:accclose = int(input(f"{effect(22)}{effect(23)}Enter account number: {effect(1)}"))
            except ValueError:print(f"{effect(3)}Please try again.{effect(23)}")
            else:break
        del self.Accounty
    def deposit(self):
        self.Account = Account()
    def withdraw(self):
        self.Account = Account()
    def addInterest(self):
        None
    def __del__(self):
        None

class Account:
    def __init__(self, name:str, number:int, __balance = 0):
        self.name=input(f"Account name: {effect(1)}").upper()
        self.__balance=0
        while True:
            try:self.number = int(input(f"{effect(22)}{effect(23)}Account number: {effect(1)}"))
            except ValueError:print(f"{effect(3)}Please try again.{effect(23)}")
            else:break
        print(self)#RETURNS AN ERROR
    def getBalance(self):
        None
    def deposit(self, __balance):None
        #self.__balance = __balance
        #__balance = __balance + float(input(f""))
    def withdraw(self, __balance):None
        #self.__balance = __balance
        #__balance = __balance - float(input(f""))
    def __str__(self):#HAS ERROR
        return f"{self.name} [{self.number}] P {self.__balance}"
    def __del__(self):
        None

class SavingsAccount(Account):
    None
    
def Program_run():#starts program and simple explanation
    sys("cls")
    muonbank = Bank("Muonbank")
    while True:
        print(f"Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to open an account, {effect(1)}{effect(3)}v{effect(22)}{effect(23)} to show accounts, and {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to close an account.")
        actions = input(f"Input {effect(1)}{effect(3)}d{effect(22)}{effect(23)} or {effect(1)}{effect(3)}w{effect(22)}{effect(23)} to deposit or withdraw to an account respectively.").lower()
        if actions == "y":muonbank.openAccount()
        elif actions == "v":muonbank.showAccounts()
        elif actions == "x":muonbank.closeAccount()
        elif actions == "d":None#muonbank.deposit()
        elif actions == "w":None#muonbank.withdraw()
        else:break
    input(f"\nPress enter to terminate program.")
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)

if __name__ == "__main__":Program_run()