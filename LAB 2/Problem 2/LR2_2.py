import linecache 

fileName = input("Insert a filename: ")
file = open(fileName, "r")

i=0
for x in file:
    print(i+1,")", x, end="")
    i=i+1

print("")
lineNum = i
print(fileName, "has", i, "line")
while lineNum != 0:
    lineNum = int(input("Please choose a line to print (Type 0 to stop): "))
    print(linecache.getline(fileName, lineNum))
    if lineNum == 0:
        exit()
  
