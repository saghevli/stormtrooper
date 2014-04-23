#!/bin/sh
#Usage: sh pcap_split.sh <directory> <number of files>
#run from streams directory
for i in `seq 0 $2`
do
    editcap -F libpcap $1/stream-"$i".pcap $1/stream-"$i".pcap
done
