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
        raise OptException("Please input file's path.")
    else:
        if not os.path.exists(options.filename):
            raise OptException('Invalid file.')

    K = 10
    my_code_book = code_book(options.folder_path, K)
    hist = hard_quatization(options.filename, my_code_book)
    print hist
