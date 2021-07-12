#lab 5a Task3: Simple Queries in python 1/3


import numpy as np
# Write your query function here
def query(fname):
  data=np.loadtxt(fname, delimiter=",", usecols=[0,2])
  
  records=[]
  for i in data:
    if ( i[1]>=1):
      records.append(i)
  
  return(np.array(records))



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print(result)