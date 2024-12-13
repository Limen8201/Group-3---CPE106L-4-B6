#Statisticians would like to have a set of functions to compute the median
#and mode of a list of numbers. The median is the number that would
#appear at the midpoint of a list if it were sorted. The mode is the number
#that appears most frequently in the list. Define these functions in a module
#named stats.py. Also include a function named mean, which computes the
#average of a set of numbers. Each function expects a list of numbers as an
#argument and returns a single number.

import numpy
from scipy import stats

def Mean_fucntion(lst):
    print("Mean:",numpy.mean(lst))
    
def Median_fucntion(lst):
    print("Median:",numpy.median(lst))
    
def Mode_fucntion(lst):
    print(stats.mode(lst))
    
    
listSize = input("Enter size of list: ")
print("list of numbers: ")
listNum = []
i = 0
while i < int(listSize):
    number =int(input())
    listNum.append(number)
    i=i+1

Mean_fucntion(listNum)
Median_fucntion(listNum)
Mode_fucntion(listNum)
