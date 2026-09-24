"""COMPOSITION"""
class Nucleus:
    def __init__(self):
        print("Nucleus created")
    def __del__(self):
        print("Nucleus is gone")
    
class Mitochondria:
    def __init__(self):
        print("Mitochondria created")
    def powerTheCell(self):
        print("Mitochondria is providing energy")
    def __del__(self):
        print("Mitochondria is gone")

class Cell:
    def __init__(self):
        print("Cell created")
        self.Nucleus = Nucleus()
        self.Mitochondria = Mitochondria()
    def exist(self):
        print("Cell is existing")
        self.Mitochondria.powerTheCell()
    def __del__(self):
        del self.Nucleus
        del self.Mitochondria
        print("Cell is gone")
        
cellAtWork = Cell()
cellAtWork.exist()
del cellAtWork
