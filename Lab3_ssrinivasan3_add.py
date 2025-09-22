"""
Program Name: Lab3_ssrinivasan3_add.py

Author: Shrrayash Srinivasan

Purpose of this program: I must import the project file from Project 1 and add 5 more items to it.

Date: September 10, 2025

"""
#Import project from project 1 (don't copy and paste it)
from Lab3_ssrinivasan3_list import camping_stuff

# Add 5 more items to the list 
more_stuff = ["First Aid Kit", "Wolf Urine", "Canteens", "Fishing Rods", "Snacks"]

camping_stuff.extend(more_stuff)

#Print the modified list
print((camping_stuff))

print("The new total of items in the list is now", (len(camping_stuff)))
                     
        
