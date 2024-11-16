class Element:
    # region constructeurs
    def __init__(self, symbol, name, atomic_number, atomic_weight):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_weight
    # endregion constructeurs 
             
    # region méthodes
    
    def equals(self, other):
        return self.symbol == other.symbol and self.name == other.name and self.atomic_number == other.atomic_number and self.atomic_weight == other.atomic_weight
    
    # endregion méthodes