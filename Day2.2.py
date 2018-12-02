import datetime
import os
from collections import Counter

# PROBLEM STATEMENT
# https://adventofcode.com/2018/day/2#part2

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

maxLen = 24
maxI = 0
maxJ = 0
maxCommon = []
for box1 in data:
    box1 = box1.strip()
    for box2 in data:
        box2 = box2.strip()
        if box1 != box2:
            common = 0
            commonSet = ""
            for i in range(len(box1)):
                if box1[i] == box2[i]:
                    common+=1
                    commonSet+=box1[i]
                if common > maxLen:
                    maxLen = common
                    maxCommon = commonSet
                    maxI = box1
                    maxJ = box2
                    print(box1)
                    print(box2)
                    print(maxLen)
                    print("*******************************************")
                    #print("{} overlaps {} by {}".format(box1,box2,maxLen))
 
answer = maxCommon

# Custom Problem code ends here

end = datetime.datetime.now()
print("Ended process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
