#Write a program that allows the user to navigate through the lines of text in
#a file. The program prompts the user for a filename and inputs the lines of
#text into a list. The program then enters a loop in which it prints the number
#of lines in the file and prompts the user for a line number. Actual line
#numbers range from 1 to the number of lines in the file. If the input is 0, the
#program quits. Otherwise, the program prints the line associated with that
#number.9

import linecache 

fileName = input("Insert a filename (name.txt): ")
file = open(fileName, "r")

i=0
for x in file:
    i=i+1

print(fileName, "has", i, "line")

lineNum = 0
while lineNum != -1:
    lineNum = int(input("Please choose a line to print: "))
    if lineNum == 0:
        exit()
    print(linecache.getline(fileName, lineNum))
