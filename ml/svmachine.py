# svmachine
# requires build & install of PyML (pyml.sourceforge.net)

import PyML
from PyML import *

datfile = 'datatraining'
testfile = 'datatesting'
# CSV organized like so:
# size, time delta, IsDestinationBlocked

data = VectorDataSet(datfile, labelsColumn = -1)
# the -1 means the last column (the Blocked boolean)

print "TRAINING DATA:"
print data

s = SVM()

print "SVM:"
print s

s.train(data)




#r = s.cv(data, numFolds=5)
#s.save(filename)
#new_svm = SVM() ;; new_svm.load(filename, data) ;; results = new_svm.test(test_data)


##testfile = 'google3.data'
testdata = VectorDataSet(testfile, labelsColumn = -1)
print "TEST DATA:"
print testdata

results = s.test(testdata)

print "SVM:"
print s

print "RESULTS:"
print results

