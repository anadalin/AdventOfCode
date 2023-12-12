# Advent of Code 2023
# Day 2 Cube Conundrum Part 2
# author: a9enad

#Test Data
'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

def readFile(file):
    with open(file, 'r') as rf:
        lines = rf.readlines()
    return lines


def powerMinCubesPossible(game):
    maxReveal = {'red': 0, 'green': 0, 'blue': 0}
    power = ''
    newline = game.strip('\n')
    reveals = newline.split('; ')
    #Update number of cubes based colours from reveal
    for reveal in reveals:
        for cubes in reveal.split(', '):
            numOfCubes, colour = cubes.split(' ')
            maxReveal[colour] = max(maxReveal[colour],int(numOfCubes))
    # Calculate power of number of cubes from each colour
    power = maxReveal['red'] * maxReveal['green'] * maxReveal['blue']  
    return power

def sumPower(path):
    total = 0
    for line in path:
        gameID, gameInfo = line.split(': ')
        name, ID = gameID.split(' ')
        total += powerMinCubesPossible(gameInfo)

    return total

file = readFile("input.txt")
total = sumPower(file)
print(total)