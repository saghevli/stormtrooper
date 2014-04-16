(1) To install PyML (it's included in the repo)

cd PyML-0.7.13.3
python setup.py build
python setup.py install

REQUIRES numpy (a number library you probably already have)

(2) To install DPKT (it's also included in repo!)

cd dpkt-1.8
python setup.py build
python setup.py install

(3) To convert a PCAP file into a CSV for ML input:

> Open up datagen.py and change filename1 (line 16) to whatever .pcap file you want
> Or change the Reader input directly (line 26)
> Ideally datagen would take a command line arg or file input for PCAP file name
> Then run datagen.py and pipe output to file:

python datagen.py > datafilename.data

(4) To load a data file into the SVM and train it:

> Open up svmachine.py and change the input file name on line 7
> It defaults to 'google.data'
> Again, this is something that a future version could read from a config file or the command line
> Then simply run svmachine.py

python svmachine.py