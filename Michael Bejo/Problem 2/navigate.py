import linecache 

fileName = input("Insert a filename (name.txt): ")
file = open(fileName, "r")

i=0
for x in file:
    i=i+1

print(fileName, "has", i, "line")

lineNum = 0
lineNum = int(input("Please choose a line to print: "))
if lineNum == 0:
    exit()
  
print(linecache.getline(fileName, lineNum) )
