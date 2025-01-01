import os

def mode(fileName):
    try:
        # get the size of file
        file_size = os.path.getsize(fileName)
    
        # if file size is 0, it is empty
        if file_size == 0:
            print("Mode: 0")
        else:
            f = open(fileName, 'r')
            # Input the text, convert its to words to uppercase, and
            # add the words to a list
            words = []
            for line in f:
                wordsInLine = line.split()
                for word in wordsInLine:
                    words.append(word.upper())
                
            # Obtain the set of unique words and their
            # frequencies, saving these associations in
            # a dictionary
            theDictionary = {}
            for word in words:
                number = theDictionary.get(word, None)
                if number == None:
                    # word entered for the first time
                    theDictionary[word] = 1
                else:
                    # word already seen, increment its number
                    theDictionary[word] = number + 1
                
            # Find the mode by obtaining the maximum value
            # in the dictionary and determining its key
            theMaximum = max(theDictionary.values())
            for key in theDictionary:
                if theDictionary[key] == theMaximum:
                    print("The mode is", key)
                    break
                
    except FileNotFoundError as e:
        print("File NOT found")

def median(fileName):
    try:
        # get the size of file
        file_size = os.path.getsize(fileName)
    
        # if file size is 0, it is empty
        if file_size == 0:
            print("Median: 0")
        else:
            f = open(fileName, 'r')
            
            # Input the text, convert it to numbers, and
            # add the numbers to a list
            numbers = []
            for line in f:
                words = line.split()
                for word in words:
                    numbers.append(float(word))
                
            # Sort the list and print the number at its midpoint
            numbers.sort()
            midpoint = len(numbers) // 2
            print("The median is", end=" ")
            if len(numbers) % 2 == 1:
                print(numbers[midpoint])
            else:
                print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
    
    except FileNotFoundError as e:
        print("File NOT found")
    
     
def mean(fileName):
    try:
        # get the size of file
        file_size = os.path.getsize(fileName)
    
        # if file size is 0, it is empty
        if file_size == 0:
            print("Median: 0")
        else:
            f = open(fileName, 'r')
            
            # Input the text, convert it to numbers, and
            # add the numbers to a list
            numbers = []
            for line in f:
                words = line.split()
                for word in words:
                    numbers.append(float(word))
                
            # Initialize variables
            total = 0
            count = 0
                
            #Finding the total and count of list
            for val in numbers:
                total += val
                count += 1
            
            # Calculate the mean
            mean = total / count
                    
            # Output the mean value
            print("Mean: ", mean)
                
    except FileNotFoundError as e:
        print("File NOT found")
        
        
def main():
    fileName = input("Enter the file name: ")
    mode(fileName)
    median(fileName)
    mean(fileName)

main()
