#Lab 2b Task1: Heavenly Angles

import numpy as np
# Write your angular_dist function here.
def angular_dist(ra1, dec1, ra2, dec2):
  lst= [ra1,dec1,ra2,dec2]
  ra1,dec1,ra2,dec2=np.radians(lst)
  
  a=np.sin(np.abs((dec1-dec2)/2))**2
  
  b=np.cos(dec1)*np.cos(dec2)*(np.sin((ra1-ra2)/2)**2)
  
  return(np.degrees(2*np.arcsin(np.sqrt(a+b))))
  



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))

