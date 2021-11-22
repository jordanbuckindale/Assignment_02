"""
Assignment #2
Course: 1026A
Due Date: Oct 20th 2021
Description: This program will contain the functions of the program.

Created by: Jordan Buckindale
Student #: 251246279
"""


def basicCode(numVal):
    stringNum = str(numVal)
    lastValue = stringNum[-1]
    num = stringNum[:-1]
    sum = 0
    for n in num:
        sum += int(n)
    if (sum % 10) == int(lastValue):
        return True
    else:
        return False


def positionalCode(numVal):
    stringNum = str(numVal)
    lastValue = stringNum[-1]
    num = stringNum[:-1]
    numberPosition = 1
    u = 0
    for t in num:
        stringMult = (int(t) * numberPosition)
        u = u + stringMult
        numberPosition += 1
    if (u % 10) == int(lastValue):
        return True
    else:
        return False


def universalProductCode(numVal):
    stringNum = str(numVal)
    lastValue = stringNum[-1]
    num = stringNum[:-1]
    sum = 0
    numberPosition = 1
    for n in num:
        if n.isdigit():
            if numberPosition % 2 == 0:
                sum += int(n)
                numberPosition += 1
            else:
                sum += int(n) * 3
                numberPosition += 1
    if 1 <= (sum % 10) <= 9:
        completeCheckDigit = 10 - (sum % 10)
    else:
        completeCheckDigit = 0

    if completeCheckDigit == int(lastValue):
        return True
    else:
        return False
