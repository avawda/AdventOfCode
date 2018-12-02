import os

# Setup path and read file in
path = "C:/Users/vawdaa\OneDrive - Standard Bank/Python/AdventCode/"
file = open(path + "Day1_Input.txt","r")

# Process the data
output = 0
counter = 0
duplicateFound = False
results = ["0"]
# Loop until we find the duplicate frequency
while not duplicateFound:
    counter += 1
    if counter%10==0:
        print("File Read Counter = "+str(counter))
    data = file.readlines()
    for num in data:
        output = output+int(num)
        if output in results:
            print("DANGER : DUPLICATE REQUENCY = "+str(output))
            print("ITERATIONS REQUIRED = "+str(counter))
            duplicateFound = True
            break
        else:     
            results.append(output)
    file.seek(0)
    if counter == 200:
        print("Forced exit after 100 tries")
        break 

#print(output)
#print(results)