#Lab 5b Task 3: Calculating the Mean difference

import numpy as np

# write a function that calculates the median of the differences
# between our predicted and actual values
def median_diff(predicted, actual):
  
  med_diff=np.median(np.abs(predicted-actual))
  
  return(med_diff)

if __name__ == "__main__":
  # load testing data
  targets = np.load('targets.npy')
  predictions = np.load('predictions.npy')

  # call your function to measure the accuracy of the predictions
  diff = median_diff(predictions, targets)

  # print the median difference
  print("Median difference: {:0.3f}".format(diff))

