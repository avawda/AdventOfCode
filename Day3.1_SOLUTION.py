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
from collections import defaultdict
import re

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
m = defaultdict(list)
overlaps = {}
for (claim_number, start_x, start_y, width, height) in claims:
  overlaps[claim_number] = set()
  for i in range(start_x, start_x + width):
    for j in range(start_y, start_y + height):
      if m[(i,j)]:
        for number in m[(i, j)]:
          overlaps[number].add(claim_number)
          overlaps[claim_number].add(number)
      m[(i,j)].append(claim_number)

answer = len([k for k in m if len(m[k]) > 1])
# print("b", [k for k in overlaps if len(overlaps[k]) == 0][0])
# Custom Problem code ends here

print()
end = datetime.datetime.now()
print("Ended process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
