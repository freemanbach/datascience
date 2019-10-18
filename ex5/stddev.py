import random
import time
import math


"""
A quick lib for finding out the Standard Deviation of a population 
from a list of values. N is the population.
"""
def stddevpop(myvalues):
    n = len(myvalues)
    sumofvalues, total, mean, std = 0,0,0,0
 
    # find the mean
    for i in myvalues:
        sumofvalues+=1
    mean = sumofvalues / len(myvalues)
 
    # sum of all values from mean
    for i in myvalues:
        total+=math.pow(i-mean,2)
    std = total / n
    
    return math.sqrt(std)


"""
A quick lib for finding out the Standard Deviation of a Sample 
population from a list of values. N-1 is the sample population.
"""
def stddevsamp(myvalues):
    n = len(myvalues)
    sumofvalues, total, mean, std = 0,0,0,0
 
    # find the mean
    for i in myvalues:
        sumofvalues+=1
    mean = sumofvalues / len(myvalues)
 
    # sum of all values from mean
    for i in myvalues:
        total+=math.pow(i-mean,2)
    std = total / (n-1)
    
    return math.sqrt(std)
 

def main():
    mylst = []
    random.seed(time.time())
    for i in range(0,10):
        tmp = random.randint(0,20)
        mylst.append(tmp)
        
    print str(mylst)
    stddev1 = stddevpop(mylst)
    print "Std deviation of a Population: " + str(stddev1)
    stddev2 = stddevsamp(mylst)
    print "Std deviation of a Sample Population: " + str(stddev2)

if __name__ == "__main__":
    main()
