from vq import *

if __name__ == '__main__':
    train_path = "./Graz02TranValidationTest/Test/test/"
    K = 10
    my_code_book = code_book(train_path, K)
    #printmy_code_book
    test_path = "./Graz02TranValidationTest/Test/test/bike_166.bmp"
    hist = hard_quatization(test_path, my_code_book)
    print hist
