import numpy as np
# Write your calc_stats function here.
def calc_stats(fname):
   data=np.loadtxt(fname, delimiter=",")
   m=np.round(np.mean(data),decimals=1)
   md=np.round(np.median(data),decimals=1)
   return (m,md)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)