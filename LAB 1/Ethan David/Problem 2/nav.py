
def navigate_file():
    try:
        lines = open(input("Enter the filename (include .txt): "), 'r').readlines()
        while True:
            line_num = int(input(f"Enter a line number (1-{len(lines)}, or 0 to quit): "))
            if line_num == 0: break
            if 1 <= line_num <= len(lines): print(lines[line_num - 1].strip())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    navigate_file()
