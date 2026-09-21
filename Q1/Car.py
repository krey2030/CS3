class Car: 
    def __init__(self, brand, model, battery=35):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        self.battery -= distance/20
        print("The car traveled",distance,"km")
        print("You have",self.battery,"wH left")
    def charge(self, wH):
        self.__battery += wH
        print("Car recharged. You now have",self.battery,"wH")

car = Car("Geely", "EX5")
while car.battery > 0:
    act = input("What do you want to do? (g or c)")
    if act == "g":
        distance = int(input("How far? "))
        car.go(distance)
    elif act == "c":
        wH = int(input("How much to charge? "))
        car.charge(wH)
    else:
        print("Invalid Action")

print("Game over. You ran out of batteries")

