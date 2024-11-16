import radioactivedecay as rd
from collections import defaultdict

decay_data = rd.DEFAULTDATA
nuclides_by_element = defaultdict(list)

# get all isotopes and add them to the dictionary
for nuclide in decay_data.nuclides:
    if decay_data.half_life(nuclide) != float('inf'):
        element_symbol = ''.join(filter(str.isalpha, nuclide))
        nuclides_by_element[element_symbol].append(nuclide)

# Sort the nuclides by element
for element in nuclides_by_element:
    nuclides_by_element[element].sort()

# Convert the defaultdict to a regular dictionary
nuclides_by_element = dict(nuclides_by_element)


def printIsotopes(element):
    for element, nuclides in sorted(nuclides_by_element.items()):
        if element == element:
            print(f"{element}: {', '.join(nuclides)}")

def returnIsotopeDictionary():
    return nuclides_by_element

def returnIsotopes(element):
    return nuclides_by_element[element]