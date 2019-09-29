import csv

def parseFile():
    
    data = "sampledata.txt"
    
    with open(data) as csvData:
        csv_read = csv.reader(csvData, delimiter=',')
        line = 0
        for row in csv_read:
            if line == 0:
                print "Column names are {" +  "".join(row) + "}"
                line += 1
            else:
                #name, class, dorm, room, gpa
                print  "{ Student " + row[0] + " is in graduating class of " + row[1] + " living in " + row[2] + " room " + row[3] + " and gpa is " + row[4] + " .}"
                line += 1
        print "Processed: " + str(line) + " lines."
    
def main():
    parseFile()
    
    
main()