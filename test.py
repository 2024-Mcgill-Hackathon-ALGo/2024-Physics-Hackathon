import radioactivedecay as rd
import matplotlib.pyplot as plt

# Create a Nuclide object for U-235
u235 = rd.Nuclide('U-235')
print(rd.Nuclide('U-235').activities)


# Plot the decay chain of U-235
# u235.plot()

# # Adjust layout to increase spacing
# plt.title("Decay Chain of U-235", fontsize=16)
# plt.subplots_adjust(left=0.1, right=0.9, top=2, bottom=0.1)  # Adjust these values to your preference
# plt.tight_layout()
# plt.show()
