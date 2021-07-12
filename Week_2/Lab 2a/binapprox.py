#Lab 2a Task4:  Calculation of median using binapprox algorithm

import math
import numpy as np

# Write your median_bins and median_approx functions here.
def median_bins(values , B):
  
  mean=np.mean(values)
 
  stdev=np.std(values)
  
  count=0
  
  minval=mean-stdev
  maxval=mean+stdev
  
  width=2*stdev/B
  
  
  for i in values:
    if (i < minval):
      count+=1


  lst_bin=[]
  
  for i in range(B):
    lst_bin.append(0)
  
  for i in values:
    if(minval<=i and i<maxval):
      lst_bin[int((i-minval)//width)]+=1
  
  return(mean, stdev, count, np.array(lst_bin))

def median_approx(values,B):
  
  mean , stdev, count, lst_bin=median_bins(values,B)
  
  minval=mean-stdev
  width=2*stdev/B
  
  i_req=B-1
  
  for i in range(B):
    count+=lst_bin[i]
    if(count>=(len(values)+1)/2):
      i_req=i
      break
  
  median=minval + width*(i_req+0.5)
  
  return median
  
# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
  
  print(median_bins([0,1],5))
  print(median_approx([0,1],5))

