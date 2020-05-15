import time
from bisect import bisect_left 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''
# old version
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
# the older version is a polynomial runtime operation O(n^c)

# My version O(n log n)

names_1.sort()

def BinarySearch(names_1, name): 
    i = bisect_left(names_1, name) 
    if i != len(names_1) and names_1[i] == name: 
        return i 
    else: 
        return -1
  
for name in names_2:
    res = BinarySearch(names_1, name) 
    if res == -1:
        pass
    else:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
