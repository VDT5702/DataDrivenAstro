#lab 5a Task4: Simple Queries in python 2/3

import numpy as np
# Write your query function here
def query(fname):
  data=np.loadtxt(fname, delimiter=",", usecols=[0,2])
  
  records=[]
  for i in data:
    if ( i[1]>=1):
      records.append(i)
  
  a=np.array(records)
  b=np.argsort(a[:,1])
  return(a[b])





# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print(result) 