def effect(Effect: int): #text style for bold, italic, underlines, etc.
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removed bold, #23 removes italic, #24 = removes underline
#car
class Car:
    def __init__(self,brand,model,battery=35):
        self.brand = brand
        self.model = model
        self.battery = battery
        print(f"You've created a {self.brand}, {self.model}")
    def go(self,distance):
        self.battery -= distance/20
        print(f"{effect(22)}{effect(23)}You traveled",distance,"KM")
        print(f"{effect(22)}{effect(23)}You have {self.battery} wH left")
    def charge(self,wH):
        self.battery += wH
        print("You charged",wH,"wH")

car = Car("Geely","EX5")
while car.battery > 0:
    act = input(f"{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}y{effect(22)}{effect(23)} to drive. Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to charge car. {effect(1)}{effect(3)}\n").lower()
    if act == "y":
        distance = float(input(f"{effect(22)}{effect(23)}How far【KM】? {effect(1)}"))
        car.go(distance)
    elif act == "x":
        charge = float(input(f"{effect(22)}{effect(23)}How much to charge【wH】? {effect(1)}"))
        car.charge(charge)
    else:print(f"{effect(22)}Invalid action")
else:print(f"{effect(22)}{effect(3)}Game over. You ran out of batteries.")