#Lab 2a Task2: Time taken to calculate median

import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  # the time to generate the random array should not be included
  data = np.random.rand(size)
  
  seconds=0.0
  for i in range(ntrials):
  # modify this function to time func with ntrials times using a new random array each time
    start=time.perf_counter()
    res = func(data)
    seconds+=time.perf_counter()-start
    
    data=np.random.rand(size)
   
    # return the average run time
  avg=seconds/ntrials
  return avg

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))

