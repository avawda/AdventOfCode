import datetime
import os
from collections import Counter

# PROBLEM STATEMENT
# https://adventofcode.com/2018/day/2

def hasTwo(boxID):
    for key,value in Counter(boxID).items():
        if value == 2: 
            return True
    return False

def hasThree(boxID):
    for key,value in Counter(boxID).items():
        if value == 3: 
            return True
    return False


print("*************")
print(os.path.basename(__file__))
print("*************")
answer = 0
start = datetime.datetime.now()

print("Started process : {}".format(start))

# Custom Problem code starts here
path = "C:/Users/vawdaa/OneDrive - Standard Bank/Python/AdventCode/"
file = open(path + "Day2_Input.txt","r")
data = file.readlines()

countDoubles = 0
countTriples = 0
for box in data:

    box = box.strip()
    if hasTwo(box):
        countDoubles += 1

    if hasThree(box):
        countTriples += 1  

    # print(Counter(box))  

answer = countDoubles*countTriples
print("Boxes have {} doubles and {} triples".format(countDoubles,countTriples))    

# Custom Problem code ends here

end = datetime.datetime.now()
print("Ended process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
