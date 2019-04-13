# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:27:13 2018

@author: Yigao
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.hierarchy import ward, dendrogram
import os
#import numpy as np
#import pandas as pd

## load all texts from "Novels_Corpus" subdirectory
directory = "Novels_Corpus"
filenames = []
names = []
for filename in os.listdir(directory):
    filenames.append(directory + "/" + filename)
    names.append(filename[:-4])
vectorizer = CountVectorizer(input = "filename")
dtm = vectorizer.fit_transform(filenames)
vocab = vectorizer.get_feature_names()
dtm = dtm.toarray()

## Distance metrics
dist = euclidean_distances(dtm)
cosdist = 1 - cosine_similarity(dtm)

## 2D Visualization
mds = MDS(n_components = 2, dissimilarity = "precomputed", random_state = 5193)
pos = mds.fit_transform(cosdist)
xs, ys = pos[:,0], pos[:,1]
for x, y, name in zip(xs, ys, names):
    plt.scatter(x, y)
    plt.text(x, y, name)
plt.title("Document Distances 2D Cartesian")
plt.show()

## 3D Visualization
mds = MDS(n_components = 3, dissimilarity = "precomputed", random_state = 5193)
pos = mds.fit_transform(cosdist)
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(pos[:,0], pos[:,1], pos[:,2])
for x, y, z, s in zip(pos[:,0], pos[:,1], pos[:,2], names):
    ax.text(x, y, z, s)
plt.title("Document Distances 3D Cartesian")
plt.show()

## Hierarchical Clustering Visualization
linkage_matrix = ward(cosdist)
dendrogram(linkage_matrix, orientation = "right", labels = names)
plt.tight_layout()
plt.title("Document Distances Hierarchical Clustering")
plt.show()