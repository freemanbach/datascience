# Author  : freeman
# Date    : 2019.09.29
# Version : 0.0.1
# Desc    :
#
###################################################################

import time
import random
import sys
import math


def processdata(f):
    data = []
    with open(f, 'r') as dset:
        for i in dset:
            data.append(i)
            
    return data

            
def eliminateIncomp(mylist):
    tmp, data = [], []
    for i in mylist:
        tmp = i.split(',')
        if tmp[11] != '?':
            data.append(i)
            
    return data
    
    
def main():
    
    if len(sys.argv) <= 0:
        sys.exit()
    
    d1 = processdata(sys.argv[1])
    d2 = eliminateIncomp(d1)
    for i in d2:
        print i
        
        
if __name__ == "__main__":
    main()