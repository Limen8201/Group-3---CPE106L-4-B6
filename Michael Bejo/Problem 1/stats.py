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




