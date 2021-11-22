"""
Assignment #2
Course: 1026A
Due Date: Oct 20th 2021
Description: # The program will determine whether a basic identification number
             is a valid Basic Code, a Positional Code or a UPC Code.

Created by: Jordan Buckindale
Student #: 251246279
"""

# import functions
from code_check import basicCode, positionalCode, universalProductCode

# lists
BasicCode_list = []
PositionalCode_list = []
UniversalCode_list = []
OtherCode_list = []

# prompt user input
numVal = input("Please enter code (digits only) (enter 0 to quit) ")

while int(numVal) != 0:
    basicCodeValue = basicCode(numVal)  # Basic Code Function
    if basicCodeValue is True:
        BasicCode_list.append(numVal)
        print(f"-- code: {numVal} valid Basic code.")

    PositionalCodeValue = positionalCode(numVal)  # Positional Code Function
    if PositionalCodeValue is True:
        PositionalCode_list.append(numVal)
        print(f"-- code: {numVal} valid Position code.")

    upcCodeValue = universalProductCode(numVal)  # Universal Code Function
    if upcCodeValue is True:
        UniversalCode_list.append(numVal)
        print(f"-- code: {numVal} valid UPC code.")

    if not universalProductCode(numVal) and not positionalCode(numVal) and not basicCode(numVal):  # other
        OtherCode_list.append(numVal)
        print(f"-- code: {numVal} not Basic, Position or UPC code.")

    numVal = input("Please enter code (digits only)(enter 0 to quit) ")

# print output
print("\nSummary")

if len(BasicCode_list) == 0:
    print("Basic : None")
else:
    print("Basic :", ', '.join(map(str, BasicCode_list)))

if len(PositionalCode_list) == 0:
    print("Position : None")
else:
    print("Position :", ', '.join(map(str, PositionalCode_list)))

if len(UniversalCode_list) == 0:
    print("UPC : None")
else:
    print("UPC :", ', '.join(map(str, UniversalCode_list)))

if len(OtherCode_list) == 0:
    print("None: None")
else:
    print('None :', ', '.join(map(str, OtherCode_list)))
