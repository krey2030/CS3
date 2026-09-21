class Glassware:
    def __init__(self, material="Glass"):
        self.material = material


class Beaker(Glassware):
    def __init__(self, capacity_ml, material="Glass"):
        super().__init__(material)
        self.capacity_ml = capacity_ml


class Tray:
    def __init__(self, beaker_capacity=250):
        self.beakers = [Beaker(capacity_ml=beaker_capacity) for _ in range(5)]

if __name__ == "__main__":
    my_tray = Tray(500)
    print(f"Tray created with {len(my_tray.beakers)} beakers.")
    print(f"Beaker 1 Capacity: {my_tray.beakers[0].capacity_ml}ml")
    print(f"Beaker 1 Material (inherited): {my_tray.beakers[0].material}")
