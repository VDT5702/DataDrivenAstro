#Lab 2b Task 4: Look around you

import numpy as np

#hms2dec definition
def hms2dec( h, m, s):
  
  return (15*(h + m/60 + s/3600))

#dms2dec() definition
def dms2dec( d, m, s):
  
  if d>0 :
    return (d + m/60 + s/3600)
  
  else:
    return (-1*(-1*d + m/60 + s/3600))


# Write your import_bss function here.
#import_bss definition  
def import_bss():
  
  cat=np.loadtxt('bss.dat',usecols=range(1,7))
  
  tup_bss=[]
  for i in range(len(cat)):
    tup_bss.append((i+1,hms2dec(cat[i][0], cat[i][1], cat[i][2]),dms2dec(cat[i][3],cat[i][4],cat[i][5])))
  
  return(tup_bss)

def angular_dist(ra1, dec1, ra2, dec2):
  lst= [ra1,dec1,ra2,dec2]
  ra1,dec1,ra2,dec2=np.radians(lst)
  
  a=np.sin(np.abs((dec1-dec2)/2))**2
  
  b=np.cos(dec1)*np.cos(dec2)*(np.sin((ra1-ra2)/2)**2)
  
  return(np.degrees(2*np.arcsin(np.sqrt(a+b))))
  

# Write your find_closest function here
def find_closest(cat, asc, dec):
  
  d_min = angular_dist(cat[0][1],cat[0][2],asc,dec)
  id_min=1
  
  for tup in cat:
    
    dist = angular_dist(tup[1],tup[2],asc,dec)
    
    if (dist < d_min ):
      id_min=tup[0]
      d_min=dist
    
  return(id_min,d_min)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))

