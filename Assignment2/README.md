# Individual Project Assignment 2: Eigenfaces and Facial Recognition

Data Reduction Techniques - Using PCA, EigenFaces, and Python3

## Goal

Write a Python3 program `eigenfaces.py` to read in all faces (as vectors), create a matrix which is comprised of all face vectors, perform PCA to generate an eigenface matrix in a reduced dimension (the reduction per Turk and Pentland), and use the eigenface matrix to match both faces in the dataset and test faces not in the dataset.

## Instructions

1) Read all the image-type data into Python3.

2) Convert each face in the dataset (.pgm) into a vector of values.

3) Take all faces in the dataset, convert each to a vector and place all vectors into one matrix.

4) Find the mean of all the columns and subtract that mean from all the columns to form a normalized face matrix.
- Create an image `meanface.jpg` of the mean face. 

5) Perform the appropriate Turk and Pentland method for PCA to determine the eigenvectors and eigenvalues of the covariance matrix.

6) Order the eigenvalues. Choose the top 30 eigenvalues.

7) Select the top k eigenvectors.

8) Per the methods of Turk and Pentland, project the 30 eigenvectors back into the original space.
 - Create a file with the top 5 eigenvalues and top 5 eigenvectors. Project eigenvectors back into the normal space. These are called the EIGENFACES.
 - Next, create code that converts all 30 eigenfaces into images. Eigenfaces also look kind of like faces, but just creepy and non-specific. Create images of the top 5 eigenfaces and SAVE THESE TOP 5 to FILES as well `eigenface_?.jpg`.

9) Create a matrix of the projected 30 eigenvectors. These 30 eigenvectors are called EIGENFACES and the matrix is the eigenface_matrix. 

## Tests

Test 1: Choose any image from the dataset of faces. Make a copy of it and save it as TEST_Image.pgm. Then, read it into code, vectorize it, normalize it (subtract the mean), and project it to eigenface reduced space using the eigenfaces matrix. Then, compare it to all faces in the database by reading in each face, doing the same steps, and taking the euclidean distance between each database face and the testface. Program should match it with the image in the database for which the euclidean distance is smallest.

Test 2: Pull an image out of the database of faces. Call it TEST_Image_2.pgm. BUT REMOVE IT from the database. The idea here is to see if program can find a face CLOSE TO the test face removed from the dataset.
