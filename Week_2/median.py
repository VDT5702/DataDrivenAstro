# Write your list_stats function here.
def list_stats(lst):
  
  lst.sort()
  mid=len(lst)//2
  
  if (len(lst)==1):
    median=lst[0]
  
  elif(len(lst)%2==0):
    median=(lst[mid-1]+lst[mid])/2
  
  else:
    median=lst[mid]
  
  sumlst=0
  
  for i in lst:
    sumlst+=i
  
  mean=sumlst/len(lst)
  
  return (median,mean)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)