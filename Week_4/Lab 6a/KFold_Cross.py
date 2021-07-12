#Lab 6a Task 2: K-FOld Cross Variation

import numpy as np
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeRegressor

import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# paste your get_features_targets function here
def get_features_targets(data):
  # complete this function
  features=np.zeros((data.shape[0],4))
  features[:,0]=data['u']-data['g']
  features[:,1]=data['g']-data['r']
  features[:,2]=data['r']-data['i']
  features[:,3]=data['i']-data['z']

  targets=np.zeros((data.shape[0],1))
  targets=data['redshift']
  
  return (features, targets)


# paste your median_diff function here
def median_diff(predicted, actual):
  
  med_diff=np.median(np.abs(predicted-actual))
  
  return(med_diff)


# complete this function
def cross_validate_model(model, features, targets, k):
  kf = KFold(n_splits=k, shuffle=True)

  # initialise a list to collect median_diffs for each iteration of the loop below
  median_diffs_iter=[]
  
  for train_indices, test_indices in kf.split(features):
    train_features, test_features = features[train_indices], features[test_indices]
    train_targets, test_targets = targets[train_indices], targets[test_indices]
    
    # fit the model for the current set
    model.fit(train_features,train_targets)
    
    # predict using the model
    prediction_test=model.predict(test_features)
    
    # calculate the median_diff from predicted values and append to results array
    median_diffs_iter.append(median_diff(prediction_test, test_targets))
 
  # return the list with your median difference values
  return(median_diffs_iter)

if __name__ == "__main__":
  data = np.load('./sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model with a maximum depth of 19
  dtr = DecisionTreeRegressor(max_depth=19)

  # call your cross validation function
  diffs = cross_validate_model(dtr, features, targets, 10)

  # Print the values
  print('Differences: {}'.format(', '.join(['{:.3f}'.format(val) for val in diffs])))
  print('Mean difference: {:.3f}'.format(np.mean(diffs)))

