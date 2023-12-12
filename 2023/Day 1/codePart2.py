# Advent of Code 2023
# Day 1 Trebuchet?! Part 2
# author: a9enad

#Test Data
'''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
423oneight
'''

# extract first digit from line
def findFirstDigit(line):
    digit = False
    while not digit:
        for char in line:
            if char.isdigit():
                digit = True
                return char

# replace word with digit in line
def replaceWordWithDigit(line):
    replacement = {
        'one': 'o1e',
        'two': 't2o', 
        'three': 't3e',
        'four': '4', 
        'five': '5e', 
        'six': '6',
        'seven': '7n', 
        'eight': 'e8t', 
        'nine': 'n9e',
        'zero': '0o'
        }
    for key, value in replacement.items():
        line = line.replace(key, value)
    return line


def readCalibrationValue(lines):
    sum = 0
    # iteration over lines
    for line in lines:
        # replace word with digit
        # before = line
        line = replaceWordWithDigit(line)
        # print(before +" replaced with " + line)
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