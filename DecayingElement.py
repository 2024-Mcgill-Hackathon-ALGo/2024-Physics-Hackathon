from Element import Element

class DecayingElement(Element):
    def __init__(self, symbol, name, atomic_number, atomic_weight, possible_decays):
        super().__init__(symbol, name, atomic_number, atomic_weight)
        
        # possible decays should be a dictionnary with this structure:
        # {decay_type: child isotope}
        # example: {"alpha": "He"}
        # example: {"beta-": "B"}
        # example: {"beta+": "C"}
        self.possible_decays = possible_decays
        
    def decay(self, decay_type):
        if decay_type in self.possible_decays:
            self.fetchDecayingElementData(self.possible_decays[decay_type])
        else:
            print(f"Decay type {decay_type} not possible for {self.symbol}")
            
    def fetchDecayingElementData(self, symbol):
        # fetch data from json
        pass