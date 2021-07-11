from astropy.io import fits 
import numpy as np

# Write your mean_fits function here:
def mean_fits(lst_iname):
 
  data=[]
  for iname in lst_iname:
    hdulist=fits.open(iname)
    data.append(hdulist[0].data)
    
  for i in range(1,len(lst_iname)):
    data[0]=np.add(data[0],data[i])
  
  data[0]=np.round(np.divide(data[0],len(lst_iname)),decimals=20)
  
  return data[0]

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()