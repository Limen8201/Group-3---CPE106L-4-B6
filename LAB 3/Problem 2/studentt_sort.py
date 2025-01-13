import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Compares two Student objects for equality based on name."""
        if isinstance(other, Student):
            return self.name if self.name == other.name else other.name
        return self.name  # If not comparable, return the current student's name

    def __lt__(self, other):
        """Compares if the name of the first Student is lexicographically less than the second."""
        if isinstance(other, Student):
            return self.name if self.name < other.name else other.name
        return self.name  # If not comparable, return the current student's name

    def __ge__(self, other):
        """Compares if the name of the first Student is lexicographically greater than or equal to the second."""
        if isinstance(other, Student):
            return self.name if self.name >= other.name else other.name
        return self.name  # If not comparable, return the current student's name

def main():
    """A simple test."""
    # Create a list of students
    student1 = Student("Ken", 5)
    student2 = Student("Alice", 5)
    student3 = Student("Bob", 3)
    student4 = Student("David", 4)
    student5 = Student("Eve", 5)

    students = [student1, student2, student3, student4, student5]
    
    # Shuffle the list
    random.shuffle(students)
    
    # Display shuffled students' information
    print("Shuffled list of students:")
    for student in students:
        print(student)
        print()
    
    # Sort the list of students
    students.sort()
    
    # Display sorted students' information
    print("Sorted list of students:")
    for student in students:
        print(student)
        print()

if __name__ == "__main__":
    main()
