import math
import os
from PIL import Image
import numpy as np
import scipy.misc as smp
train_imgs = np.loadtxt("Output.txt")


def add_vectors(ar1, ar2):
    for i in range(len(ar1)):
        ar2[i] = ar1[i] + ar2[i]
    return ar2


def build_medians():
    sum_vector = [0] * 784
    i = 1
    k = 0
    median_vectors = dict()
    while i < len(train_imgs):
        if train_imgs[i][0] == train_imgs[i - 1][0]:
            sum_vector = add_vectors(sum_vector, train_imgs[i][1:])
            k += 1
        else:
            med_vector = []
            for j in sum_vector:
                med_vector.append(j / k)
            median_vectors[train_imgs[i - 1][0]] = med_vector
            sum_vector = [0] * 784
            k = 0
        i += 1
    return median_vectors


def count_middle_color(numpy_array):
    num_black = 0
    num_white = 0
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] == 0:
                num_black += 1
            else:
                num_white += 1
    if num_black and num_white:
        return float(num_black) / (num_white + num_black)
    else:
        return 0


def binarize_array(numpy_array, threshold=0.2):
    """Binarize a numpy array."""
    vector = []
    for i in range(0, len(numpy_array), 10):
        for j in range(0, len(numpy_array[0]), 10):
            coef = count_middle_color(numpy_array[i:i + 9, j:j + 9])
            if coef > threshold:
                vector.append(1)
            else:
                vector.append(0)
    return vector


def calculate_distance(v1, v2):
    dist = 0
    for i in range(len(v1)):
        dist += abs(v1[i] * v1[i] - v2[i] * v2[i])
    return math.sqrt(dist)


def min_key(dictionary):
    minimum = 789
    minimum_key = 0
    for i in dictionary:
        if dictionary[i] < minimum:
            minimum_key = i
            minimum = dictionary[i]
    return minimum_key, minimum


def test_image(numpy_array, median_vectors):
    d_dict = dict()
    for i in median_vectors:
        distance = calculate_distance(median_vectors[i], numpy_array)
        d_dict[i] = distance
    print(d_dict)
    return min_key(d_dict)


def none_zero_min(array):
    minimum = 1
    for i in array:
        if minimum > i > 0:
            minimum = i
    return minimum


def sharping_image(med_vectors):
    final_vectors = dict()
    for vector in med_vectors:
        edited_vector = []
        for j in med_vectors[vector]:
            if j > max(med_vectors[vector])*0.85:
                edited_vector.append(1)
            else:
                edited_vector.append(0)
        final_vectors[vector] = edited_vector
    return final_vectors


med = sharping_image(build_medians())
path = 'Letters'
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

