#!/usr/bin/env python
import csv
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--db", dest="db",help="write report to FILE", metavar="DB", default="./reg.sqlite3")
parser.add_option("-q", "--quiet",action="store_false", dest="verbose", default=True,help="don't print status messages to stdout")

(opts, args) = parser.parse_args()

class dbTable:
    def __init__(self):
        self.tableDef()
        
    def tableDef(self):
        # we expect to overload this in child classes
        pass
    def addField(self,dbfield,dbfieldtype,dictmap):
        print "adding field",dbfield
    
class dbTablePlayer(dbTable):
    def tableDef(self):
        self.addField('name','text','textbox7')
        self.addField('age','int','Age')
        self.addField('phone','text','Phone')
        self.addField('gender','text','Gender')
        self.addField('program','text','textbox162')
        self.addField('address','text','textbox20')
        self.addField('date','text','SysDate')
        
        
        #self.addField('address','text')
        #self.addField('address','text')
        #self.addField('address','text')
        #self.addField('address','text')
        
class dbTableVolunteer(dbTable):
    def tableDef(self):
        self.addField('name','text','textbox9')
        self.addField('phone','text','textbox45')
        self.addField('program','text','textbox24')
        self.addField('address','text','textbox11')
        
        
def processFile(file):
    # process each CSV file
    print "#### processing file:",file
    with open(file, 'rb') as csvfile:
        #record = csv.reader(csvfile, delimiter=',', quotechar='"')
        # we can differentiate between the types of input CSVs via the dict keys
        # wow, the DictReader uses the first line as the field header and automatically
        # pulls that from
        record = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        #print record.__len__()
        #header = record[0]
        recnum = 0
        for row in record:
            if recnum == 0:
                # need to figure out whether this is a volunteer or player so 
                # we know which table to put them in
                print '#header:','|'.join(row.values())
                
                # also need to sort out the mapping of column to db
            print '|'.join(row.values())
            recnum += 1
    
#for arg in args:
#    processFile(arg)
    
p = dbTablePlayer()
v = dbTableVolunteer()
    
