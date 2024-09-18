'''Assume each pizza has 8 slices. Assuming that there is a family of 4.Ask how
many slices everyone in the family eats.Then calculate how many whole pizzas are
required for a family of 4 for one meal? How many are the leftover slices?
So if everyone is eating 3 slices you need 2 pizzas with 4 leftover slices.'''

# Constants for pizza slices and family size
slices_per_pizza = 8
family_size = 4

# Input: number of slices each person eats
slices_per_person = int(input("how many slices does each person eat? "))

# Total slices needed
total_slices_needed = slices_per_person * family_size

# Calculate the number of pizzas required and leftover slices
pizzas_needed = total_slices_needed // slices_per_pizza
leftover_slices = total_slices_needed % slices_per_pizza

# If there are leftover slices, add one more pizza to cover those slices
if leftover_slices > 0:
    pizzas_needed += 1

# Calculate the actual leftover slices after adding extra pizza
actual_leftover_slices = pizzas_needed * slices_per_pizza - total_slices_needed

# Output results
print(f"Number of pizzas required: {pizzas_needed}")
print(f"Leftover slices: {actual_leftover_slices}")

