import numpy
from scipy import stats
def median_function(lst):
    print("Median: ", numpy.median(lst))
def mode_function(lst):
    print("Mode: ", stats.mode(lst))
def mean_function(lst):
    print("Mean: ", numpy.mean(lst))
  
a = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
    
print("List: ", a)

a.sort()

print("Sorted List: ", a)

median_function(a)
mode_function(a)
mean_function(a)




