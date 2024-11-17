import radioactivedecay as rd
import matplotlib.pyplot as plt

# Create a Nuclide object for U-235
# u235 = rd.Nuclide('U-235')
# print(u235.decay_data)


# # Plot the decay chain of U-235
# u235.plot()

# # # Adjust layout to increase spacing
# plt.title("Decay Chain of U-235", fontsize=16)
# plt.subplots_adjust(left=0.1, right=0.9, top=2, bottom=0.1)  # Adjust these values to your preference
# plt.tight_layout()
# plt.show()

import radioactivedecay as rd

# Replace 'U-238' with the desired radionuclide
nuclide = rd.Nuclide('Pb-208')


daughters = nuclide.progeny()
print(daughters)

decay_modes = nuclide.decay_modes()
print(decay_modes)

# atomic_number = nuclide.Z
# print(atomic_number)



# Access the default decay dataset
decay_data = rd.DEFAULTDATA


# Get a list of all radionuclides
# radionuclides = decay_data.nuclides
# print(f"Total number of radionuclides: {len(radionuclides)}")
# print(radionuclides)


# # Filter for radioactive nuclides
# radioactive_nuclides = [
#     nuclide for nuclide in radionuclides
#     if decay_data.half_life(nuclide) != float('inf')
# ]
# print(f"Total number of radioactive nuclides: {len(radioactive_nuclides)}")
# print(radioactive_nuclides)

from collections import defaultdict

# Initialize a dictionary to hold nuclides by element
nuclides_by_element = defaultdict(list)

# Iterate through all nuclides in the dataset
for nuclide in decay_data.nuclides:
    # Check if the nuclide is radioactive
    if decay_data.half_life(nuclide) != float('inf'):
        # Extract the element symbol (e.g., 'U' from 'U-238')
        element_symbol = ''.join(filter(str.isalpha, nuclide))
        # Append the nuclide to the corresponding element list
        nuclides_by_element[element_symbol].append(nuclide)

# Sort the nuclides within each element
for element in nuclides_by_element:
    nuclides_by_element[element].sort()

# Convert the defaultdict to a regular dictionary for display
nuclides_by_element = dict(nuclides_by_element)

# Display the sorted radioactive nuclides by element
for element, nuclides in sorted(nuclides_by_element.items()):
    print(f"{element}: {', '.join(nuclides)}")