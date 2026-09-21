class hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def takeDamage(self, amount):
        self.hp -= amount

arthur = hero("Arthur", 100)
morgana = hero("Morgana", 100)
arthur.takeDamage(10)
print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")
