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

def import_super():
  
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  
  tup_super=[]
  
  for i in range(len(cat)):
    tup_super.append((i+1,cat[i][0],cat[i][1]))  
    
  return (tup_super)
    
  


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)