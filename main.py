from vq import *
from optparse import OptionParser
import os

class OptException(Exception):
    pass

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="folder_path",\
                      help="the path of folder that contains images file.")
    parser.add_option("-f", "--file", type="string", dest="filename", \
                      help="the target image file.")

    (options, args) = parser.parse_args()

    if not options.folder_path:
        raise OptException("Please input folder's path.")
    else:
        if not os.path.isdir(options.folder_path):
            raise OptException('Invalid path.')

    if not options.filename:
        raise OptException("Please input test file's path.")
    else:
        if not os.path.exists(options.filename):
            raise OptException('Invalid file.')

    read = 0
    while read != 1 and read != 2:
    	read = input("Read from word.txt? 1-->yes, 2-->no:  ")
    read = True if read == 1 else False

    soft = 0
    while soft != 1 and soft != 2:
    	soft = input("Do soft quantization? 1-->soft, 2-->hard:  ")
    soft = True if soft == 1 else False

    K = 0
    while K == 0 :
        K = input("codebook size? K =  ")
        K = int(K)

    my_code_book = code_book(options.folder_path, K, read_from_txt=read)
    hist = quatization(options.filename, my_code_book, soft=soft)
    print hist
