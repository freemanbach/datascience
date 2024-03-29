# Author   : freeman
# Date     : 2019.10.22
# version  : 0.0.8
# desc     : statistical functions 
#          : 
###################################################
import random
import time
import math
import sys
from collections import OrderedDict


"""
Standard Mean
m    : a list of values,  meaning [] object
"""
def stdmean(m):
    sumofvalues = 0
    if str(type(m)).split("\'")[1] != 'list':
        print "Your input must be of type list !"
        sys.exit(1)
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


"""
Support Pearson correlation coefficient
"""
def sum_xy(a,b):
    xy=0
    if str(type(a)).split("\'")[1] != 'list' and str(type(b)).split("\'")[1] != 'list':
        print "Your inputs must be of type list !"
        sys.exit(1)

    if len(a) != len(b):
        print "Length of List A and List B dont equate."
        sys.exit(1)
        
    for i in range(0 , len(a)):
        xy += a[i]*b[i]
    
    return xy


"""
Support Pearson correlation coefficient
"""
def sum_x(a):
    x = 0
    for i in a:
        x+=i
    return x


"""
Support Pearson correlation coefficient
"""
def sum_y(b):
    y = 0
    for i in b:
        y+=i
    return y


"""
Support Pearson correlation coefficient
"""
def sum_x2(a):
    x2 = 0
    for i in a:
        x2+=math.pow(i,2)
    return x2
    

"""
Support Pearson correlation coefficient
"""
def sum_y2(b):
    y2 = 0
    for i in b:
        y2+=math.pow(i,2)
    return y2
   
    
"""
Pearson correlation coefficient
"""
def pearsoncc(x,y):
    s_x, s_y, s_xy, s_x2, s_y2 = 0,0,0,0,0
    
    if str(type(x)).split("\'")[1] != 'list' and str(type(x)).split("\'")[1] != 'list':
        print "Your inputs must be of type list !"
        sys.exit(1)

    if len(x) != len(y):
        print "Length of List X and List Y dont equate."
        sys.exit(1)

    s_x = sum_x(x)
    s_y = sum_y(y)
    s_x2 = sum_x2(x)
    s_y2 = sum_y2(y)
    s_xy = sum_xy(x,y)
        
    x1 = len(x)*s_x2 - math.pow(s_x, 2)
    y1 = len(x)*s_y2 - math.pow(s_y, 2)
    pcc = ((len(x)*s_xy)-(s_x*s_y)) / math.sqrt(x1*y1)
    
    return pcc


"""
Spearman rank correlation coefficient (List)
not sure if this data structure could be a dict or as a list
Problem is that Dictionary is not ordered like list O(N) and cant 
contain duplicates due to hash-table O(1). 
x    :  list 1
y    :  list 2
"""
def spearmanrcc(x,y):
    d = 0
    
    if str(type(x)).split("\'")[1] != 'list' and str(type(x)).split("\'")[1] != 'list':
        print "Your inputs must be of type list !"
        sys.exit(1)
        
    if len(x) != len(y):
        print "Length of List x and List y dont equate."
        sys.exit(1)
    
    for i in range(0, len(x)):
        d += math.pow(abs(x[i]-y[i]),2) 
    d = 6 * d
    srcc = 1 - ( d / ( len(x) * ( math.pow(len(x),2) - 1 )) )
    
    return srcc


"""
testing functions from above in main
"""
def main():
    
    #Spearman Rank Coefficient
    phy = [3, 5, 1, 6, 7, 2, 8, 9, 4]
    mth = [5, 3, 2, 6, 8, 1, 7, 9, 4]
    
    # random sample
    mylst, mylst2 = [], [3, 4, 4, 5, 6, 8]
    #Pearman corrolation coefficient
    age_x, glucose_y = [43,21,25,42,57,59] , [99,65,79,75,87,81]
    # Some other random things to test
    random.seed(time.time())
    for i in range(0,10):
        tmp = random.randint(0,20)
        mylst.append(tmp)
        
    #a =90
    #print stdmean(a)
    print "Ans is: " + str(spearmanrcc(phy, mth))
    print "Your answer is: " + str(pearsoncc(age_x, glucose_y))
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