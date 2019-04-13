# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:43:21 2018

@author: Yigao
"""

import numpy as np
from PIL import Image
import os
from scipy.spatial.distance import euclidean
import math
import matplotlib.pyplot as plt

## read face images to facematrix
directory = "FACESdata"
a = True
for dirname in os.listdir(directory):
    for filename in os.listdir(directory + "/" + dirname):
        fullpath = directory + "/" + dirname + "/" + filename
        img = Image.open(fullpath).convert("L")
        imagearray = np.array(img)
        flat = imagearray.ravel()
        facevector = np.matrix(flat)
        while a is True:
            facematrix = np.empty(facevector.shape, dtype = "uint8")
            a = False
        facematrix = np.r_[facematrix, facevector]
facematrix = np.delete(facematrix, (0), axis = 0)
facematrix_t = np.transpose(facematrix)
original_shape = imagearray.shape

## calculate mean face
facemean = facematrix_t.mean(axis = 1)
facemean_array = np.asarray(facemean.reshape(original_shape))
#facemean_img = Image.fromarray(facemean_array, "L")
#facemean_img.save("meanface.jpg")
print("This is the mean face.")
facemean_img = plt.figure()
plt.imshow(facemean_array, cmap = plt.get_cmap("gray"))
plt.axis("off")
plt.show()
facemean_img.savefig("meanface.jpg")


## normalize face matrix, calculate eigenvalues and eigenvectors
Norm_Face_Matrix = facematrix_t - facemean
print("Normalized face matrix is")
print(Norm_Face_Matrix)
print("The shape is")
print(Norm_Face_Matrix.shape)
Norm_Face_Matrix_t = np.transpose(Norm_Face_Matrix)
CovMatrix = np.matmul(Norm_Face_Matrix_t, Norm_Face_Matrix)
evals, evects = np.linalg.eig(CovMatrix)
evals_sort = np.sort(evals)

## ask user to input top number of eigenvectors in eigenface matrix
#k = 5
k = eval(input("Enter the number of eigenvectors: "))
eigenface_matrix = np.empty(facemean.shape)
for i in range(1,k+1):
    eindex, = np.where(evals == evals_sort[-i])
    evect_reduce_t = np.transpose(evects[eindex[0]])
    evect = np.matmul(facematrix_t, evect_reduce_t)
    evect_array = np.asarray(evect.reshape(original_shape))
    #evect_img = Image.fromarray(evect_array, "L")
    #evect_img.save("eigenface_" + str(i) + ".jpg")
    print("Eigenface " + str(i) + " is")
    evect_img = plt.figure()
    plt.imshow(evect_array, cmap = plt.get_cmap("gray"))
    plt.axis("off")
    plt.show()
    evect_img.savefig("eigenface_" + str(i) + ".jpg")
    eigenface_matrix = np.c_[eigenface_matrix, evect]
eigenface_matrix = np.delete(eigenface_matrix, (0), axis = 1)
print("Eigenface matrix is")
print(eigenface_matrix)
print("The shape is")
print(eigenface_matrix.shape)

## Test 1
## read test image
test_img = Image.open("TEST_Image.pgm")
test_array = np.array(test_img)
test_flat = test_array.ravel()
test_vector = np.matrix(test_flat)
Norm_test = np.transpose(test_vector) - facemean
test_proj = np.matmul(np.transpose(eigenface_matrix), Norm_test)

## compare every image in dataset to test image
b = math.inf
for dirname in os.listdir(directory):
    for filename in os.listdir(directory + "/" + dirname):
        fullpath = directory + "/" + dirname + "/" + filename
        img = Image.open(fullpath).convert("L")
        imagearray = np.array(img)
        flat = imagearray.ravel()
        facevector = np.matrix(flat)
        Norm_facevector = np.transpose(facevector) - facemean
        face_proj = np.matmul(np.transpose(eigenface_matrix), Norm_facevector)
        eucl_dist = euclidean(test_proj, face_proj)
        if eucl_dist < b:
            b = eucl_dist
            savepath = fullpath
match_img = Image.open(savepath).convert("L")
match_img.show()
match_img.save("TEST_Image.jpg")

## Test 2
## basically same thing with test 1 but this time we don't consider the original image in the dataset
c = math.inf
for dirname in os.listdir(directory):
    for filename in os.listdir(directory + "/" + dirname):
        fullpath = directory + "/" + dirname + "/" + filename
        if fullpath == "FACESdata/s14/2.pgm": # because this is our test image
            continue
        img = Image.open(fullpath).convert("L")
        imagearray = np.array(img)
        flat = imagearray.ravel()
        facevector = np.matrix(flat)
        Norm_facevector = np.transpose(facevector) - facemean
        face_proj = np.matmul(np.transpose(eigenface_matrix), Norm_facevector)
        eucl_dist = euclidean(test_proj, face_proj)
        if eucl_dist < c:
            c = eucl_dist
            savepath = fullpath
close_img = Image.open(savepath).convert("L")
close_img.show()
close_img.save("PREDICTED_Image.jpg")