# Author   : freeman
# Date     : 2019.10.19
# version  : 0.0.3
# desc     : statistical functions 
#          : 
###################################################
import random
import time
import math
import sys


"""
Standard Mean
m    : a list of values,  meaning [] object
"""
def stdmean(m):
    sumofvalues = 0
    if str(type(m)).split("\'")[1] != 'list':
        print "Your input must be of type list !"
        sys.exit(1)
    else:
        # find the mean
        for i in m:
            sumofvalues+=i
    return float(sumofvalues) / len(m)


"""
A quick lib for finding out the Standard Deviation of a population 
from a list of values. N is the population.
myvalues    :  a list of population data, see above
total       :  sum of each of the data points minus the mean then square  
std         :  Standard deviation value
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
vac        :   a list object with data points, see stdmean function
"""
def variancepop(vac):
    return math.pow(stddevpop(vac), 2)


"""
A quick lib for finding out the Standard Deviation of a Sample 
population from a list of values. (N-1) is the sample population.
myvalues    :  a list of Sample population data, see above
total       :  sum of each of the data points minus the mean then square  
std         :  Standard deviation value
"""
def stddevsamp(myvalues):
    n = len(myvalues)
    total, mean, std = 0,0,0

    mean = stdmean(myvalues)

    # sum of all values from mean
    for i in myvalues:
        total+=math.pow(i-mean,2)
    std = total / (n-1)
    
    return math.sqrt(std) 


"""
Compute the Variance of a Sample Population
vac   : a list of sample population
"""
def variancesamp(vac):
    return math.pow(stddevsamp(vac), 2)


"""
Compute the Z-Score
x    : a single test score
mean : mean of the all the test scores
std  : Standard Deviation of your test score population 
"""
def zscore(x, mean, std):
    return float(x-mean) / std


def main():
    mylst, mylst2 = [], [3, 4, 4, 5, 6, 8]
    random.seed(time.time())
    for i in range(0,10):
        tmp = random.randint(0,20)
        mylst.append(tmp)
        
    #a =90
    #print stdmean(a)
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