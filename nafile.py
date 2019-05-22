from PIL import Image
import PIL
import numpy as np
import os
import math
import pandas as pd
from pcaf1 import pca
import deepdish as dd
import pickle

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
    # print(d_dict)
    return min_key(d_dict)

def letter():
    mean_l = np.load('mean.npy')

    V = np.load('Vectors.npy')
    V=V[:,:1000]

    path = 'test'
    test_list = ['test/image.png']
    # for r, d, f in os.walk(path):
    #     for file in f:
    #         test_list.append(os.path.join(r, file))

    d = dd.io.load('Values.h5')

    for i in test_list:
        im = Image.open(i)
        im.load()
        image_data = np.asarray(im)
        print(image_data)
        image_data_bw = image_data.max(axis=2)
        non_empty_columns = np.where(image_data_bw.max(axis=0) > 0)[0]
        non_empty_rows = np.where(image_data_bw.max(axis=1) > 0)[0]
        cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

        image_data_new = image_data[cropBox[0]:cropBox[1] + 1, cropBox[2]:cropBox[3] + 1, :]

        im = Image.fromarray(image_data_new)
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])  # 3 is the alpha channel
        image = background.convert('L')  # convert image to monochrome
        image.save('lul.png')
        image = image.resize((80, 110), PIL.Image.ANTIALIAS)
        image.save('lol.png')
        image = np.array(image)
        image[image <= 20] = 0
        image[image >= 20] = 1
        image = image.flatten()-mean_l
        image1 = np.dot(V.T, image)


        letter, dist = test_image(image1, d)
        print(i)
        print(letter)
        print(dist)
        return(letter.split('\\')[1])