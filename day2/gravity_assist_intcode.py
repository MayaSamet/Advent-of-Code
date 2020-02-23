# Advent of Code - Day 2
import numpy as np

### part 1
intcode = np.loadtxt('day2_input.txt', dtype = int, delimiter=",")

# replace position
intcode[1] = 12
intcode[2] = 2

# opcode function
i=0
while intcode[i] != 99:
    if intcode[i] == 1:
        intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        i += 4
    elif intcode[i] == 2:
        intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        i += 4
    else:
        print("something went wrong!")
        break;

print("Day 2 part 1 solution: " + str(intcode[0]))
