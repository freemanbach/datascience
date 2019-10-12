# Author  : freeman
# Date    : 2019.10.12
# Version : 0.0.1
# Desc    :
#
###################################################################

import time
import random
import sys
import math


def getRandSamp(f):
    tmp, data = [], []
    with open(f, 'r') as dset:
        for i in dset:
            tmp.append(i)
    
    # random Sampling
    data = random.sample(tmp, 100)
    return data
    #print data
    #print len(data)
    
def splitTheStuff(d):
    
    return 0

def main():
    
    if len(sys.argv) <= 1:
        print "not enough parameters, need a datasource file as parameter." # machine.data
        sys.exit()
    else:
        a = getRandSamp(sys.argv[1])
        b = splitTheStuff(a)
        
    
    
if __name__ == "__main__":
    main()