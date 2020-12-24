import sys

from chapter8 import *
from chapter9 import *

if __name__ == '__main__':
    if len(sys.argv) > 2:
        globals()[sys.argv[1]](sys.argv[2])
    else:
        globals()[sys.argv[1]]()
