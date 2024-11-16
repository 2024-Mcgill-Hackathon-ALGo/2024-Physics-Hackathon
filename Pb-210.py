from DecayingElement import DecayingElement
from Element import Element

pb206 = Element("Pb", "Lead", 82, 206)

po210 = DecayingElement("Po", "Polonium", 84, 210, {"alpha": pb206})
ti206 = DecayingElement("Ti", "Titanium", 22, 206, {"beta-": pb206})

hg206 = DecayingElement("Hg", "Mercury", 80, 206, {"beta-": ti206})
bi210 = DecayingElement("Bi", "Bismuth", 83, 210, {"alpha": ti206, "beta-": po210})

pb210 = DecayingElement("Pb", "Lead", 82, 210, {"beta-": bi210, "alpha": hg206})

        