# Author  : freeman
# Date    : 2019.10.21
# Version : 0.0.3
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
    

# answer the question 2-doors and low maintenance
def get2dlowmaint(f):
    data, fdset = [], []
    with open(f, 'r') as dset:
        for i in dset:
            tmp = i.split(',')
            if tmp[1] == "low" and tmp[2] == "2": 
                data.append(i)
    
    # print len(data)
    return data
    
    
# answer the question 4-doors and high maintenance
def get4dhighmaint(f):
    data, fdset = [], []
    with open(f, 'r') as dset:
        for i in dset:
            tmp = i.split(',')
            if tmp[1] == "vhigh" and tmp[2] == "4": 
                data.append(i)
    
    # print len(data)
    return data
    
    
def getRandomSample2(f):
    data,size, ndata = [], [], []
    # jiggle the random generator aka increase entropy in the machine
    random.seed(time.time())
    # add data to a list
    with open(f, 'r') as dset:
        for i in dset:
            data.append(i)
    # Thinking of writing my own unique Sampling Algorithm
    return 0
    
    
def main():
    
    if len(sys.argv) <= 1:
        print "not enough parameters"
        sys.exit()
    
    #getRandomSample1(sys.argv[1])
    #get2dlowmaint(sys.argv[1])
    print sys.argv[0]
    ans = get4dhighmaint(sys.argv[1])
    for i in ans:
        print i
    
if __name__ == "__main__":
    main()