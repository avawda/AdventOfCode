import datetime
import os

# PROBLEM STATEMENT
#


print("*************")
print(os.path.basename(__file__))
print("*************")
answer = 0
start = datetime.datetime.now()

print("Started process : {}".format(start))


# Custom Problem code starts here
file = open("Day3_Test.txt","r")
data = file.readlines()
for claim in data:
    claim = claim.strip()
    topLeftX = claim[claim.find(",")+1]
    topleftY = claim[claim.find("@")+2]
    sizeX = claim[claim.find("x")-1]
    sizeY = claim[claim.find("x")+1]
    print("{} | {},{} | {}x{}".format(claim,topLeftX,topleftY,sizeX,sizeY))
# Custom Problem code ends here

print()
end = datetime.datetime.now()
print("Ended process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
