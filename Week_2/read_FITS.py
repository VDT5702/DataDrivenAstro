# Write your load_fits function here.
def load_fits(iname):
  from astropy.io import fits
  import numpy as np
  
  hdulist = fits.open(iname)
  data = hdulist[0].data
  n=data.shape[0]
  return (np.argmax(data)//n, np.argmax(data)%n)



if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image3.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image3.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 

