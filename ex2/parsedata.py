import csv

def processGPA(mygpa):
    size, total = len(mygpa), 0.00
    for i in mygpa:
        total+=i
    avggpa = total / size
    
    return avggpa


def parseFile():
    
    data = "sampledata.txt"
    mygpa = []
    
    with open(data) as csvData:
        csv_read = csv.reader(csvData, delimiter=',')
        line = 0
        print "\n"

        for row in csv_read:
            if line == 0:
                print "Column names are {" +  "".join(row) + "}"
                line += 1
            else:
                #name, class, dorm, room, gpa
                print  "{ Student " + row[0] + " is in graduating class of " + row[1] + " living in " + row[2] + " room " + row[3] + " and gpa is " + row[4] + " .}"
                mygpa.append(float(row[4]))
                line += 1
         
        gpa = processGPA(mygpa)
        print "\n"*2
        print "Your GPA mean is: " + str(gpa)
        print "Processed: " + str(line) +   " lines."
        print "Processed: " + str(line-1) + " records."
    
def main():
    parseFile()
    
    
main()