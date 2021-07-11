import numpy as np
import time
from astropy.io import fits
# Write your function median_FITS here:
def median_fits(lst):
  
  start=time.perf_counter()
  data=[]

  for i in lst:
    hdulist = fits.open(i)
    data.append(hdulist[0].data)
  
  data=np.array(data)
  
  m=np.median(data , axis=0)
  
  seconds=time.perf_counter()-start
  
  size = data.nbytes/1024
  
  return (m, seconds, size)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])