#!/bin/sh
#splits streams in given file into separate streams
#places result files in passed in directory
#Usage: sh pcap_split.sh <input_filename> <output_directory>
#run from streams directory
mkdir $2
for stream in `tshark -r $1 -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -r $1 -F pcap -w $2/stream-$stream.pcap -Y "tcp.stream==$stream"
done
