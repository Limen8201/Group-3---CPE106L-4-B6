import numpy as np
from scipy import stats
def mean_func(num):
  print('Mean: ',np.mean(num))

def med_func(num):
  print('Meadian: ',np.median(num))

def mode_func(num):
  print(stats.mode(num))

lst = [1,2,3,4,5,6,7,8,9,10]

mean_func(lst)
med_func(lst)
mode_func(lst)
