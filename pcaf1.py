from PIL import Image
from numpy import *

def chunking_dot(big_matrix, small_matrix, chunk_size=100):
    # Make a copy if the array is not already contiguous
    small_matrix = ascontiguousarray(small_matrix)
    print(big_matrix.shape[0])
    print(small_matrix.shape[1])
    R = zeros((big_matrix.shape[0], small_matrix.shape[1]))
    for i in range(0, R.shape[0], chunk_size):
        end = i + chunk_size
        R[i:end] = dot(big_matrix[i:end], small_matrix)
    return R

def pca(X):
  """  Principal Component Analysis
    input: X, matrix with training data stored as flattened arrays in rows
    return: projection matrix (with important dimensions first), variance
    and mean."""

  # get dimensions
  num_data,dim = X.T.shape

  # center data
  mean_X = X.mean(axis=0)
  X = X - mean_X
  X = X.T

  if dim>num_data:
    # PCA - compact trick used
    M = dot(X,X.T) # covariance matrix
    e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
    X = X.T
    tmp = dot(X,EV)
    tmp = tmp.T # this is the compact trick
    V = tmp[::-1] # reverse since last eigenvectors are the ones we want
    S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
    for i in range(V.shape[1]):
      V[:,i] /= S
    V[isnan(V)] = 0
  else:
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    # PCA - SVD used
    U,S,V = linalg.svd(X)
    V = V[:num_data] # only makes sense to return the first num_data

  # return the projection matrix, the variance and the mean
  return V,S,mean_X