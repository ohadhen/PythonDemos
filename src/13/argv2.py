#from sys import argv
import sys

print "the argument count is %d" % (len(sys.argv)-1)

print "The script is called:", sys.argv[0]
#for i in range(len(sys.argv)):
#    print "argument ",i+1,sys.argv[i]
for arg in sys.argv[1:]:
    print arg