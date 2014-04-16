# datagen.py
# generates CSV .data file for input to svmachine.py
# Requires DPKT by Dug Song & Jon Oberheide, available here: code.google.com/p/dpkt/downloads/list

# run like:
# python datagen.py > filename.data

from __future__ import print_function
import dpkt
import socket
import sys
import pprint
import operator

# run from data_collection
def main():
    if len(sys.argv) < 3:
        print("Usage: capcount.py <stream_dir> <number of files> <sorted(optional)>")
        return
    directory_name = sys.argv[1]
    max_file = int(sys.argv[2])
    last_time = 0
    flows = {}
    for i in range(0, max_file):
        packet_count = 0
        for ts, pkt in dpkt.pcap.Reader(open(directory_name + "/stream-" + str(i) + ".pcap", 'r')):
            packet_count += 1
        flows[i] = packet_count

    #pprint.pprint(flows)
    # sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
    sorted_flows = {}
    if len(sys.argv) >= 4 and sys.argv[3] == "sorted":
        sorted_flows = sorted(flows.values())
    else:
        sorted_flows = flows
    pprint.pprint(sorted_flows)
    #for key in sorted_flows:
     #   print(key)


if __name__ == "__main__":
    main()


