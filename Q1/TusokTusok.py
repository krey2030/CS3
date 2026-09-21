class tusokTusok:
    name = ""
    sauce = []
    def __init__(self, name):
        self.name = name
    def dip(self, sauce):
        self.sauce.append(sauce)
    def eat(self):
        print("I ate", self.name, "with", end=" ")
        [print(s.name, end=", ") for s in self.sauce]
        print("and it tastes", end=" ")
        [print(s.taste, end=", ") for s in self.sauce]
        print()
class Sauce:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

fishball = tusokTusok("fishball")
vinegar = Sauce("vinegar", "sour")
sweet = Sauce("sweet sauce", "sweet")
spicy = Sauce("spicy sauce", "spicy")
fishball.dip(vinegar)
fishball.dip(sweet)
fishball.eat()#test
