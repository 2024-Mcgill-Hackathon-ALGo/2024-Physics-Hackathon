from DecayingElement import DecayingElement
from Element import Element
from DecayType import DecayType

pb206 = Element("Pb", "Lead", 82, 206)

po210 = DecayingElement("Po", "Polonium", 84, 210, {DecayType.ALPHA: pb206})
ti206 = DecayingElement("Ti", "Titanium", 22, 206, {DecayType.BETA_MINUS: pb206})

hg206 = DecayingElement("Hg", "Mercury", 80, 206, {DecayType.BETA_MINUS: ti206})
bi210 = DecayingElement("Bi", "Bismuth", 83, 210, {DecayType.ALPHA: ti206, DecayType.BETA_MINUS: po210})

pb210 = DecayingElement("Pb", "Lead", 82, 210, {DecayType.BETA_MINUS: bi210, DecayType.ALPHA: hg206})

        