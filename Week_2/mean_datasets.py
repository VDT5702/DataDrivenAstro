import numpy as np
# Write your mean_datasets function here

def mean_datasets(lst):
  n=len(lst) #just keepng the count of number of files
  a=[]
  for i in lst:
    a.append(np.loadtxt(i,delimiter=","))
  
  for i in range(1,n):
    a[0]=np.add(a[0],a[i])
  
  a[0]=np.round(np.divide(a[0],n),decimals=1)
  return a[0]
    

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))

