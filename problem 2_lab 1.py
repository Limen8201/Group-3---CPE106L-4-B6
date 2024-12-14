filename = input("Enter the filename: ")

file = open(filename, "r")
lines = file.readlines()
file.close()

print("Number of lines:", len(lines))

while True:
    line_number = int(input("Enter a line number (0 to quit): "))

    if line_number == 0:
        break
    elif 1 <= line_number <= len(lines):
        print(lines[line_number - 1].strip())
    else:
        print("Invalid line number. Please try again.")