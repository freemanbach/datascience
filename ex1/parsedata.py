  
# Author  : freeman
# Date    : 2019.09.29
# Version : 0.0.1
# Desc    : 
#         : 
###################################################################

import json
import sys


def quit():
    sys.exit(0)


def readdata():
    if int(chkparams()) == 1:
        with open( sys.argv[1] , 'r') as fi:
            ds = json.load(fi)
    else:
        print "Insufficient Parameters."
        quit()

    return ds


# parentName, parentAge, parentKidAgeList
def findoldest(pn,pa,ka):
    nka, ca = [], 0
    for i in ka:
        nka.append(int(i))
    nka.sort()
    
    # find out age of parent from first born and latest born
    cao = int(pa) - int(nka[len(nka)-1])
    cay = int(pa) - int(nka[0])
    
    print "Parent name is:              " + pn
    print "Parent age is:               " + str(pa)
    print "Parent oldest is:            " + str(nka[len(nka)-1])
    print "Parent youngest is:          " + str(nka[0])
    print "Parent first Conceived age:  " + str(cao)
    print "Parent latest Conceived age: " + str(cay)
    

def procdata(tmpdata):
    kidsage = []
    name = tmpdata['firstname'] + "   " + tmpdata['lastname']
    age = tmpdata['age']
    print name
    print "Age is: " + str(age)
    print " hobbies are:" + " ".join(tmpdata['hobbies'])
    print "\n"
    
    kidsinfo = tmpdata['children']
    for items in kidsinfo:
        for k,v in items.iteritems():
            print str(k) + "    " + str(v)
            if str(v).isdigit():
                kidsage.append(str(v))
                
    return name,age, kidsage
            
        
def chkparams():
    args = sys.argv[1:]
    if len(args) <= 0:
        ans = False
    else:
        ans = True
        
    return ans


def main():
    data = readdata()
    name, age, kids = procdata(data)
    findoldest(name,age, kids)
    
    
if __name__ == "__main__":
    main()