from PIL import Image
from numpy import *

def pca(X):
  """  Principal Component Analysis
    input: X, matrix with training data stored as flattened arrays in rows
    return: projection matrix (with important dimensions first), variance
    and mean."""

  # get dimensions
  num_data,dim = X.shape

  # center data
  mean_X = X.mean(axis=0)
  X = X - mean_X
  X = X.T

  print(shape(X))

  # PCA - compact trick used
  M = dot(X, X.T)  # covariance matrix
  print(M)
  print(shape(M))
  e, EV = linalg.eigh(M)  # eigenvalues and eigenvectors
  idx = e.argsort()[::-1]
  S = e[idx]
  V = EV[:, idx]
  # return the projection matrix, the variance and the mean
  return V,S,mean_X