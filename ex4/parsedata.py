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


def getRandomSample1(f):
    data, ndata = [], []
    with open(f, 'r') as dset:
        for i in dset:
            data.append(i)
    
    # random Sampling
    ndata = random.sample(data, 500)
    print "Size of this new sample is: " + str(len(ndata))
    
    
def getRandomSample2(f):
    data,size, ndata = [], [], []
    # jiggle the random generator aka increase entropy in the machine
    random.seed(time.time())
    # add data to a list
    with open(f, 'r') as dset:
        for i in dset:
            data.append(i)
    # Thinking of writing my own unique Sampling Algorithm
    
    
def main():
    
    if len(sys.argv) <= 0:
        sys.exit()
    else:
        getRandomSample1(sys.argv[1])
    
    
    
if __name__ == "__main__":
    main()