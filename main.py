from vq import *

if __name__ == '__main__':
    pic_folder = "../Graz02TranValidationTest/Train/bike/"
    K = 25
    my_code_book = code_book(pic_folder, K)

    test_pic = "../Graz02TranValidationTest/Test/bike/bike_166.bmp"
    hist = quatization(test_pic, my_code_book)
    print hist
