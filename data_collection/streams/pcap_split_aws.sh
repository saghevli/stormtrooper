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
    tshark -r $1 -w $2/stream-$stream.pcapng -R "tcp.stream==$stream"
    sudo editcap -F libpcap $2/stream-"$stream".pcapng $2/stream-"$stream".pcap
    sudo rm $2/stream-"$stream".pcapng
done
