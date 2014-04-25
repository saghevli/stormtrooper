#!/bin/sh
#splits streams in given file into separate streams
#places result files in passed in directory
#Usage: sh pcap_split.sh <input_filename> <output_directory>
#run from streams directory
mkdir $2
tshark -r $1 -T fields -e tcp.stream | sort -n | uniq
for stream in `tshark -r $1 -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -r $1 -F libpcap -w $2/stream-$stream.pcap -R "tcp.stream==$stream"
done
