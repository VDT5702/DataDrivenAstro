#lab 5a Task5: Simple queries in python 3/3


import numpy as np
# Write your query function here
def query(fname1,fname2):
  data1=np.loadtxt(fname1, delimiter=",", usecols=[0,2])
  data2=np.loadtxt(fname2, delimiter=",", usecols=[0,5])
  
  records=[]
  for i in data1:
    for j in data2:
      if ( i[0]==j[0]):
        if (i[1]>=1):
          records.append([j[1]/i[1]])
  
  a=np.array(records)
  b=np.argsort(a[:,0])
  return(a[b])




# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
  print(result)