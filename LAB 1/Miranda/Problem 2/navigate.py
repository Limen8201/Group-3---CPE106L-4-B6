def navigate_file():
    filename = input("Enter the filename (name.txt): ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        while True:
            print(f"File '{filename}' has {len(lines)} lines.")
            line_number = int(input("Enter a line number (0 to quit): "))
            if line_number == 0:
                print("Exiting the program.")
                break
            if 1 <= line_number <= len(lines):
                print(lines[line_number - 1].strip())
            else:
                print("Invalid line number. Please try again.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

navigate_file()
