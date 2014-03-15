import cv2
import os
import numpy as np
from scipy import cluster
import scipy


def __dist(u, v):
    """
    Get euclidean distance of two ndarray.

    Parameters
    ----------
    u, v : numpy ndarray

    Returns
    -------
    The distance calculated by scipy.
    """
    return scipy.spatial.distance.euclidean(u, v)

def __sift_dect_and_compute(image):
    """
    Extract features and computes their descriptors using SIFT algorithm.

    Parameters
    ----------
    image: the absolute path of image file

    Returns
    -------
    kp: Keypoints detected by SIFT.
    des: descriptors computed by SIFT.
    """
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = cv2.SIFT().detectAndCompute(gray, None)
    return kp, des

def hard_quatization(image, code_book):
    """
    Do hard quatization by assign codes from a code book to target image
    that computes the euclidian distance between image and every frame
    in the code_book.

    Parameters
    ----------
    image: the absolute path of image file
    code_book: numpy ndarray

    Returns
    -------
    adict:
    """
    kp, des = __sift_dect_and_compute(image)
    adict = {}
    shortest = []
    for i in range(0, len(code_book)):
        adict[i] = 0

    for p in des:
        mini = 0
        for i in range(0, len(code_book)):
            t = __dist(code_book[i], p)
            if mini == 0 or t < mini:
                mini = t
                shortest = i
        adict[shortest] += 1
    return adict

def code_book(folder_path, K, save=True):
    """
    Generate the bag of words for a folder of pictures.

    Parameters
    ----------
    folder_path: the absolute path of the folder that contains set of
    images

    k: int or ndarray
        The number of clusters to form as well as the number of
        centroids to generate.

    save: The flag for saving the result code book.

    Returns
    -------
    nd: ndarray
        A 'k' by 'N' array of centroids found at the last iteration of
        k-means.
    """
    des_pool = np.zeros((0, 128))
    kp = []
    for each_img in os.listdir(folder_path):
        image_path = folder_path + each_img
        kp, des = __sift_dect_and_compute(image_path)
        des_pool = np.concatenate((des_pool, des))
    nd, p = cluster.vq.kmeans2(des_pool, K)
    if save:
        np.savetxt('word.txt', nd)
    return nd
