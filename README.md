Bag of words
===================

This repo is the Course Project 2 for CS598 Visual Information Retrieval in Stevens Institute of Technology which implements the basic bag-of-feature representation of an image. We also provide both hard quantization and soft quantization in it. 

##Dependecies:

[OpenCV-Python](http://docs.opencv.org/trunk/doc/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html#py-table-of-content-setup)

[Scipy Library](http://www.scipy.org/scipylib/index.html)

[Numpy] (http://www.numpy.org)

##File Structure:
```
root/
  |-main.py                   (Runnable file for testing our APIs)
  |-vq.py                     (Functions for creating bag of words)
```
## How to run the code:

Install dependecies first. (OpenCV-Python, Scipy, Numpy)

  Usage: main.py [options]
  Options:
    -h, --help            show this help message and exit
    -s FOLDER_PATH, --source=FOLDER_PATH
                          the path of folder that contains images file.
    -f FILENAME, --file=FILENAME
                          the target image file.
