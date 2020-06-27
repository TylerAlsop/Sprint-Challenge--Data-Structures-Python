import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

########## Pseudo Code ##########
# Create a binary search tree class. It will need insert and contains functions.
    #****** Done. See import at top of page. ******
# Initialize a binary search tree with an empty string for the initial value.
bst = BSTNode("")
# Take all of the names in names_1 file and use the bst.insert() method to add them to the tree.
for name_from_names_1 in names_1:
    bst.insert(name_from_names_1)
# Use the bst.contains() methods to check the bst for names from names_2 file.
    # If the bst already contains a name in names_2 file then add it to the "duplicates" list above using the append() method.
for name_from_names_2 in names_2:
    if bst.contains(name_from_names_2):
        duplicates.append(name_from_names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
