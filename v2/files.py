import json
import ast

def read(filen):

      f = open(filen, "r")

      filecont = (f.read())

      f.close()

      return filecont

def readjs(filen):

      f = open(filen, "r")

      filecont = json.loads(f.read())

      f.close()

      return filecont

def write(content,filen):

      f = open(filen, "w")

      f.write(content)

      f.close()

def writejs(jsonf,filen):

      f = open(filen, "w")

      f.write(json.dumps(jsonf))

      f.close()

 

#Thanks for your time

#Ben Simmons