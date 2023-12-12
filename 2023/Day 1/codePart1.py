# Advent of Code 2023
# Day 1 Trebuchet?! Part 1
# author: a9enad

# extract first digit from line
def findFirstDigit(line):
    digit = False
    while not digit:
        for char in line:
            if char.isdigit():
                digit = True
                return char


def readCalibrationValue(lines):
    sum = 0
    # iteration over lines
    for line in lines:
        # extract first and last digits
        firstDigit = findFirstDigit(line)
        lastDigit = findFirstDigit(reversed(line))

        # calculate sum
        if firstDigit and lastDigit:
            num = int(firstDigit + lastDigit)
            sum += num
    return sum

# read lines from file
def readFile(file):
    with open(file, "r") as rf:
        lines = rf.readlines()
        return readCalibrationValue(lines)


result = readFile("input.txt")
print(result)
