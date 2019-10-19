import random
import time
import math


"""
Standard Mean
"""
def stdmean(m):
    sumofvalues = 0
    
    # find the mean
    for i in m:
        sumofvalues+=i
    return float(sumofvalues) / len(m)

    
"""
A quick lib for finding out the Standard Deviation of a population 
from a list of values. N is the population.
"""
def stddevpop(myvalues):
    n = len(myvalues)
    total, mean , std = 0,0,0
    
    mean = stdmean(myvalues)
 
    # sum of all values from mean
    for i in myvalues:
        total+=math.pow(i-mean,2)
    std = total / n
    
    return math.sqrt(std)


"""
Compute the Variance of a population.
"""
def variancepop(vac):
    return math.pow(stddevpop(vac), 2)

"""
A quick lib for finding out the Standard Deviation of a Sample 
population from a list of values. N-1 is the sample population.
"""
def stddevsamp(myvalues):
    n = len(myvalues)
    total, mean, std = 0,0,0,0

    mean = stdmean(myvalues)

    # sum of all values from mean
    for i in myvalues:
        total+=math.pow(i-mean,2)
    std = total / (n-1)
    
    return math.sqrt(std) 


"""
Compute the Variance of a Sample Population
"""
def variancesamp(vac):
    return math.pow(stddevsamp(vac), 2)


def main():
    mylst, mylst2 = [], [3, 4, 4, 5, 6, 8]
    random.seed(time.time())
    for i in range(0,10):
        tmp = random.randint(0,20)
        mylst.append(tmp)


    print str(mylst)
    stddev1 = stddevpop(mylst2)
    print "Std deviation of a Population: " + str(stddev1)
    stddev2 = stddevsamp(mylst2)
    print "Std deviation of a Sample Population: " + str(stddev2)
    print "\n"
    print "Variance of a population: " + str(variancepop(mylst2))
    print "Variance of a Sample population: " + str(variancesamp(mylst2))


if __name__ == "__main__":
    main()