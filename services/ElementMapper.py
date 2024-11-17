import radioactivedecay as rd
from model.DecayingElement import DecayingElement
from model.DecayType import DecayType

#Mapper that turns an element string like ("Pb-210" or "U-235") into a DecayingElement object with a map that has the possible decays associated to the decaying element those
#decays lead to 
class mapper:
    def __init__(self):
        print("Mapper created")
    
    @staticmethod
    def toDecayingElement(elementString):
        fetchedElement = rd.Nuclide(elementString)
        
        elementSymbol = elementString[:2]
        
        atomic_number = fetchedElement.Z
        atomic_weight = fetchedElement.A
        
        possible_decays: {DecayType, DecayingElement} = {}
        
        for a, b in zip(fetchedElement.decay_modes(), fetchedElement.progeny()):
            # print(a, b)
            if(a == "α"):
                possible_decays[DecayType.ALPHA] = mapper.toDecayingElement(b)
            elif(a == "β-"):
                possible_decays[DecayType.BETA_MINUS] = mapper.toDecayingElement(b)
            elif(a == "β+"):
                possible_decays[DecayType.BETA_PLUS] = mapper.toDecayingElement(b)
            
        half_life = fetchedElement.half_life('y')
        
                
        return DecayingElement(elementSymbol, atomic_number, atomic_weight, possible_decays, half_life)


# Example usage with debugging methodes that are in decayinElement.py
# helloWorld = toDecayingElement("Pb-210")
# helloWorld.helloWorld()
# helloWorld.printDecayers()

# var = "test"
# print(var[:2]) # te