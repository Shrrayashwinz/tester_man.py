'''
Program Name: Lab3_ssrinivasan3_replace.py

Author: Shrrayash Srinivasan

Purpose of this program: I must replace one string object with a specific object - 'binoculars' - while doing the usual
import of the project 2 and add it to project 3

Date: September 10, 2025
'''
# Get the import from project 2 [WITHOUT COPYING AND REPLACING IT]
from Lab3_ssrinivasan3_add import camping_stuff

# Replace 'Flashlight' with 'binoculars'
camping_stuff.pop(2)
camping_stuff.insert(2, 'Binoculars')

# Print the new list
print ((camping_stuff))

print("Flashlight has been replace with binoculars")
