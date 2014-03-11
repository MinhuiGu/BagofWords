import cv2
import os
import numpy as np
from scipy import cluster
import scipy

def dist(u,v):
    return scipy.spatial.distance.euclidean(u, v)

def hard_quatization(path,book):

    img = cv2.imread(path,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kp, des = cv2.SIFT().detectAndCompute(gray,None)
    adict = {}
    shortest = []
    for i in range(0,len(book)):
        adict[i] = 0
        
    for p in des:
        mini = 0
        for i in range(0,len(book)):
            t = dist(book[i],p)
            if mini == 0 or t < mini:
                mini = t
                shortest = i
        adict[shortest] += 1
    return adict 
                
def codeword( db_path,K, save = True):
    des_pool = np.zeros((0,128))
    kp = []
    for each_img in os.listdir(db_path):
        path = db_path + each_img
        img = cv2.imread(path,cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        kp, des = cv2.SIFT().detectAndCompute(gray,None)
        des_pool = np.concatenate((des_pool,des))
          
    nd,p = cluster.vq.kmeans2(des_pool, K)
    if save:
        np.savetxt('word.txt', nd)
        
    return nd


if __name__ == '__main__':
    train_path = "./Graz02TranValidationTest/Train/bike/"
    K = 10
    codebook = codeword(train_path,K)
    #print codebook
    
    test_path = "./Graz02TranValidationTest/Test/bike/bike_166.bmp"
    hist = hard_quatization(test_path,codebook)
    print hist
