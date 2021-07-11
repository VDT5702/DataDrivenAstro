import numpy as np
import time

def angular_dist(ra1, dec1, ra2, dec2):  
  lst=[ra1,dec1,ra2,dec2]
  
  ra1,dec1,ra2,dec2=np.radians(lst)
  a=np.sin(np.abs((dec1-dec2)/2))**2
  
  b=np.cos(dec1)*np.cos(dec2)*(np.sin((ra1-ra2)/2)**2)
  
  return(np.degrees(2*np.arcsin(np.sqrt(a+b))))
  

# Write your find_closest function here
def find_closest(cat, asc, dec):
 
  d_min = angular_dist(cat[0][0],cat[0][1],asc,dec)
  id_min=0
  
  for i in range(len(cat)):
    
    dist = angular_dist(cat[i][0],cat[i][1],asc,dec)
    
    if (dist < d_min ):
      id_min=i
      d_min=dist
    
  return(id_min,d_min)


# Write your crossmatch function here.
def  crossmatch(bss_cat, super_cat, max_dist):
  
  start=time.time()
  
  lst_matches=[]
  lst_no_matches=[]
  
  for i in range(len(bss_cat)):
    
    id_min,d_min=find_closest(super_cat,bss_cat[i][0],bss_cat[i][1])
    
    if d_min < max_dist:
      lst_matches.append((i,id_min,d_min))
    
    else:
      lst_no_matches.append(i)  
  
  return (lst_matches,lst_no_matches,time.time()-start)





# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

