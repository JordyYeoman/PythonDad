print("Day 1: Not Quite Lisp")
startingFloor = 0

# run tests
testSet = ['(','(',')','(','(',')','(']

# Python map
movements = { 
    '(' : 1,
    ')' : -1
}

# for t in testSet:
#     startingFloor += movements[t]
# startingFloor = 0

file = open('day1.txt', 'r')
 
while 1:
    # read by character
    char = file.read(1)         
    if not char:
        break
    # do stuff      
    startingFloor += movements[char]

print(startingFloor)

# send it
file.close()