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
        self.fields = []
        self.fieldtype = {}
        self.fieldcons = {}
        self.fieldmap = {}
        self.tableDef()
        
    def tableDef(self):
        # we expect to overload this in child classes
        pass
    
    def addField(self,dbfield,dbfieldtype,dbfieldcons,dictmap):
        print "adding field",dbfield
        self.fields.append(dbfield)
        self.fieldtype[dbfield] = dbfieldtype
        self.fieldcons[dbfield] = dbfieldcons
        self.fieldmap[dbfield] = dictmap
    
class dbTablePlayer(dbTable):
    def tableDef(self):
        self.addField('name','text','','textbox7')
        self.addField('age','int','','Age')
        self.addField('phone','text','','Phone')
        self.addField('gender','text','','Gender')
        self.addField('program','text','','textbox162')
        self.addField('address','text','','textbox20')
        self.addField('date','text','','SysDate')
               
class dbTableVolunteer(dbTable):
    def tableDef(self):
        self.addField('name','text','','textbox9')
        self.addField('phone','text','','textbox45')
        self.addField('program','text','','textbox24')
        self.addField('address','text','','textbox11')
        
class dataFile:
    def __init__(self,filename):
        self.filename = filename
        self.data = []
        self.readFile(filename)
        self.type = self.determineType()
        
    def readFile(self,filename):
        print "#### processing file:",filename
        #with open(filename) as f:
            #lines = f.readlines()
        lines = [line.strip('\r\n\357\273\277 ') for line in open(filename)]
        for line in lines:
            pass 
            
        record = csv.DictReader(lines, delimiter=',', quotechar='"')
        for row in record:
            self.data.append(row)
        
        
        #with open(filename, 'rb') as csvfile:
        #    record = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        #    for row in record:
        #        self.data.append(row)
                
    def determineType(self):
        # lets figure out what type it is...
        keystr = ','.join(sorted(self.data[0].keys()))
        print "Keystr:",keystr
        if keystr == 'Age,Court,Gender,Phone,SysDate,TShirtSize,TeamNumber,textbox162,textbox163,textbox20,textbox7':
            return 'p'
        elif keystr == 'Age,AgeDivision,LastName,TeamNumber,textbox11,textbox24,textbox27,textbox45,textbox46,textbox7,textbox9':
            return 'v'
        else:
            return 'na'
        
        
fileData = []
db = {}
        
for arg in args:
    fileData.append(dataFile(arg))
    
db['p'] = dbTablePlayer()
db['v'] = dbTableVolunteer()

for typ in ['p','v']:
    print "Looking for fileData of type:",typ
    for df in fileData:
        print "Checking file:",df.filename,df.type
        if df.type == typ:
            print "process:",df.filename,typ
    
