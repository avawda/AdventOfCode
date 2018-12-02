import os

# Setup path and read file in
path = "C:/Users/vawdaa\OneDrive - Standard Bank/Python/AdventCode/"
print(os.listdir(path))
file = open(path + "Day1_Input.txt","r")
data = file.readlines()

# Process the data
output = 0
for num in data:
    output = output+int(num) 

print(output)
